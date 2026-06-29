class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # we are given 2 strings, we want to know if they are both anagrams of each other, 
        # meaning they have the exact same number of each character

        # implement: since an anagram means both strings must have the same number of characters, if we sort the strings and compare them that should return true or false for us

        # code:
            return sorted(s) == sorted(t)