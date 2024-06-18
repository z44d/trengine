from aiohttp import ClientSession

from .types import AjaxTranslateResult
from .exceptions import ApiException

import requests


class AjaxTranslator:
    @staticmethod
    def translate(
        text: str, translated_lang: str = "en", source_lang: str = None
    ) -> "AjaxTranslateResult":
        """Translate a text using ajax engine.

        Args:
            text (str): the text to translate.
            translated_lang (str, optional): The lang code of target lang. Defaults to "en".
            source_lang (str, optional): Source lang of the text. Defaults to None.
        """
        source_lang = source_lang or AjaxTranslator.detect(text)
        response = requests.post(
            "https://www.translate.com/translator/ajax_translate",
            data={
                "text_to_translate": text,
                "translated_lang": translated_lang,
                "source_lang": source_lang,
                "use_cache_only": "false",
            },
        )
        try:
            result = response.json()
        except Exception as e:
            return BaseException(str(e))

        if not result["result"] == "success":
            raise ApiException(result["message"])

        return AjaxTranslateResult.parse(result, source_lang)

    @staticmethod
    def detect(text: str) -> str:
        """Detect language code from text.

        Args:
            text (str): The text.
        """
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


class AsyncAjaxTranslator:
    @staticmethod
    async def translate(
        text: str, translated_lang: str = "en", source_lang: str = None
    ) -> "AjaxTranslateResult":
        """Translate a text using ajax engine.

        Args:
            text (str): the text to translate.
            translated_lang (str, optional): The lang code of target lang. Defaults to "en".
            source_lang (str, optional): Source lang of the text. Defaults to None.
        """
        source_lang = source_lang or await AsyncAjaxTranslator.detect(text)
        async with ClientSession() as session:
            async with session.post(
                "https://www.translate.com/translator/ajax_translate",
                data={
                    "text_to_translate": text,
                    "translated_lang": translated_lang,
                    "source_lang": source_lang,
                    "use_cache_only": "false",
                },
            ) as response:
                try:
                    result = await response.json()
                except Exception as e:
                    return BaseException(str(e))
                if not result["result"] == "success":
                    raise ApiException(result["message"])

            return AjaxTranslateResult.parse(result, source_lang)

    @staticmethod
    async def detect(text: str) -> str:
        """Detect language code from text.

        Args:
            text (str): The text.
        """
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
