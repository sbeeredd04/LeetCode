#INITIAL SOLUTION

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
#         #solving using queue <- 73 <- 74 
#         n = len(temperatures)
#         counts = []

#         #loop through the list once
#         for i in range(0, n) : 

#             curr = temperatures[i]
#             nxt = i+1
#             count = 0

#             #while loop to get the count for the current number while the next number exists
#             while nxt < n: 

#                 #if current >= nxt then add 1 to the count (equal to since equal is not warmer) 
#                 #the case where count is greater than 1 and if end of the list then count = 0 
#                 if curr >= temperatures[nxt] :
                    
#                     count += 1

#                     if count > 0 and nxt == (n-1):
#                         count = 0
                
#                 #else if the the next temperature is warmer add the count and exit the while loop
#                 elif curr < temperatures[nxt]:
#                     count += 1 
#                     break

#                 #add the count for the next iteration
#                 nxt += 1
            
#             #append the count to the counts
#             counts.append(count)
        
#         #return the list
#         return counts
    
from typing import List
    
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        print(f"Input temperatures: {temperatures}")
        print("===" * 20)
        
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        print(f"Initial result list: {res}")
        print(f"Initial stack: {stack}")
        print("===" * 20)
        
        # Iterate through the temperatures
        # Use a stack to keep track of indices of temperatures
        for i, t in enumerate(temperatures):
            
            print(f"Current temperature: {t} at index {i}")
            
            while stack and t > stack[-1][0]:
                print(f"Found warmer temperature: {t} > {stack[-1][0]} at index {i}")
                print(f"Stack before popping: {stack}")
                
                temp, index = stack.pop()
                
                print(f"Popped from stack: ({temp}, {index}) and stack is now {stack}")
                res[index] = i - index
                
                print(f"Updated result for index {index}: {res[index]}")
                
            print(f"Stack before appending: {stack}")
            
            # Append the current temperature and its index to the stack
            print(f"Appending ({t}, {i}) to stack")
            print("===" * 20)

            stack.append((t, i))
            
        print(f"Final result list: {res}")
        print(f"Final stack: {stack}")
        print("===" * 20)
        return res
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]