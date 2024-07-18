from . import (
    google,
    hozory,
    speech_to_text,
    tdict,
    ocr,
    text_to_speech,
    identify_music,
    tr,
)

__all__ = ["AsyncEngine", "Engine"]

HEADERS = {
    "User-Agent": "GoogleTranslate/6.6.1.RC09.302039986 (Linux; U; Android 9; Redmi Note 8)"
}


class Engine:
    @property
    def tr(self) -> "tr.AjaxTranslator":
        """Use ajax engine.

        Returns:
            ajax.AjaxTranslator: Ajax Engine Class.
        """
        return tr.Translator

    @property
    def google(self) -> "google.GoogleTranslator":
        """Use google engine.

        Returns:
            google.GoogleTranslator: Google Engine Class.
        """
        return google.GoogleTranslator

    @property
    def hozory(self) -> "hozory.HozoryTranslator":
        """Use hozory engine.

        Returns:
            hozory.HozoryTranslator: Hozory Engine Class.
        """
        return hozory.HozoryTranslator

    @property
    def tdict(self) -> "tdict.TdictTranslator":
        """Use tdict engine.

        Returns:
            tdict.TdictTranslator: tdict Engine Class.
        """
        return tdict.TdictTranslator

    @property
    def ocr(self) -> "ocr.OCR":
        """Use OCR service.

        Returns:
            ocr.OCR: Ocr Class.
        """
        return ocr.OCR

    @property
    def speech_to_text(self) -> "speech_to_text.SpeechToText":
        """Use speech_to_text service.

        Returns:
            speech_to_text.SpeechToText: speech_to_text Engine Class.
        """
        return speech_to_text.SpeechToText

    @property
    def text_to_speech(self) -> "text_to_speech.TextToSpeech":
        """Use text_to_speech service.

        Returns:
            text_to_speech.TextToSpeech: text_to_speech Engine Class.
        """
        return text_to_speech.TextToSpeech

    @property
    def identify_music(self) -> "identify_music.IdentifyMusic":
        """Use identify_music service.

        Returns:
            identify_music.IdentifyMusic: identify_music Engine Class.
        """
        return identify_music.IdentifyMusic


class AsyncEngine:
    @property
    def tr(self) -> "tr.AsyncAjaxTranslator":
        """Use ajax engine.

        Returns:
            ajax.AsyncAjaxTranslator: Ajax Engine Class.
        """
        return tr.AsyncTranslator

    @property
    def google(self) -> "google.AsyncGoogleTranslator":
        """Use google engine.

        Returns:
            google.AsyncGoogleTranslator: Google Engine Class.
        """
        return google.AsyncGoogleTranslator

    @property
    def hozory(self) -> "hozory.AsyncHozoryTranslator":
        """Use hozory engine.

        Returns:
            hozory.AsyncHozoryTranslator: Hozory Engine Class.
        """
        return hozory.AsyncHozoryTranslator

    @property
    def tdict(self) -> "tdict.AsyncTdictTranslator":
        """Use tdict engine.

        Returns:
            tdict.AsyncTdictTranslator: tdict Engine Class.
        """
        return tdict.AsyncTdictTranslator

    @property
    def ocr(self) -> "ocr.AsyncOCR":
        """Use OCR service.

        Returns:
            ocr.AsyncOCR: Ocr Class.
        """
        return ocr.AsyncOCR

    @property
    def speech_to_text(self) -> "speech_to_text.AsyncSpeechToText":
        """Use speech_to_text service.

        Returns:
            speech_to_text.AsyncSpeechToText: speech_to_text Engine Class.
        """
        return speech_to_text.AsyncSpeechToText

    @property
    def text_to_speech(self) -> "text_to_speech.AsyncTextToSpeech":
        """Use text_to_speech service.

        Returns:
            text_to_speech.AsyncTextToSpeech: text_to_speech Engine Class.
        """
        return text_to_speech.AsyncTextToSpeech

    @property
    def identify_music(self) -> "identify_music.AsyncIdentifyMusic":
        """Use identify_music service.

        Returns:
            identify_music.AsyncIdentifyMusic: identify_music Engine Class.
        """
        return identify_music.AsyncIdentifyMusic
