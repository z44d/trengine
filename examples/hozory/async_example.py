from trengine.hozory import AsyncHozoryTranslator

import asyncio

hozory_engine = AsyncHozoryTranslator()


async def main():
    print(
        await hozory_engine.translate("Hi everyone!", "ar"),
    )


asyncio.run(main())
