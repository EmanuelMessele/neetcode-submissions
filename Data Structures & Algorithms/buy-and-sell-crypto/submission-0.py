class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we are given a list of integers (prices) where prices[i] is the price of 
        # Neetcoin on an ith day
        # choose a single day to buy one Neetcoin and a different day to sell in the future
        # return max profit you can achieve , choose not to make any transactions and return 0



        # implementation
        # left pointer at 0 , and right pointer at 1
        # continuously check if prices[right] > prices[left]
        # if so update profit
        # else change buy pointer to current pointer so it cost lest

        left, right = 0,1
        max_profit = 0

        while right < len(prices):

            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right

            right += 1


        return max_profit