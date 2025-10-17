from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        #initialize a counter for all characters in p
        counter = Counter(p)

        #lenght of substring
        length = len(p)

        #final result
        res = []

        # find the difference in the counter between all the substrings in the string
        for i in range(0, len(s)-length+1): 

            #initliaze the counter for substring
            substring = s[i:i+length]
            subCounter = Counter(substring)

            #differencce between counter and subcounter -> should be zero
            difference = subCounter - counter

            #if the list is empty both sets are equal then add the index
            if len(list(difference.elements())) == 0: 
                res.append(i)

        return res
