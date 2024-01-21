import speech_recognition as sr

def audio_to_text(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_sphinx(audio_data)
        print("Text from audio: {}".format(text))
    except sr.UnknownValueError:
        print("PocketSphinx could not understand audio")
    except sr.RequestError as e:
        print("Error with PocketSphinx recognizer; {0}".format(e))

if __name__ == "__main__":
    audio_file_path = "audios/blood_loss_transfusion.wav"
    audio_to_text(audio_file_path)
