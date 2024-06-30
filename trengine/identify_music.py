import os
import requests

from aiohttp import ClientSession, FormData

from .types import IdentifyMusicResult
from .exceptions import ApiException

from json import dumps


class IdentifyMusic:
    @staticmethod
    def identify(file_path: str) -> "IdentifyMusicResult":
        """Identify music using shazam.

        Args:
            file_path (str): The path to the audio file to be identified. This should be a valid path to an audio file
        """
        with open(file_path, "rb") as f:
            b = f.read()
        response = requests.post(
            "https://api.devrio.org/api/v1/idetifymusic/",
            files={"file": (os.path.basename(file_path), b)},
        )
        try:
            result = response.json()
        except Exception as e:
            raise BaseException(str(e))

        if not result["ok"]:
            raise ApiException(dumps(result["error"], indent=2, ensure_ascii=False))

        return IdentifyMusicResult.parse(result, file_path)


class AsyncIdentifyMusic:
    @staticmethod
    async def identify(file_path: str) -> "IdentifyMusicResult":
        """Identify music using shazam.

        Args:
            file_path (str): The path to the audio file to be identified. This should be a valid path to an audio file
        """
        with open(file_path, "rb") as f:
            b = f.read()
        async with ClientSession() as session:
            form = FormData()
            form.add_field("file", b, filename=os.path.basename(file_path))
            async with session.request(
                "post", "https://api.devrio.org/api/v1/idetifymusic/", data=form
            ) as response:
                try:
                    result = await response.json()
                except Exception as e:
                    raise BaseException(str(e))
                if not result["ok"]:
                    raise ApiException(
                        dumps(result["error"], indent=2, ensure_ascii=False)
                    )

                return IdentifyMusicResult.parse(result, file_path)
