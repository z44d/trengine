from . import ajax, google, hozory, tdict, ocr

__all__ = ["AsyncEngine", "Engine"]


class Engine:
    @property
    def ajax(self) -> "ajax.AjaxTranslator":
        """Use ajax engine.

        Returns:
            ajax.AjaxTranslator: Ajax Engine Class.
        """
        return ajax.AjaxTranslator

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


class AsyncEngine:
    @property
    def ajax(self) -> "ajax.AsyncAjaxTranslator":
        """Use ajax engine.

        Returns:
            ajax.AsyncAjaxTranslator: Ajax Engine Class.
        """
        return ajax.AsyncAjaxTranslator

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
