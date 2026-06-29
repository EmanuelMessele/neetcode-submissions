class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # problem: we have a list of numbers and a target to reach , we then want to return the indices that
        # add up to that target

        # implementation idea: i think the only way to do this is to loop for each number in a two for loop manner

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    if  i != j:
                        return[i,j]
                
            
        
    

        