import os
import requests

from aiohttp import ClientSession, FormData

from .types import SpeechToTextResult
from .exceptions import ApiException

from json import dumps


class SpeechToText:
    @staticmethod
    def to_text(file_path: str, language: str = "en") -> "SpeechToTextResult":
        """Speech to text using google cloud.

        Args:
            file_path (str): The path to the audio file to be transcribed into text. This should be a valid path to an audio file
            language (str, optional): the source language code of the audio file. Defaults to "en". Supported languages are: en, ar
        """
        with open(file_path, "rb") as f:
            b = f.read()
        response = requests.post(
            "https://api.devrio.org/api/v1/SpeechToText/",
            data={
                "language": language,
            },
            files={"file": b},
        )
        try:
            result = response.json()
        except Exception as e:
            raise BaseException(str(e))

        if not result["ok"]:
            raise ApiException(dumps(result["error"], indent=2, ensure_ascii=False))

        return SpeechToTextResult.parse(result, file_path)


class AsyncSpeechToText:
    @staticmethod
    async def to_text(file_path: str, language: str = "en") -> "SpeechToTextResult":
        """Speech to text using google cloud.

        Args:
            file_path (str): The path to the audio file to be transcribed into text. This should be a valid path to an audio file
            language (str, optional): the source language code of the audio file. Defaults to "en". Supported languages are: en, ar
        """
        with open(file_path, "rb") as f:
            b = f.read()
        async with ClientSession() as session:
            form = FormData()
            form.add_field("file", b, filename=os.path.basename(file_path))
            form.add_field("language", language)
            async with session.request(
                "post", "https://api.devrio.org/api/v1/SpeechToText/", data=form
            ) as response:
                try:
                    result = await response.json()
                except Exception as e:
                    raise BaseException(str(e))

                if not result["ok"]:
                    raise ApiException(
                        dumps(result["error"], indent=2, ensure_ascii=False)
                    )

                return SpeechToTextResult.parse(result, file_path)
