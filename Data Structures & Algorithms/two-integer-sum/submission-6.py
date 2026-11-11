class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we are given a list of integers and a target integer
        # we need to return the indices of the list when indexed and added together give us the target

        # implementation: we have two pointers on both ends of the list 
        # start off by adding both for a sum, then we check to see if that sum is less than greater than or equal to our target, 
        # if its less than move left index up one, if greater than, move right index down, if equal too return both indices
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

      