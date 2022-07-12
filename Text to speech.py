import pyttsx3

engine = pyttsx3.init()

SpeechRate = engine.getProperty('rate')
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')

for CurrentVoices in enumerate(voices):
    print(CurrentVoices[0], CurrentVoices[1])

engine.setProperty('rate', 200)
engine.setProperty('voices', voices[3].id)
engine.setProperty('volume', volume-0.10)

answer = "Hello world i just said something"
engine.say(answer)
engine.runAndWait()