import speech_recognition as sr

def audio_to_text(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_sphinx(audio_data)
        return "Text from audio: {}".format(text)
    except sr.UnknownValueError:
        return "PocketSphinx could not understand audio"
    except sr.RequestError as e:
        return "Error with PocketSphinx recognizer; {0}".format(e)

if __name__ == "__main__":
    audio_file_path = "audios/blood_loss_transfusion.wav"
    print(audio_to_text(audio_file_path))
