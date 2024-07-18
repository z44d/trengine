from trengine.tr import Translator

engine = Translator()

print(engine.translate("Hi everyone!", "ar"), "\n", engine.detect("مرحبًا"))
