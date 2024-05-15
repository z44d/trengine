from aiohttp import ClientSession

from .types import GoogleTranslateResult

import requests


class GoogleTranslator:
    def __init__(self) -> None:
        pass

    def translate(self, text: str, dest: str = "en") -> "GoogleTranslateResult":
        response = requests.get(
            f"https://clients5.google.com/translate_a/t?client=at&sl=auto&tl={dest}&q={text}"
        )
        try:
            result = response.json()
        except Exception as e:
            raise BaseException(str(e))

        return GoogleTranslateResult.parse(result[0], dest)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return self


class AsyncGoogleTranslator:
    def __init__(self) -> None:
        pass

    async def translate(self, text: str, dest: str = "en") -> "GoogleTranslateResult":
        async with ClientSession() as session:
            async with session.get(
                f"https://clients5.google.com/translate_a/t?client=at&sl=auto&tl={dest}&q={text}"
            ) as response:
                try:
                    result = await response.json()
                except Exception as e:
                    raise BaseException(str(e))

                return GoogleTranslateResult.parse(result[0], dest)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        return self
