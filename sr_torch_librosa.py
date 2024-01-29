import torch
import librosa
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

def audio_to_text(audio_file):
    model_name = "facebook/wav2vec2-base-960h"
    processor = Wav2Vec2Processor.from_pretrained(model_name)
    model = Wav2Vec2ForCTC.from_pretrained(model_name)

    audio_input, _ = librosa.load(audio_file, sr=18000, mono=True)

    inputs = processor(audio_input, return_tensors="pt", padding="longest", truncation=True, max_length=100000)

    with torch.no_grad():
        logits = model(inputs.input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)
    text = "Transcription:" + transcription[0]
    return text

if __name__ == "__main__":
    audio_file_path = "audios/blood_loss_transfusion.wav"
    print(audio_to_text(audio_file_path))