class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we are given an int array: nums
        # we need to return an array that for each element in the array
        # the index of that element, is = to every value in the given array with the exception of the element in given arrays index

        # i think we can do a double for loop but we use indexing instead of for each 
        # then we can use i 
        result = [0] * len(nums)


        for i in range(0, len(nums)):
            answer = 1
            for j in range(0, len(nums)):
                if j != i:
                    answer = answer * nums[j]

            result[i] = answer
        
        return result
                