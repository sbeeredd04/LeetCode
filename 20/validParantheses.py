class Solution:
    def isValid(self, s: str) -> bool:
        
        #list to acting as a stack to store
        stack = []
        i = 0
        ob = {')':'(', ']':'[', '}':'{'}

        while i < len(s): 
            if s[i] in ob.values(): 
                stack.append(s[i])
            else:
                if stack and stack[-1] == ob[s[i]]:
                    stack.pop()
                else: 
                    return False
            i += 1

        return True if not stack else False