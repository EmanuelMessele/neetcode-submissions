class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given a list of strings, we want to return a list of sublists
        # where in each sublist we have all the anagrams that are the same

        # create a dictionary that contains sorted verison of words as keys and the list of each 
        # the list of the words as the values
        # combine all the values --> sublists ---> into one list

        result = []
        sort = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if not sort:
                sort[sorted_word] = [word]
            else:
                if sorted_word in sort:
                    sort[sorted_word].append(word)
                else:
                    sort[sorted_word] = [word]
         
        for value in sort.values():
            result.append(value)
        

        return result
