from trengine.speech_to_text import AsyncSpeechToText

speech = AsyncSpeechToText()


async def main():
    print(await speech.to_text("audio.ogg", language="en"))


import asyncio

asyncio.run(main())
