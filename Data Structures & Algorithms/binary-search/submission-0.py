class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # distinct integers --> in a list sorted ascending
        # we are also given a target to find
        # must find the integer in log(n) time

        # implementation: binary search --> check middle number
        # if target > middle ---> search middle ---> end
        # if target < middle ---> search front --> middle


        
        if not nums: # if nums is empty we return -1 beacause an empty list wont have a aarget
            return -1

        
        beg,mid,end = 0, len(nums) // 2, len(nums) - 1


        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
           return self.search(nums[beg:mid], target)
        else:
            res = self.search(nums[mid + 1:], target)
            return mid + 1 + res if res != -1 else -1