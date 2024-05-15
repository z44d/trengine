from trengine.ajax import AsyncAjaxTranslator

import asyncio

ajax_engine = AsyncAjaxTranslator()


async def main():
    print(
        await ajax_engine.translate("Hi everyone!", "ar"),
        "\n",
        await ajax_engine.detect("مرحبًا"),
    )


asyncio.run(main())
