class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # we are given a list of strings
        # we must go through this list of strings and group all the strings that are anagrams together in sublists 
        # we must finally return a list of sublists with matching anagrams in each sublist

        # implement
        # we can create a dictionary that stores the sorted version of the words found in the list
        # going thru each word in the list, we can sort it and see if it is in the dictionary, if so add it to the list in the values part of the dictionary
        # if not, create a new key and add it to the values there
        # finally return the values of the dictionary

        anagrams = {}

        for str in strs:
            key = ''.join(sorted(str))
            if key in anagrams:
               anagrams[key].append(str)
            else:
                anagrams[key] = [str]
            
        values = anagrams.values()

        return list(values)