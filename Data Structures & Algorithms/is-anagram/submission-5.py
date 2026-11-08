class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we are given 2 strings
        # objective: return true if both strings are anagrams
        # anagram --> same amount of same characters

        # implementation
        # turn string into a list
        # then we sort list by character
        # then we go thru both lists checking for differences, if there is one return false
        # if we go thru both lists and no differeces, return true

        list1 = list(s)
        list2 = list(t)

        list1.sort()
        list2.sort()

        if len(list1) != len(list2):
            return False
        
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False

        return True
