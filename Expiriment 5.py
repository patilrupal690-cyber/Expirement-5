def find_lcs(first_sequence, second_sequence):
    first_length = len(first_sequence)
    second_length = len(second_sequence)

    dp_table = [[0] * (second_length + 1)
                for _ in range(first_length + 1)]

    for first_index in range(1, first_length + 1):
        for second_index in range(1, second_length + 1):

            if first_sequence[first_index - 1] == second_sequence[second_index - 1]:
                dp_table[first_index][second_index] = (
                    dp_table[first_index - 1][second_index - 1] + 1
                )
            else:
                dp_table[first_index][second_index] = max(
                    dp_table[first_index - 1][second_index],
                    dp_table[first_index][second_index - 1]
                )

    first_index = first_length
    second_index = second_length
    common_subsequence = ""

    while first_index > 0 and second_index > 0:

        if first_sequence[first_index - 1] == second_sequence[second_index - 1]:
            common_subsequence += first_sequence[first_index - 1]
            first_index -= 1
            second_index -= 1

        elif dp_table[first_index - 1][second_index] > dp_table[first_index][second_index - 1]:
            first_index -= 1

        else:
            second_index -= 1

    common_subsequence = common_subsequence[::-1]

    return dp_table[first_length][second_length], common_subsequence


first_sequence = input("Enter first sequence: ")
second_sequence = input("Enter second sequence: ")

lcs_length, lcs_result = find_lcs(first_sequence, second_sequence)

print(f"\nLength of Longest Common Subsequence:{lcs_length}")
print(f"Longest Common Subsequence: {lcs_result}")