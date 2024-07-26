def calculate_cer(reference, hypothesis):
    """
    Calculate Character Error Rate (CER) between reference and hypothesis strings.
    CER is the percentage of characters that are incorrect in the hypothesis compared to the reference.
    """
    reference = reference.lower()
    hypothesis = hypothesis.lower()

    # Create a matrix to store the distances between substrings
    dp = [[0] * (len(hypothesis) + 1) for _ in range(len(reference) + 1)]

    for i in range(len(reference) + 1):
        for j in range(len(hypothesis) + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif reference[i - 1] == hypothesis[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],      # Insert
                                  dp[i - 1][j],      # Remove
                                  dp[i - 1][j - 1])  # Replace

    # Calculate CER as the normalized edit distance
    cer = dp[len(reference)][len(hypothesis)] / len(reference)
    return cer


if __name__ == "__main__":
    # Example usage
    reference_text = "hello world"
    hypothesis_text = "hola world"

    cer = calculate_cer(reference_text, hypothesis_text)
    print(f"Character Error Rate (CER): {cer:.2%}")
