import torch
import librosa
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

# Load the model and processor
model_name = "facebook/wav2vec2-base-960h"
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)

# Load and preprocess the audio
audio_input, _ = librosa.load("audios/car_accident_legs_arms.wav", sr=18000, mono=True)  # Replace with the path to your audio file

# Tokenize the audio input
inputs = processor(audio_input, return_tensors="pt", padding="longest", truncation=True, max_length=100000)

# Perform inference
with torch.no_grad():
    logits = model(inputs.input_values).logits

# Decode the logits to obtain the transcription
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)
print("Transcription:", transcription[0])
