from trengine.google import AsyncGoogleTranslator

import asyncio

google_engine = AsyncGoogleTranslator()


async def main():
    print(
        await google_engine.translate("Hi everyone!", "ar"),
    )


asyncio.run(main())
