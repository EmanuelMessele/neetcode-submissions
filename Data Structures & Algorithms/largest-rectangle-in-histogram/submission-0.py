class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # we are given a list of heights where each element in the list are heights of a bar --> each width is size 1
        # we want to return the area of the largest rectangle
        # area is length * width


        # implementation:
      
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start,h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea