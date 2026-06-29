class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we are given an integer array of numbers and a number k, expecting 
        # the k most frequent elements returned

        # need to return a list with the k most frequent elements

        # implementaiton: i think i create a dictionary, key is the number and the value is the frequency
        # after all values are updated, we add the k most values into a list and return it

        freq = {}
        result = []

        for num in nums:
            if not freq:
                freq[num] = 1
            else:
                if num in freq:
                    freq[num] = freq[num] + 1
                else:
                    freq[num] = 1

        items = list(freq.items())
        sorted_items = sorted(items, reverse = True, key=lambda item: item[1])
        subset = sorted_items[:k]

        for num, freq in subset:
            result.append(num)

        return result