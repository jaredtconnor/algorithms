# Given an array of strings, return all the possible permutations
def backtracking_permutations(results, str): 

    # base case - exit once the result length equals all characters
    if(len(results) == len(str)): 
        print(''.join(results))


    for i in range(len(str)): 
        current_choice = str[i]

        # If the permutation was not already made, add it to our result set
        if(current_choice not in results): 
            results.append(current_choice) 

            # recursive call 
            backtracking_permutations(results, str)

            # stopping condition
            results.pop()


def permutations(str):

    results = []
    backtracking_permutations(results, str)

permutations("ABC")





