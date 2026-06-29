class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # problem: we have a list of words
        # we want to return a list of lists of all words that are all anagrams

        # implementation
            # create a dictionary 
                # the key would be the word sorted by letters within, and the key would be the list of each word in that group
                # we iterate thru each word find its signature and see if it matches any keys
                # if it does, append that word to the values of the matching signature
                # if not, then add a new signature and a list append it to that list

        anagrams = {}

        for str in strs:
            newStr = "".join(sorted(str)) 
            if newStr in anagrams:
                anagrams[newStr].append(str)
            else:
                anagrams[newStr] = [str]

        return list(anagrams.values())
                
                

                

                    



            

