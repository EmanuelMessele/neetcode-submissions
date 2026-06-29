class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we have a list of heights for a possible container
        # the goal is to create the container with the greatest area and return that area
        
        # implementation 
        # have an area variable to keep updating, 
        # double for loops, going thru each height, pick the smallest of the heights and multiply it by the distance between the two values
        # if greater than current area update if not keep going

        area = 0
        height = 0
        width = 0

        for i in range(len(heights)):
            for j in range(len(heights)):
                if i != j:
                    if heights[i] < heights[j]:
                        height = heights[i]
                    elif heights[j] < heights[i]:
                        height = heights[j]
                    else:
                        height = heights[i]


                    width = abs(i - j)


                current_area = height * width
                if current_area > area:
                    area = current_area

        print(height)
        print(width)
        return area
        