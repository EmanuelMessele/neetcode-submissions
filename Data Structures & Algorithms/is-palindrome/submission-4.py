class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we are given a string
        # we must return true if it is a palindrome meaning the string reads the same forwards and backwards

        # we can have a pointer pointing to the beginning of the string and one at the end
        # from here we can iterate the pointers up or down until we reach the middle or left passes right
            # check if the letters match, if they dont return false

       
        lowerS = s.lower()
        left, right = 0, len(lowerS) - 1
        while left < right:
            while left < right and not lowerS[left].isalnum():
                left += 1
            
            while left < right and not lowerS[right].isalnum():
                right -= 1

            if lowerS[left] != lowerS[right]:
                return False

            left += 1
            right -= 1

        return True