from aiohttp import ClientSession

import requests


class TdictTranslator:
    def __init__(self) -> None:
        pass

    def translate(self, text: str, dest: str = "en") -> str:
        response = requests.get(
            f"https://t3.translatedict.com/1.php?p1=auto&p2={dest}&p3={text}"
        )
        return response.text

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return self


class AsyncTdictTranslator:
    def __init__(self) -> None:
        pass

    async def translate(self, text: str, dest: str = "en") -> str:
        async with ClientSession() as session:
            async with session.get(
                f"https://t3.translatedict.com/1.php?p1=auto&p2={dest}&p3={text}"
            ) as response:
                return await response.text("utf-8")

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        return self
