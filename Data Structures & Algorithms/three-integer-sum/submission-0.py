class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # problem: we have an integer array
        # we need to return a list ---> each element are triplets (a list of 3 numbers that add up to 0)

        # implementation: 
        # we need a list to return a bunch of lists 
        # we need 3 pointers within this starting array --> iterate some way where all 3 reach different combinations

        triplets = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i != k and k != j and i != j:
                        if nums[i] + nums[j] + nums[k] == 0:
                            numbers = [nums[i],nums[j],nums[k]]
                            sortedNumbers = sorted(numbers)
                            if sortedNumbers not in triplets:
                                triplets.append(sortedNumbers)
                           
                                
        
        return triplets