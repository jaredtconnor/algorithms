
# Test input:
A = [2, 3, 4, 4, 7, 11, 11, 11, 13]

# RETURNS: The numver of valid entries after deletion


def sorted_array_remove_dups(A: list[int]) -> int:

    if not A:
        return 0

    write_index = 1

    for i in range(1, len(A)):

        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1

    return write_index


result = sorted_array_remove_dups(A)
print(result)
