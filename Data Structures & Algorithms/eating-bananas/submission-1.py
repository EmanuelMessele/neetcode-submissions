class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # you are given a list where each piles[i] shows the number of bananas in piles
        # also given h --> the number of hours to eat all the bananas
        # we need to return the minimum integer k --> the eating rate per hour
        # to eat all the bananas within the h hours

        # implementation:
        # possible answers include 1 --> to the max number of bananas per pile
        # we start in the middle if our final hours is more than h we start with a lower value, if less than h we raise it
        
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid
            
            if hours <= h:
                right = mid
            else:
                left = mid + 1
            
        return left
        