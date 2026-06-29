class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # keeping score for a baseball 
        # given a list of operations number, + , D, C, change your result list 
        # add up all the numbers in the list and return the final value

        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False

        scores = []
        finalScore = 0
        i = 0

        for x in operations:
            print(x)
            if is_number(x):
                scores.append(int(x))
            else:
                # match(x):
                #     case "+":
                #         scores[-1] = scores[-1] + scores[-2]
                #         break
                #     case "D":
                #         scores[-1] = 2 * scores[-1]
                #         break
                #     case "C":
                #         scores.remove(scores[-1])
                #         break
                if x == "+":
                    value = scores[-1] + scores[-2]
                    scores.append(value)
                elif x == "D":
                    value = 2 * scores[-1]
                    scores.append(value)
                else:
                    scores.remove(scores[-1])


            print(scores)

      
        
        for num in scores:
            finalScore += num


        return finalScore

