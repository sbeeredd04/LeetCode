from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        #convert the string into a list of integers
        digits = [int(d) for d in digits]
        
        #create a dictionary to map the digits to letters
        digit_to_letters = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        
        #create a list to store the combinations
        combinations = []
        
        #using backtracking to find the combinations
        def backtrack(index: int, current_combination: str):
            #if the current combination is of the same length as the digits then add it to the list
            if index == len(digits):
                combinations.append(current_combination)
                return
            
            #get the letters for the current digit
            letters = digit_to_letters[digits[index]]
            
            #loop through the letters and call backtrack for each letter
            for letter in letters:
                backtrack(index + 1, current_combination + letter)
                
        #if the digits are empty then return an empty list
        if not digits:
            return []
        
        #call backtrack for the first digit
        backtrack(0, "")
        return combinations
    

# Example usage
if __name__ == "__main__":
    sol = Solution()
    digits = "23"
    print(sol.letterCombinations(digits))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    
    digits = ""
    print(sol.letterCombinations(digits))  # Output: []
    
    digits = "2"
    print(sol.letterCombinations(digits))  # Output: ["a","b","c"]