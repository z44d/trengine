from trengine.ocr import AsyncOCR

ocr = AsyncOCR()


async def main():
    print(await ocr.from_image("./test.png", language="eng"))


import asyncio

asyncio.run(main())
