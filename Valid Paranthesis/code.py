class Solution:
    def isValid(self, s: str) -> bool:
# initializing stack and paranthesis
        stack = [] 
        paranthesis = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for char in s:
            if char in paranthesis.values(): # if char  is a open bracket, add it to stack
                stack.append(char)
            else:
                if not stack or (stack[-1] != paranthesis[char]): #otherwise check the last item of stack matches the correct closing bracket
                    return False
                else:
                    stack.pop() # If the matching is correct, pop it from the stack
        if not stack: # finally stack should be an empty list
            return True
        else:
            return False # otherwise return false
