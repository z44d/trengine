import requests
import aiohttp
import json
import os

from aiofiles import open as AsyncOpen

from .exceptions import ApiException


class OCR:
    def __init__(self) -> None:
        pass

    def from_image(self, path: str, language: str = "eng") -> str:
        with open(path, "rb") as f:
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
                files={"file": f},
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

    async def from_image(self, path: str, language: str = "eng") -> str:
        async with AsyncOpen(path, "rb") as f:
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
                data.add_field("file", await f.read(), filename=os.path.basename(path))
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
                        raise ApiException(
                            json.dumps(result, indent=4, ensure_ascii=False)
                        )

                    return result["ParsedResults"][0]["ParsedText"]
