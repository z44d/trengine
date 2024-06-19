from aiohttp import ClientSession

from .types import HozoryTranslateResult
from .exceptions import ApiException

from json import dumps

import requests, trengine


class HozoryTranslator:
    @staticmethod
    def translate(text: str, target: str = "en") -> "HozoryTranslateResult":
        """Translate a text using hozory engine.

        Args:
            text (str): the text to translate.
            target (str, optional): The lang code of target lang. Defaults to "en".
        """
        response = requests.get(
            f"https://hozory.com/translate/?target={target}&text={text}",
            headers=trengine.HEADERS,
        )
        try:
            result = response.json()
        except Exception as e:
            raise BaseException(str(e))

        if not result["status"] == "ok":
            raise ApiException(dumps(result["result"], indent=2, ensure_ascii=False))

        return HozoryTranslateResult.parse(result["result"], target)


class AsyncHozoryTranslator:
    @staticmethod
    async def translate(text: str, target: str = "en") -> "HozoryTranslateResult":
        """Translate a text using hozory engine.

        Args:
            text (str): the text to translate.
            target (str, optional): The lang code of target lang. Defaults to "en".
        """
        async with ClientSession() as session:
            async with session.get(
                f"https://hozory.com/translate/?target={target}&text={text}",
                headers=trengine.HEADERS,
            ) as response:
                try:
                    result = await response.json()
                except Exception as e:
                    raise BaseException(str(e))

                if not result["status"] == "ok":
                    raise ApiException(
                        dumps(result["result"], indent=2, ensure_ascii=False)
                    )

                return HozoryTranslateResult.parse(result["result"], target)
