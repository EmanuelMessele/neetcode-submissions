class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we are given a list of numbers and a target to find
        # we need to find it in log(n) time

        # implementation: binary search:
        # we have a left and right pointer, one at 0 and one at the length of the lsit
        # if the middle of these two pointers is less than target, look to only the right of the list
        # vice versa

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

        

        