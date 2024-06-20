import requests
import aiohttp
import aiofiles
import json
from .types import SpeechToTextResult
from .exceptions import ApiException

class SpeechToText:
    @staticmethod
    def speechtotext(file_path: str, language: str = "en") -> SpeechToTextResult:
       """Speech to text using google cloud.

        Args:
            file_path (str): The path to the audio file to be translated into text. This should be a valid path to an audio file 
            language (str, optional): he language code for the speech in the audio file. Defaults to "en".
        """
        url = "https://api.devrio.org/api/v1/SpeechToText/"
        try:
            with open(file_path, 'rb') as file:
                files = {'file': file}
                data = {'language': language}
                response = requests.post(url, files=files, data=data)
                result = response.json()

                if not result.get("ok", False):
                    raise ApiException(
                        json.dumps(result.get("error", {}), indent=2, ensure_ascii=False)
                    )

                return SpeechToTextResult.parse(result, file_path)

        except Exception as e:
            raise BaseException(f"Unexpected error occurred: {e}")

class AsyncSpeechToText:
    @staticmethod
    async def speech_to_text(file_path: str, language: str = "en") -> SpeechToTextResult:
        """Speech to text using google cloud.

        Args:
            file_path (str): The path to the audio file to be translated into text. This should be a valid path to an audio file 
            language (str, optional): he language code for the speech in the audio file. Defaults to "en".
        """
        url = "https://api.devrio.org/api/v1/SpeechToText/"
        try:
            async with aiohttp.ClientSession() as session:
                async with aiofiles.open(file_path, mode='rb') as file:
                    data = aiohttp.FormData()
                    data.add_field('file', await file.read(), filename=file_path.split('/')[-1])
                    data.add_field('language', language)

                    async with session.post(url, data=data) as response:
                        result = await response.json()

                        if not result.get("ok", False):
                            raise ApiException(
                                json.dumps(result.get("error", {}), indent=2, ensure_ascii=False)
                            )

                        return SpeechToTextResult.parse(result, file_path)

        except aiohttp.ClientError as e:
            raise BaseException(f"HTTP error occurred: {e}")

        except Exception as e:
            raise BaseException(f"Unexpected error occurred: {e}")
