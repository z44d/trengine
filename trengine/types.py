from dataclasses import dataclass
from json import dumps


class Base:
    @staticmethod
    def default(obj: "Base"):
        return {
            **{
                attr: (getattr(obj, attr))
                for attr in filter(lambda x: not x.startswith("_"), obj.__dict__)
                if getattr(obj, attr) is not None
            },
        }

    def __str__(self) -> str:
        return dumps(self, indent=4, default=Base.default, ensure_ascii=False)


@dataclass
class GoogleTranslateResult(Base):
    translated_text: str
    original_language: str
    dest_language: str

    @staticmethod
    def parse(d: list, dest: str) -> "GoogleTranslateResult":
        return GoogleTranslateResult(
            translated_text=" ".join([i for i in d[:-1]]),
            original_language=d[-1],
            dest_language=dest,
        )


@dataclass
class AjaxTranslateResult(Base):
    original_text: str
    translated_text: str
    translation_language: str
    original_language: str

    @staticmethod
    def parse(d: dict, org: str) -> "AjaxTranslateResult":
        return AjaxTranslateResult(
            original_text=d["original_text"],
            translated_text=d["translated_text"],
            translation_language=d["human_translation_details"]["translation_language"],
            original_language=org,
        )


@dataclass
class HozoryTranslateResult(Base):
    translated_text: str
    translation_language: str
    voice_link: str

    @staticmethod
    def parse(d: dict, dest: str) -> "HozoryTranslateResult":
        return HozoryTranslateResult(
            translated_text=d["translate"],
            translation_language=dest,
            voice_link=d["Voice_link"],
        )
