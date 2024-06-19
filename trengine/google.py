from aiohttp import ClientSession

from .types import GoogleTranslateResult

import requests, trengine


class GoogleTranslator:
    @staticmethod
    def translate(
        text: str, to_language: str = "en", source_language: str = "auto"
    ) -> "GoogleTranslateResult":
        """Translate a text using google engine.

        Args:
            text (str): the text to translate.
            to_language (str, optional): The lang code of target lang. Defaults to "en".
            source_language (str, optional): Source lang of the text. Defaults to "auto".
        """
        response = requests.get(
            f"https://clients5.google.com/translate_a/t?client=at&sl={source_language}&tl={to_language}&q={text}",
            headers=trengine.HEADERS,
        )
        try:
            result = response.json()
        except Exception as e:
            raise BaseException(str(e))

        return GoogleTranslateResult.parse(result[0], to_language)


class AsyncGoogleTranslator:
    @staticmethod
    async def translate(
        text: str, to_language: str = "en", source_language: str = "auto"
    ) -> "GoogleTranslateResult":
        """Translate a text using google engine.

        Args:
            text (str): the text to translate.
            to_language (str, optional): The lang code of target lang. Defaults to "en".
            source_language (str, optional): Source lang of the text. Defaults to "auto".
        """
        async with ClientSession(headers=trengine.HEADERS) as session:
            async with session.get(
                f"https://clients5.google.com/translate_a/t?client=at&sl={source_language}&tl={to_language}&q={text}"
            ) as response:
                try:
                    result = await response.json()
                except Exception as e:
                    raise BaseException(str(e))

                return GoogleTranslateResult.parse(
                    result[0],
                    to_language,
                    source_language if source_language != "auto" else None,
                )
