class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we are given a string 
        # if it is a palindrome return True, other wise return False

        # implementation: 
        # take the string, remove whitespace, and put into a list
        # have two pointers one in the beginning, one in the end
        # compare values at both pointers and the moment they are dif return false
        # if there is never a dif until the pointers are at the same space then return true

        
        char_list = [char for char in s.lower() if char.isalnum()]
        left, right = 0, len(char_list) - 1
        print(char_list)

        while left < right:
            if char_list[left] != char_list[right]:
                return False

            left = left + 1
            right = right - 1

        return True