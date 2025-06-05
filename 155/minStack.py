class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val > self.minimum : 
            pass
        else: 
            self.minimum = val

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack:
            self.minimum = float('inf')
        else:
            self.minimum = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
    

#example usage
if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.getMin())  # Returns -3
    min_stack.pop()
    print(min_stack.top())      # Returns 0
    print(min_stack.getMin())   # Returns -2
# Output: