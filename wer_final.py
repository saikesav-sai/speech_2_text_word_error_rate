def wer(ref, hyp):
    # Tokenize the reference and hypothesis texts
    ref_tokens = ref.split()
    hyp_tokens = hyp.split()

    # Initialize dynamic programming table
    dp = [[0] * (len(hyp_tokens) + 1) for _ in range(len(ref_tokens) + 1)]

    # Fill in the DP table
    for i in range(len(ref_tokens) + 1):
        for j in range(len(hyp_tokens) + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                if ref_tokens[i - 1] == hyp_tokens[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1],  # substitution
                                       dp[i - 1][j],      # deletion
                                       dp[i][j - 1])      # insertion

    # Calculate WER
    wer_value = dp[len(ref_tokens)][len(hyp_tokens)] / len(ref_tokens)
    return wer_value

def cer(ref, hyp):
    ref_chars = list(ref)
    hyp_chars = list(hyp)

    # Initialize dynamic programming table
    dp = [[0] * (len(hyp_chars) + 1) for _ in range(len(ref_chars) + 1)]

    # Fill in the DP table
    for i in range(len(ref_chars) + 1):
        for j in range(len(hyp_chars) + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                if ref_chars[i - 1] == hyp_chars[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1],  # substitution
                                       dp[i - 1][j],      # deletion
                                       dp[i][j - 1])      # insertion

    # Calculate CER
    cer_value = dp[len(ref_chars)][len(hyp_chars)] / len(ref_chars)
    return cer_value

# Example usage:
reference_text = "OH HE HAS BEEN AWAY FROM NEW YORK HE HAS BEEN ALL ROUND THE WORLD HE DOESNT KNOW MANY PEOPLE HERE BUT HES VERY SOCIABLE AND HE WANTS TO KNOW EVERY ONE"
hypothesis_text = "OH HE HAS BEEN AWAY FROM NEW YOR HE HAS BEEN ALL ROUND THE WORLD HE DOESN'T BNOMANY PEOPLE HERE BUT HE VERY FAILT OF THE OND HE WANTS TO KNOW EVERYONE"
wer_score = wer(reference_text, hypothesis_text)
cer_score = cer(reference_text, hypothesis_text)
print("Word Error Rate:", wer_score)
print("Character Error Rate:", cer_score)
