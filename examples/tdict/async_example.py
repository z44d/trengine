from trengine.tdict import AsyncTdictTranslator

import asyncio

tdict_engine = AsyncTdictTranslator()


async def main():
    print(
        await tdict_engine.translate("Hi everyone!", "ar"),
    )


asyncio.run(main())

# Note: there is no special return type for tdict, it's always return string
