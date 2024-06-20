from trengine.speech_to_text import SpeechToText

speech = SpeechToText()

print(speech.to_text("audio.ogg", language="en"))
