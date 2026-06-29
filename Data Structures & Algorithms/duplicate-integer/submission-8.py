class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # problem: we are given an integer array of nums, if any of the values appear more than once return true, otherwise return false
        # implementation: we can create a set, since a set does not take duplicates we can check if there is as we take in each number, if there is return true, if not return false

        dupes = set()

        for num in nums:
            if num in dupes:
                return True
            else:
                dupes.add(num)

        return False
        