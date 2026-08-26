class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = []

        for num in nums:
            if num not in numbers:
                numbers.append(num) 
            else:
                return True

        return False
