class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # we are given two strings and we need to compare them together to see if they are anagrams
        # if they are anagrams return true, if not reutn false

        # implement
        # we can plit the strings into lists of characters and sort them
        # check them for equality and return our boolean based on this equality

        # code
        isAnagram = False 

        sortedS = sorted(s)
        sortedT = sorted(t)

        if(sortedS == sortedT):
            isAnagram = True

        return isAnagram