import Levenshtein

# Replace these with the actual transcriptions
reference_transcription = "the quick brown fox jumps over the lazy dog"
original_transcription = "the quik brown fox jumps over the lazy dog"
noisy_transcription = "the qwik brwn fox jumps over lazy dog"

# Compute the Word Error Rate (WER) for the original audio
original_wer = Levenshtein.distance(reference_transcription.split(), original_transcription.split()) / len(reference_transcription.split())

# Compute the WER for the noisy audio
noisy_wer = Levenshtein.distance(reference_transcription.split(), noisy_transcription.split()) / len(reference_transcription.split())

print(f"Original WER: {original_wer:.2%}")
print(f"Noisy WER: {noisy_wer:.2%}")
