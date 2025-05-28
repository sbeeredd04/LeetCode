class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grouped = {}

        #iterate through the list of strings
        for s in strs:             
            key = ''.join(sorted(s))
            if key in grouped : 
                grouped[key].append(s)
            else : 
                grouped[key] = [s]
        return list(grouped.values())