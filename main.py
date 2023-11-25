import speech_recognition
import pyttsx3

import pyaudio

recognizer = speech_recognition.Recognizer()

while True:

    try : 
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio= recognizer.listen(mic, timeout=10)

            text= recognizer.recognize_sphinx(audio_data=audio)
            text = text.lower()

            print(f"Recognized {text}")
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
        recognizer = speech_recognition.Recognizer()
        continue
    except speech_recognition.RequestError as e:
        print(f"Could not request results from service; {e}")
    except speech_recognition.WaitTimeoutError:
        print("Listening timed out. Please try again.")
