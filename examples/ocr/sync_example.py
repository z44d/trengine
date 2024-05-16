from trengine.ocr import OCR

ocr = OCR()

print(ocr.from_image("./test.png", language="ara"))
