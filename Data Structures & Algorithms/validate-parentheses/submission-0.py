class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #1. Create an empty stack to store opening brackets
        # Map opening brackets to their closing counterparts
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        #2. Iterate through each character in the string
        for char in s:
            if char in mapping: # Opening bracket
                stack.append(char)
            else: # Closing bracket
                # Stack empty or mismatch
                if not stack:
                    return False
                
                top = stack.pop()
                if mapping[top] != char:
                    return False
        
        # Valid only if all brackets were matched
        return len(stack) == 0