class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we are given an array and if there is a duplicate return true, if not return false

        # implement, we can create a set, and for each number, check to see if it is in set
        # if not, add it in the set, if so return true


        numbers = set()

        for num in nums:
            if num in numbers:
                return True
            else:
                numbers.add(num)

        return False
        

        