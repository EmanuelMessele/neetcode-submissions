class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we have an a list of integers
        # we need to return true if any value appears more than once

        # implementation: we iterate thru the list of integers
        # create a set --> allows no duplicates
        # check if number is already in set, if so return true, if not just add to set
        numbers = set()
        for num in nums:
            if num in numbers:
                return True
            else:
                numbers.add(num)

        return False