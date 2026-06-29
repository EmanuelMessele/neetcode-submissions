class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # understand the problem 
        # we are given an array of numbers, we need to return true if there is a duplicate in the list

        # implement solution

        # declare some variable that holds our value, true or false, we wll return this later
        isDup = False
       
        # create a dictionary to hold each letter; key, and its occurence: value
        numDictionary = {}

        # iterate through the list and add into dictionary 
        for num in nums:
            numDictionary[num] = numDictionary.get(num, 0) + 1

        # finally go thru the dictionaries values and if there is a value greater than 1, return true
        for key, value in numDictionary.items():
            if value != 1:
                isDup = True
        
        return isDup

        