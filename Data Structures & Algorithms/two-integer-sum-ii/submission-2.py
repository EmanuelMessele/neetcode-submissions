class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we are given a list of numbers and a target, non decreasing
        # we need to find the two numbers that add up to the target 

        # implementation
        # one pointer at the begining, one pointer at the end
        # add the values, if less bring the pointer at the end back
        # if more bring the pointer at the beginning forward
        # return a list of the indexes

        i,j = 0, len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1 , j + 1]
            elif numbers[i] + numbers[j] < target:
                i = i + 1
            else:
                j = j - 1

        

        