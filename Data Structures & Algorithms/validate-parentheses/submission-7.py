class Solution:
    def isValid(self, s: str) -> bool:
        # we are given a string of these characters: '(', ')', '{', '}', '[' and ']'.
        # need to make sure a string is valid:
            ## Every open bracket is closed by the same type of close bracket.
            # Open brackets are closed in the correct order.
            #Every close bracket has a corresponding open bracket of the same type.
        
        # implemenation
        # have a lsit of opening and closing brackets
        # if our char is an oopening put in stack
        # if not pop out of stack and make sure they equal each other
        # if not rerturn false
        # else return true

        # Maps each closing bracket to its matching opening bracket
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for char in s:

            # If it's an opening bracket, push it onto the stack
            if char in "([{":
                stack.append(char)

            # Otherwise it's a closing bracket
            else:

                # If there's nothing to match with, it's invalid
                if not stack:
                    return False

                # Get the most recent opening bracket
                top = stack.pop()

                # Check if it matches the current closing bracket
                if top != pairs[char]:
                    return False

        # If there are still opening brackets left, it's invalid
        return len(stack) == 0
