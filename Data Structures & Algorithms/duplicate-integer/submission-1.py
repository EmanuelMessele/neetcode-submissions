class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        isDup = False
        numDictionary = {}

        for num in nums:
            numDictionary[num] = numDictionary.get(num,0) + 1
        
        for key, value in numDictionary.items():
            if value != 1:
                isDup = True


        return isDup

        