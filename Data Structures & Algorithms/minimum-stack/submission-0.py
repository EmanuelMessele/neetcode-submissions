class MinStack:
    # to help us get the minimum of the stack, we create 2 stacks one for our numbers and one for the current minimum

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val) # after we push ---> we want to compare the value we just pushed to the current least number in the min stack --> if minstack is even non empty
        
        if self.minStack:
            if self.minStack[-1] < val:
                val = self.minStack[-1]
            
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
