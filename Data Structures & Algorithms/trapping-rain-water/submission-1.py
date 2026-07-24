class Solution:
    def trap(self, height: List[int]) -> int:
        # given a list of heights representing elevation bars
        # we want to see how much maximum amount of rain water

        # implementation
        # there can only be water if there is elevation in between empty spaces
        # we can read the list until we see a 0, if there are two numbers between it, then we 
        # multiply the smaller of the two elevations by the difference in length

        # at every point, we try to find the largest elvation to the left, and the next largest elevation to the right
        # then we do min(leftmax,rightmax) - current length

        current = 1
        water = 0

        while current < len(height) - 1:
            # find left max
            leftMax = max(height[:current])

            # find right
            rightMax = max(height[current+1:])

            currentWater = min(rightMax,leftMax) - height[current]
            
            if currentWater > 0:
                water = water + currentWater

            # update current
            current = current + 1







        return water    