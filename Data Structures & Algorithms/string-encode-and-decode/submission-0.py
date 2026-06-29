class Solution:

    def encode(self, strs: List[str]) -> str:
        # given a list of strings, connect all the strings into a single string
        
        # we go thru each word in the list 
        # we gets its length, removes ambiguity for when we have to decode
        # we add a special character after the number to know when that number stops

        string = ""

        for word in strs:
            string += str(len(word)) + "#" + word
        
        return string


    def decode(self, s: str) -> List[str]:
        # now with decode, we are given a string and must return a list of all the words in that strng
        # with our decoding, we now have a number and a # to disconnect our words

        # so we iterate through each character
        # save the number before the #, that will be our length, we will know to read this much for our word
        # save the word and append it to the list, --> create a list

        words = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
        
            length = int(s[i:j])

            word = s[j + 1: j + 1 + length]
            words.append(word)

            i = j + 1 + length
        return words

        







