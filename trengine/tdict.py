from aiohttp import ClientSession

import requests, trengine


class TdictTranslator:
    @staticmethod
    def translate(text: str, to_language: str = "en") -> str:
        """Translate a text using tdict engine.

        Args:
            text (str): the text to translate.
            to_language (str, optional): The lang code of target lang. Defaults to "en".
        """
        response = requests.get(
            f"https://t3.translatedict.com/1.php?p1=auto&p2={to_language}&p3={text}",
            headers=trengine.HEADERS,
        )
        return response.text


class AsyncTdictTranslator:
    @staticmethod
    async def translate(text: str, to_language: str = "en") -> str:
        """Translate a text using tdict engine.

        Args:
            text (str): the text to translate.
            to_language (str, optional): The lang code of target lang. Defaults to "en".
        """
        async with ClientSession(headers=trengine.HEADERS) as session:
            async with session.get(
                f"https://t3.translatedict.com/1.php?p1=auto&p2={to_language}&p3={text}"
            ) as response:
                return await response.text("utf-8")
