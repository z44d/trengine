import requests
import aiohttp
import json


from .exceptions import ApiException
from typing import Union


class OCR:
    def __init__(self) -> None:
        pass

    def from_image(self, path: Union[str, bytes], language: str = "eng") -> str:
        if isinstance(path, bytes):
            b = path
        else:
            with open(path, "rb") as f:
                b = f.read()
        response = requests.post(
            "https://api8.ocr.space/parse/image",
            data={
                "language": language,
                "isOverlayRequired": True,
                "OCREngine": 1,
                "detectCheckbox": False,
                "IsCreateSearchablePDF": False,
                "isSearchablePdfHideTextLayer": True,
                "FileType": ".AUTO",
            },
            headers={
                "Apikey": "donotstealthiskey_ip1",
            },
            files={"file": b},
        )
        try:
            result = response.json()
        except Exception as e:
            raise BaseException(str(e))

        if isinstance(result, str):
            raise ApiException(result)
        if not result.get("ParsedResults"):
            raise ApiException(json.dumps(result, indent=4, ensure_ascii=False))

        return result["ParsedResults"][0]["ParsedText"]


class AsyncOCR:
    def __init__(self) -> None:
        pass

    async def from_image(self, path: Union[str, bytes], language: str = "eng") -> str:
        if isinstance(path, bytes):
            b = path
        else:
            with open(path, "rb") as f:
                b = f.read()
        async with aiohttp.ClientSession(
            headers={"Apikey": "donotstealthiskey_ip1"}
        ) as session:
            payload = {
                "language": language,
                "isOverlayRequired": True,
                "OCREngine": 1,
                "detectCheckbox": False,
                "IsCreateSearchablePDF": False,
                "isSearchablePdfHideTextLayer": True,
                "FileType": ".AUTO",
            }
            data = aiohttp.formdata.FormData(quote_fields=False)
            for k, v in payload.items():
                data.add_field(k, str(v))
            data.add_field("file", b, filename="photo.png")
            async with session.post(
                "https://api8.ocr.space/parse/image", data=data
            ) as response:
                try:
                    result = await response.json()
                except Exception as e:
                    raise BaseException(str(e))

                if isinstance(result, str):
                    raise ApiException(result)
                if not result.get("ParsedResults"):
                    raise ApiException(json.dumps(result, indent=4, ensure_ascii=False))

                return result["ParsedResults"][0]["ParsedText"]
