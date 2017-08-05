import speech_recognition as sr
rec = sr.Recognizer()
with sr.Microphone() as source:
    print("I'm listening!")
    audio = rec.listen(source=source)

    try:
        transcription = rec.recognize_google(audio)
    except sr.UnknownValueError:
        transcription = "Google Speech API is confused"
    except sr.RequestError as e:
        transcription = "Request to Google Speech API failed, request error: ", e
    print(transcription) 
