from aiohttp import ClientSession

from .types import HozoryTranslateResult
from .exceptions import ApiException

from json import dumps

import requests


class HozoryTranslator:
    def __init__(self) -> None:
        pass

    def translate(self, text: str, dest: str = "en") -> "HozoryTranslateResult":
        response = requests.get(
            f"https://hozory.com/translate/?target={dest}&text={text}"
        )
        try:
            result = response.json()
        except Exception as e:
            raise BaseException(str(e))

        if not result["status"] == "ok":
            raise ApiException(dumps(result["result"], indent=2, ensure_ascii=False))

        return HozoryTranslateResult.parse(result["result"], dest)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return self


class AsyncHozoryTranslator:
    def __init__(self) -> None:
        pass

    async def translate(self, text: str, dest: str = "en") -> "HozoryTranslateResult":
        async with ClientSession() as session:
            async with session.get(
                f"https://hozory.com/translate/?target={dest}&text={text}"
            ) as response:
                try:
                    result = await response.json()
                except Exception as e:
                    raise BaseException(str(e))

                if not result["status"] == "ok":
                    raise ApiException(
                        dumps(result["result"], indent=2, ensure_ascii=False)
                    )

                return HozoryTranslateResult.parse(result["result"], dest)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        return self
