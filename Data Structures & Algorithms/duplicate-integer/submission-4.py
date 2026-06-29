class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we are given an array: nums
        # going thru the array return true if any value appears more than once
        
        # implement
        # i think we should make another list, as we iterate thru the given array, we check if the value is
        # already in our made array, if it is just return true, if not, add it into our list

        numbers = []

        for num in nums:
            if num in numbers:
                return True
            else:
                numbers.append(num)

        return False
        