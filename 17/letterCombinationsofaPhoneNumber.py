class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits : 
            return []  
        
        keys = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        
        combinations = []
            
        def backtrack(index, curr) : 

            #if after the last index of the digit append the current index and return
            if index >= len(digits): 
                combinations.append(curr)
                return
            
            letters = keys[int(digits[index])]   #get the current index letters from the keys

            for letter in letters : 
                backtrack(index + 1, curr + letter)     #increment the index and add the current letter
        
        backtrack(0, "")
        
        return combinations
