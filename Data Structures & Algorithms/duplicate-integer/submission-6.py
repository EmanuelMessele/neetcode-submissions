class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # problem: we have a list of nums ---> if a number appears in the list twice retrun true

        # implementation: 
        # create a set ---> cant contain duplicates
        # iterate thru numbers and check if they are in the set
        # if a number in our list is already in the set return true
        # if not add in the set and keep iterating, if we finish our list of nums return false

        hasDups = False
        dups = set()
        
        for num in nums:
            if num in dups:
               hasDups = True
            else:
                dups.add(num)
        
        return hasDups