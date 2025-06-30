# Find the Duplicate Number - Problem 287

## My Self-Reflection

This was initially a really easy problem that I could solve with basic approaches, but the constraint of solving it in **constant extra space** made me think deeper about the solution.

## The Challenge
The main constraint was that I needed to:
- Use O(1) extra space
- Not modify the array by sorting or changing positions
- Still find the duplicate efficiently

## My Approach Discovery
I came across this clever approach where since I can only manipulate the given array without changing the actual values or their positions (no sorting or major algorithms), the only thing I could do was **change the sign of the values** in the array.

## How My Solution Works
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums : 
            if nums[abs(num)] < 0 :
                return abs(num)
            else : 
                nums[abs(num)] *= -1
        
        return None
```

## What I Did and What Happened

1. **I used the array indices as a marking system**: Since the numbers are in range [1, n], I could use each number as an index to mark visited positions.

2. **I flipped signs to mark visits**: For each number, I used its absolute value as an index and made the value at that index negative to mark it as "visited".

3. **I detected the duplicate**: When I encountered a number whose corresponding index already had a negative value, I knew this number had been seen before - that's my duplicate!

## Key Insights I Gained
- **Creative use of existing space**: Instead of using extra data structures, I repurposed the array itself as a marking mechanism
- **Sign manipulation**: Using negative signs as flags was a clever way to track state without additional memory
- **Index-value relationship**: The constraint that numbers are in range [1, n] was crucial - it allowed me to safely use values as indices

## What Worked Well
- O(1) space complexity achieved ✅
- O(n) time complexity - efficient ✅
- Simple logic once I understood the concept ✅

## Reflection
This problem taught me to think outside the box when faced with space constraints. Sometimes the most elegant solutions come from creatively using what you already have rather than adding more complexity. The sign-flipping technique is a powerful pattern I can apply to similar problems in the future.               