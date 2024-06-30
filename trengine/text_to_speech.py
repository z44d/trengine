import requests
import base64
from aiohttp import ClientSession

from .types import TextToSpeechResult
from .exceptions import ApiException

from json import dumps


class TextToSpeech:
    @staticmethod
    def to_speech(
        text: str, output_path: str, language: str = "en"
    ) -> "TextToSpeechResult":
        """Text to speech using google translate.

        Args:
            text (str): The text to be converted into speech
            language (str, optional): the source language code of the text. Defaults to "en".
            out_put_path (str): The path to save the output audio file
        """
        response = requests.post(
            "https://api.devrio.org/api/v1/tts/",
            json={
                "language": language,
                "text": text,
            },
        )
        try:
            result = response.json()

            if not result["ok"]:
                raise ApiException(dumps(result["error"], indent=2, ensure_ascii=False))

            with open(output_path, "wb") as f:
                f.write(base64.b64decode(result["result"]))

        except Exception as e:
            raise BaseException(str(e))

        return TextToSpeechResult.parse(result, output_path)


class AsyncTextToSpeech:
    @staticmethod
    async def to_speech(
        text: str, output_path: str, language: str = "en"
    ) -> "TextToSpeechResult":
        """Text to speech using google translate.

        Args:
            text (str): The text to be converted into speech
            language (str, optional): the source language code of the text. Defaults to "en".
            out_put_path (str): The path to save the output audio file
        """
        async with ClientSession() as session:
            async with session.post(
                "https://api.devrio.org/api/v1/tts/",
                json={
                    "language": language,
                    "text": text,
                },
            ) as response:
                try:
                    result = await response.json()

                    if not result["ok"]:
                        raise ApiException(
                            dumps(result["error"], indent=2, ensure_ascii=False)
                        )

                    with open(output_path, "wb") as f:
                        f.write(base64.b64decode(result["result"]))

                except Exception as e:
                    raise BaseException(str(e))

        return TextToSpeechResult.parse(result, output_path)
