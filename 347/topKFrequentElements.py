from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #keep track of top k and the min of top k
        topK = {}
        kmin = {}
        d = {}

        for num in nums: 
            print(f"Processing number: {num}")
            if num in d : 
                print(f"Number {num} already in frequency dictionary with count {d[num]}")
                d[num] += 1
                print(f"Updated frequency of {num} to {d[num]}")

                if num in topK:
                    print(f"Number {num} is already in topK with count {topK[num]}")
                    topK[num] = d[num]
                    if num in kmin:
                        print(f"Number {num} is already in kmin with count {kmin[num]}")
                        kmin[num] = d[num]
                else :
                    print(f"Number {num} is not in topK, adding it")
                    if len(topK) < k:
                        print(f"TopK has less than {k} elements, adding {num} to topK")
                        topK[num] = d[num]
                        kmin[num] = d[num]
                        print(f"TopK now: {topK}")
                        
                    else : 
                        
                        print(f"TopK has {k} elements, checking if {num} should replace the min")
                        #find the min in topk
                        minKey = min(kmin, key=kmin.get)
                        if d[num] > kmin[minKey]:
                            print(f"Number {num} has a higher frequency than the current min {minKey} with count {kmin[minKey]}")
                            del topK[minKey]
                            del kmin[minKey]
                            print(f"Removed {minKey} from topK and kmin")
                            topK[num] = d[num]
                            kmin[num] = d[num]
                            print(f"Added {num} to topK and kmin")
                            
            else :
                print(f"Number {num} is not in frequency dictionary, adding it")
                d[num] = 1
                print(f"Frequency of {num} set to 1")
                
                if len(topK) < k:
                    print(f"TopK has less than {k} elements, adding {num} to topK")
                    topK[num] = d[num]
                    kmin[num] = d[num]
                    print(f"TopK now: {topK}")
                    
                else : 
                    print(f"TopK has {k} elements, checking if {num} should replace the min")
                    #find the min in topk
                    minKey = min(kmin, key=kmin.get)
                    if d[num] > kmin[minKey]:
                        print(f"Number {num} has a higher frequency than the current min {minKey} with count {kmin[minKey]}")
                        del topK[minKey]
                        del kmin[minKey]
                        print(f"Removed {minKey} from topK and kmin")
                        topK[num] = d[num]
                        kmin[num] = d[num]
                        print(f"Added {num} to topK and kmin")
                        
        print(f"Final frequency dictionary: {d}")
        print(f"Final topK before returning: {topK}")
        #return the keys of topK
        print(f"Final topK: {topK}")
        return list(topK.keys())
    
if __name__ == "__main__":  
    # Example usage
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(solution.topKFrequent(nums, k))  # Output: [1, 2]

    nums = [1]
    k = 1
    print(solution.topKFrequent(nums, k))  # Output: [1]

    nums = [1, 2]
    k = 2
    print(solution.topKFrequent(nums, k))  # Output: [1, 2] or [2, 1] depending on order
    nums = [1, 2, 3, 4, 5]
    k = 3
    print(solution.topKFrequent(nums, k))  # Output: [1, 2, 3] or any combination of 3 numbers
    nums = [1, 1, 2, 2, 3, 3, 4, 4]
    k = 2
    print(solution.topKFrequent(nums, k))  # Output: [1, 2] or [3, 4] depending on order
    nums = [5, 5, 5, 6, 6, 7, 8]
    k = 2