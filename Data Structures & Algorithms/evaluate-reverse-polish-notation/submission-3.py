class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # given an array of strings, tokens representing a valid arithmetic expression
        # in Reverse Polish Notation: operators follow the operands
        # we need to return the answer of the expression

        # implementation:
        # we have some answer start at 0, a stack to contain our numbers because we will want to go back
        # to our numbers once we reach an operation. 

      
        stack = []

        for token in tokens:
            print(token)
            if token in ("+", "-", "*", "/"):
                b = stack.pop()
                a = stack.pop()

                print(a,b)
                
                match token:
                    case "+": stack.append(a + b)
                    case "-": stack.append(a - b)
                    case "*": stack.append(a * b)
                    case "/": stack.append(int(a / b))  # truncates toward zero
            else:
                stack.append(int(token))
            
        return stack[0]

        # using ai i found my mistake was that I should be putting the answer back into the stack and from there
        # keep popping 

            
                



