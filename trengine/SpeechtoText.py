import aiohttp
from aiohttp import ClientSession, FormData
from json import dumps
from .types import SpeechToTextResult
from .exceptions import ApiException

class AsyncSpeechToText:
    @staticmethod
    async def speechtotext(file_path: str, language: str = "en") -> SpeechToTextResult:
        """Speech to text using google cloud.

        Args:
            file_path (str): The path to the audio file to be translated into text. This should be a valid path to an audio file 
            language (str, optional): he language code for the speech in the audio file. Defaults to "en".
        """
        url = "https://api.devrio.org/api/v1/SpeechToText/"
        
        try:
            async with aiohttp.ClientSession() as session:
                form = FormData()
                form.add_field('file', open(file_path, 'rb'), filename=file_path)
                form.add_field('language', language)

                async with session.post(url, data=form) as response:
                    if response.status != 200:
                        raise ApiException(f"Failed to upload file. Status code: {response.status}")

                    result = await response.json()

                    if not result.get("ok"):
                        raise ApiException(dumps(result.get("error"), indent=2, ensure_ascii=False))

                    return SpeechToTextResult.parse(result, file_path)

        except aiohttp.ClientError as ce:
            raise BaseException(f"Error during HTTP request: {str(ce)}")
        except Exception as e:
            raise BaseException(f"Unexpected error: {str(e)}")
