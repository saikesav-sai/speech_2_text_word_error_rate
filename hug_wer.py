from evaluate import load
wer = load("wer")
predictions = ["hello world", "good night moon"]
references = ["hello world", "good night moon"]
wer_score = wer.compute(predictions=predictions, references=references)
print(wer_score)