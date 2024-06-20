from trengine.speechtotext import AsyncSpeechToTextService

speech = AsyncSpeechToTextService()


async def main():
    print(await speech.toText('audio.ogg', language='en'))


import asyncio

asyncio.run(main())
