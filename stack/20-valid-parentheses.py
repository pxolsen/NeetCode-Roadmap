# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s: str) -> bool:
    stack = []
    for bracket in s:
        if bracket == "(" or bracket == "[" or bracket == "{":
            stack.insert(0,bracket)
        elif bracket == ")":
            if not stack or stack[0] != "(":
                return False
            stack.pop(0)
        elif bracket == "]":
            if not stack or stack[0] != "[":
                return False
            stack.pop(0)
        elif bracket == "}":
            if not stack or stack[0] != "{":
                return False
            stack.pop(0)
    return not stack
       
        

print(isValid("()")) # True
print(isValid("()[]{}")) # True
print(isValid("(]")) # False