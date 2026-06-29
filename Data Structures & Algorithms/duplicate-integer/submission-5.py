class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we are given an array and if there is a duplicate return true, if not return false

        # implement, we can create a set, and for each number, check to see if it is in set
        # if not, add it in the set, if so return true

        listNums = set()
        hasDup = False

        for num in nums:
            if num in listNums:
                hasDup = True
            if num not in listNums:
                listNums.add(num)

        return hasDup

        