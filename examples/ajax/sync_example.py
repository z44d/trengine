from trengine.ajax import AjaxTranslator

ajax_engine = AjaxTranslator()

print(ajax_engine.translate("Hi everyone!", "ar"), "\n", ajax_engine.detect("مرحبًا"))
