class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)   # default 0 handles "no warmer day" for free
        stack = []  # indices of days still waiting for a warmer temp

        for i, temp in enumerate(temperatures):
            # today's temp resolves every waiting day that's colder than it
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                result[j] = i - j          # days waited
            stack.append(i)                # today now waits for its own warmer day

        return result