# Bottom up approach to lcs using dynamic programming
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

    return lcs_optimal_solution(str1, str2, lcs_table)

def lcs_optimal_solution(str1, str2, dp_cache): 

    lcs_solution = []
    m = len(str1)
    n = len(str2)

    while m>0 and n>0: 

        if(str1[m-1] == str2[n-1]): 
            lcs_solution.append(str1[m-1])
            m -= 1 
            n -= 1

        elif(dp_cache[m][n] == dp_cache[m][n-1]): 
            n -= 1 

        else: 
            m -= 1

    return ''.join(reversed(lcs_solution))

print(longest_common_seq_BF("ABCDGH", "AEDFHR"))