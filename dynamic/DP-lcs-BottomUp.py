# Brute force recursive algrotihm for the Longest Common Subsequence problem
def longest_common_seq_BF(str1, str2): 

    m = len(str1)
    n = len(str2)

    lcs_table = [[None] * (n+1) for i in range(m + 1)]

    for i in range(m+1): 
        for j in range(n+1): 
            if i==0 or j==0: 
                lcs_table[i][j] = 0

            elif str1[i-1] == str2[j-1]: 
                lcs_table[i][j] = lcs_table[i-1][j-1]+1

            else: 
                lcs_table[i][j] = max(lcs_table[i-1][j], lcs_table[i][j-1])

    return lcs_table[m][n]

string_1 = "AGGTAB"
string_2 = "GXTXAYB"

print("Length of LCS is ", longest_common_seq_BF(string_1, string_2))