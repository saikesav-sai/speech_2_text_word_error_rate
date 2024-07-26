import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import soundfile as sf
from scipy.io import wavfile
import numpy as np
from scipy.signal import wiener
import librosa
#From here we are applying Weiner filter
input_file = "61-70968-0000.wav"
sample_rate, audio_data = wavfile.read(input_file)
# Normalize the audio data to the range [-1, 1]
audio_data = audio_data.astype(np.float32) / np.max(np.abs(audio_data))
# Apply Wiener filter for denoising
denoised_audio = wiener(audio_data)
output_file = "4den_4_1000.wav"
# Convert the denoised audio data back to integer format
denoised_audio = (denoised_audio * np.iinfo(np.int16).max).astype(np.int16)
# Save the denoised audio to a new file
wavfile.write(output_file, sample_rate, denoised_audio)
#tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
#model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

model = Wav2Vec2ForCTC.from_pretrained("../models/word_vec")
tokenizer = Wav2Vec2Tokenizer.from_pretrained("../models/word_vec/tokenizer")



file_name = '4den_4_1000.wav'
data = wavfile.read(file_name)
framerate = data[0]
sounddata = data[1]
time = np.arange(0,len(sounddata))/framerate
input_audio, _ = librosa.load(file_name, sr=16000)
input_values = tokenizer(input_audio, return_tensors="pt").input_values
logits = model(input_values).logits
predicted_ids = torch.argmax(logits, dim=-1)
transcript = tokenizer.batch_decode(predicted_ids)[0]
print(transcript)
    