# Brute force recursive algrotihm for the Longest Common Subsequence problem
def longest_common_seq_BF(str1, str2): 
    return longest_common_seq_BF_helper(str1, str2, len(str1)-1, len(str2)-1)

def longest_common_seq_BF_helper(str1, str2, i, j):
    if i < 0 or j < 0: 
        return 0 

    elif str1[i] == str2[j]: 
        return 1 + longest_common_seq_BF_helper(str1, str2, i-1, j-1)

    else: 
        return max(longest_common_seq_BF_helper(str1, str2, i-1, j), longest_common_seq_BF_helper(str1, str2, i, j-1))


print(longest_common_seq_BF("abcde", "ac"))