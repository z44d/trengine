from trengine.text_to_speech import TextToSpeech

text = TextToSpeech()

print(text.to_speech("Hello, how are you doing today?", "audio.mp3", "en"))

