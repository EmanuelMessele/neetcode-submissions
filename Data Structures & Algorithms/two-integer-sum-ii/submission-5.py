class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we are given a list of integers in increasing order, and a target number to reach
        # we must return index1 and index2 such that index1 < index2, 
        # must return a list ==> [index1, index2]

        # implementation:
        # two pointers index1 at position 0, index2 at end of list
        # add them and see what number we get, if less than target move index1 up
        # if less than target move index2 down, until we have our value
        # make sure index1 is always less than index2

        index1, index2 = 0, len(numbers) - 1

        while index1 < index2:
            if numbers[index1] + numbers[index2] == target:
                print(index1,index2)
                return [index1 + 1, index2 + 1]
            elif numbers[index1] + numbers[index2] < target:
                index1 = index1 + 1
            else:
                index2 = index2 - 1

            