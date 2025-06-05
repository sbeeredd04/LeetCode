from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)  # Truncate towards zero
        }        

        for char in tokens:             
            if char not in operators: 
                stack.append(char)
            else:
                if len(stack) >= 2:
                    second = int(stack.pop())
                    first = int(stack.pop())
                    stack.append(operators[char](first, second))
                else:
                    return None
        if len(stack) != 1:
            return None
    
        return stack[-1]
    
# Example usage
if __name__ == "__main__":
    solution = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    result = solution.evalRPN(tokens)
    print(result)  # Output: 9

    tokens = ["4", "13", "5", "/", "+"]
    result = solution.evalRPN(tokens)
    print(result)  # Output: 6

    tokens = ["10", "6", "9", "3", "/", "-11", "*", "+", "*"]
    result = solution.evalRPN(tokens)
    print(result)  # Output: 81