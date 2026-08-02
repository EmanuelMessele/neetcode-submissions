class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two Pointer Approach
        #
        # Start with the two lines that are the farthest apart.
        # This gives us the maximum possible width.
        #
        # The area is determined by:
        #   min(left height, right height) * width
        #
        # After calculating the area:
        # - Move the pointer with the SMALLER height.
        # - Why?
        #   Because the shorter line is limiting the area.
        #   Moving the taller line only decreases the width
        #   while keeping the limiting height the same or smaller.
        #   The only chance to get a larger area is to find
        #   a taller shorter line.

        left = 0
        right = len(heights) - 1

        max_area = 0

        while left < right:

            # Current container dimensions
            height = min(heights[left], heights[right])
            width = right - left

            # Calculate area
            current_area = height * width

            # Update maximum area found
            max_area = max(max_area, current_area)

            # Move the shorter line inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area
        
        