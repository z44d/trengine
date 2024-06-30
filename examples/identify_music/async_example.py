from trengine.identify_music import AsyncIdentifyMusic

ide = AsyncIdentifyMusic()


async def main():
    print(await ide.identify("audio.mp3"))


import asyncio

asyncio.run(main())
