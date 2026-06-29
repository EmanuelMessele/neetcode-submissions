class Solution:
    def isValid(self, s: str) -> bool:
        # problem: we have a string s
        # in the string, there are characters { [ ( ) ] }
        # every open bracket is closed by that same closed bracket in the correct order, and every closed bracket by the corresponding open bracket

        # implementation:
        # we traverse the list, if open bracket then add to stack --> if closed stack pop out from stack for correct open bracket
        # if incorrect bracket return false, if empty stack return false
        # if at end of traversal , the stack is not empty return false

        brackets = list(s)
        stack = []
        openBrackets = ['{', '[', '(']

        for bracket in brackets:
            if bracket in openBrackets:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                else:
                    poppedBracket = stack.pop()
                    if bracket == ']' and poppedBracket != '[':
                        return False

                    if bracket == '}' and poppedBracket != '{':
                        return False

                    if bracket == ')' and poppedBracket != '(':
                        return False

        if stack:
            return False
        else:
            return True
        