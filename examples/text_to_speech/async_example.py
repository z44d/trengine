from trengine.text_to_speech import AsyncTextToSpeech

text = AsyncTextToSpeech()


async def main():
    print(await text.to_speech("Hello, how are you doing today?", "audio.mp3", "en"))


import asyncio

asyncio.run(main())
