from aiohttp import ClientSession

from .types import AjaxTranslateResult
from .exceptions import ApiException

import requests, trengine


class Translator:
    @staticmethod
    def translate(
        text: str, translated_lang: str = "en", source_lang: str = None
    ) -> "AjaxTranslateResult":
        """Translate a text using tr engine.

        Args:
            text (str): the text to translate.
            translated_lang (str, optional): The lang code of target lang. Defaults to "en".
            source_lang (str, optional): Source lang of the text. Defaults to None.
        """
        source_lang = source_lang or Translator.detect(text)
        response = requests.post(
            "https://www.translate.com/translator/ajax_translate",
            data={
                "text_to_translate": text,
                "translated_lang": translated_lang,
                "source_lang": source_lang,
                "use_cache_only": "false",
            },
            headers=trengine.HEADERS,
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
            headers=trengine.HEADERS,
        )
        try:
            result = response.json()
        except Exception as e:
            return BaseException(str(e))
        if not result["result"] == "success":
            raise ApiException(result["message"])

        return result["language"]


class AsyncTranslator:
    @staticmethod
    async def translate(
        text: str, translated_lang: str = "en", source_lang: str = None
    ) -> "AjaxTranslateResult":
        """Translate a text using tr engine.

        Args:
            text (str): the text to translate.
            translated_lang (str, optional): The lang code of target lang. Defaults to "en".
            source_lang (str, optional): Source lang of the text. Defaults to None.
        """
        source_lang = source_lang or await AsyncTranslator.detect(text)
        async with ClientSession(headers=trengine.HEADERS) as session:
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
                    print(result)
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
                headers=trengine.HEADERS,
            ) as response:
                try:
                    result = await response.json()
                except Exception as e:
                    return BaseException(str(e))
                if not result["result"] == "success":
                    raise ApiException(result["message"])

                return result["language"]
