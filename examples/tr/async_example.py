from trengine.tr import AsyncTranslator

import asyncio

engine = AsyncTranslator()


async def main():
    print(
        await engine.translate("Hi everyone!", "ar"),
        "\n",
        await engine.detect("مرحبًا"),
    )


asyncio.run(main())
