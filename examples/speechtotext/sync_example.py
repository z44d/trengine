from trengine.speechtotext import SpeechToTextService

speech = SpeechToTextService()

print(speech.toText('audio.ogg', language='en'))
