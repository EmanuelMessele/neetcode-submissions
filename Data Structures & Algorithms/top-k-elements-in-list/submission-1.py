class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we are given a integer arryay nums and an integer k which tells us how many elements we need to search for 
        # we must return the k most frequent elements from our array and return it as an array

        # implement: creating a dictionary to store each number--> key, frequency --> value
        # from here we can find which values have the highest value and return the k highest value elements

        freqs = {}
        answer = []

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        items = list(freqs.items())
        sortedItems = sorted(items, key= lambda x: x[1], reverse = True) # remeber sorted vs sort

        for i in range(k):
            answer.append(sortedItems[i][0])

        return answer