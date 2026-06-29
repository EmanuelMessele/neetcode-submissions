class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # problem: given an array ---> if there is a value within the array that is a duplicate return true
        # other wise return false

        # implementation: create a set to store numbers in the set and a variable, sets cant have duplicates  --->
        # --> iterate thru the array and add into the set
        # if that number is already in the set, then return true, if not keep adding to set 
        # finally return that variabel

        numbers = set()
        hasDup = False
        
        for num in nums:
            if num in numbers:
                hasDup = True
            else:
                numbers.add(num)

        return hasDup