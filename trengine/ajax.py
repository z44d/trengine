from aiohttp import ClientSession

from .types import AjaxTranslateResult
from .exceptions import ApiException

import requests


class AjaxTranslator:
    def __init__(self) -> None:
        pass

    def translate(self, text: str, dest: str = "en") -> "AjaxTranslateResult":
        org = self.detect(text)
        response = requests.post(
            "https://www.translate.com/translator/ajax_translate",
            data={
                "text_to_translate": text,
                "translated_lang": dest,
                "source_lang": org,
                "use_cache_only": "false",
            },
        )
        try:
            result = response.json()
        except Exception as e:
            return BaseException(str(e))

        if not result["result"] == "success":
            raise ApiException(result["message"])

        return AjaxTranslateResult.parse(result, org)

    def detect(self, text: str) -> str:
        response = requests.post(
            "https://www.translate.com/translator/ajax_lang_auto_detect",
            data={"text_to_translate": text},
        )
        try:
            result = response.json()
        except Exception as e:
            return BaseException(str(e))
        if not result["result"] == "success":
            raise ApiException(result["message"])

        return result["language"]

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return self


class AsyncAjaxTranslator:
    def __init__(self) -> None:
        pass

    async def translate(self, text: str, dest: str = "en") -> "AjaxTranslateResult":
        org = await self.detect(text)
        async with ClientSession() as session:
            async with session.post(
                "https://www.translate.com/translator/ajax_translate",
                data={
                    "text_to_translate": text,
                    "translated_lang": dest,
                    "source_lang": org,
                    "use_cache_only": "false",
                },
            ) as response:
                try:
                    result = await response.json()
                except Exception as e:
                    return BaseException(str(e))
                if not result["result"] == "success":
                    raise ApiException(result["message"])

            return AjaxTranslateResult.parse(result, org)

    async def detect(self, text: str) -> str:
        async with ClientSession() as session:
            async with session.post(
                "https://www.translate.com/translator/ajax_lang_auto_detect",
                data={"text_to_translate": text},
            ) as response:
                try:
                    result = await response.json()
                except Exception as e:
                    return BaseException(str(e))
                if not result["result"] == "success":
                    raise ApiException(result["message"])

                return result["language"]

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        return self
