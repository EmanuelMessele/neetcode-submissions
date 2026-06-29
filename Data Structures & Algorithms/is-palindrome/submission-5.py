class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we have a string S
        # return true if palindrome false if not
        # palindrome === same letter forwards to backeatds to middle

        # turn the string into a list and remove all the whitespace
        # have a pointer at the beginnign and the end
        # check if both letters are the same if so continue on 
        # if not stop and return false
        # using a while loop iterate thru the list 
        # make sure to increment i and j accordingly

        # case insensitive 
        # remember alphanumeric

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

            


        
        
