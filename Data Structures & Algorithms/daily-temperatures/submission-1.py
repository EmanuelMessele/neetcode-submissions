class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we are given a list of temperatures where temperature[i] is the temperature
        # on an ith day. 
        # we need to return a list that returns the how many days it takes to get
        # to a warmer day
        # if there isnt a warmer day then result[i] == 0

        # implementation
        # we go thru each temperature in the list
        # for each temp after our given temp, we put the next temps into a stack as long as they are colder
        # once we reach a warmer temp, we put the length of our temp stack in for result[i]

        # result = []
        # for i in range(len(temperatures) - 1):
        #     stack = []
        #     print(0, temperatures[i])
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] < temperatures[i]:
        #             stack.append(temperatures[j])
        #         elif temperatures[j] > temperatures[i]:
        #             result.append(len(stack) + 1)
        #             stack.clear()
        #             print(result)
        #             break
                
        #         if len(stack) == 0:
        #             result.append(0)

        # return result

        # this was my og answer


        # with ai, i see now, what my issue is 
        result = [0] * len(temperatures)   # default 0 handles "no warmer day" for free
        stack = []  # indices of days still waiting for a warmer temp

        for i, temp in enumerate(temperatures):
            # today's temp resolves every waiting day that's colder than it
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                result[j] = i - j          # days waited
            stack.append(i)                # today now waits for its own warmer day

        return result

