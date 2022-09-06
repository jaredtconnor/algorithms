
class Solution:
    def isValid(self, s: str) -> bool:  

        # Create our stack datastructure 
        stack = [] 
        valid_starts = ['{', '[','(']

        # Loop through each character in the string 
        for c in s:  

            # If the string is a starting element, add to our stack 
            if c in valid_starts: 
                stack.append(c)
            
            # Else if the character is a right element and the left element is one before it, remove from stack as valid 
            elif c == ')' and stack[-1] == '(' and len(stack) != 0: 
                stack.pop()

            elif c == ']' and stack[-1] == '[' and len(stack) != 0: 
                stack.pop()

            elif c == '}' and stack[-1] == '{' and len(stack) != 0: 
                stack.pop()
        
            # Else, the character is invalid and return false
            else: 
                return False


        # Lastly, make sure the stack is empty
        return stack == []

solution = Solution()

# Test cases: 
s_1 = "()"   
s_2 = "(){}[]" 
s_3 = "(]"

print(f"Result for '{s_1}': {solution.isValid(s_1)} | Should be True")
print(f"Result for '{s_2}': {solution.isValid(s_2)} | Should be True")
print(f"Result for '{s_3}': {solution.isValid(s_3)} | Should be False")

