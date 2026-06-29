class Solution:
    def isValid(self, s: str) -> bool:
        # we are given a list of different brackets and the goal is we need to make sure...
            # every open bracket is closed by the its closed bracket
            # done in the correct orde --> so once we see a closed bracket it should close the bracket to its left, and continue on
            # every type of close bracket has the same type of open bracket

        # implementing a stack
        # we go thru each characer in the list, if it is a open bracket add it to the stack
        # if closed brakcet, then the the last item in the stack must be the corresponding open bracket
        # as we meet open brackets with their corresponding closed brakcets, we should pop out the opne brakcet
        # if they dont match return false
        # if we have a closed bracket and the stack is empty, return false
        # we need a place to store the open brackets with their corresponding closed brackets ---> dictionary, Hashmap

        openBrackets = []
        brackets = {'}':'{',')':'(',']':'['}

        for char in s:
            if char in brackets:
                if openBrackets and openBrackets[-1] == brackets[char]:
                    openBrackets.pop()
                else:
                    return False
                
            else: 
                openBrackets.append(char)
            
        return True if not openBrackets else False

