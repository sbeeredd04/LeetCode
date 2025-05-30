# Top K Frequent Elements - Notes

## Problem Understanding
Find the k most frequent elements in an array. Two main approaches exist:

## Approach 1: Tracking Top K with Min Tracking
**Current implementation in `topKFrequentElements.py`**

### Key Issues with Current Implementation:
- **Overly complex** with too many conditions and nested if-else statements
- Uses redundant dictionaries (`topK` and `kmin` store same info)
- **Time Complexity**: O(n * k) due to finding min repeatedly

## Approach 2: Bucket Sort by Frequency ⭐ **RECOMMENDED**
**Cleaner implementation in `topKFrequentElementsAlt.py`**

### Key Concepts to Remember:

#### 1. **Bucket Array Creation**
```python
count = [[] for i in range(len(nums) + 1)]
```
- Index = frequency, Value = list of numbers with that frequency
- **Why `len(nums) + 1`?** Max possible frequency is `len(nums)`

#### 2. **Dictionary Iteration**
```python
for num, freq in d.items():
    count[freq].append(num)
```
- Use `.items()` to get both key and value

#### 3. **Reverse Range Iteration**
```python
for i in range(len(count) - 1, 0, -1):
```
- **Format**: `range(start, stop, step)`
- Goes from `len(count)-1` down to `1` (stops before `0`)

#### 4. **List Extension vs Append**
```python
if count[i]:
    result.extend(count[i])  # Adds all elements from list
    if len(result) >= k:
        return result[:k]    # Return first k elements
```

### **Time Complexity**: O(n) - much better!
### **Space Complexity**: O(n)

## Key Takeaways:
1. **Bucket sort approach is cleaner and more efficient**
2. **Avoid over-engineering** - simpler solutions are often better
3. **Use list comprehension** for creating arrays: `[[] for i in range(n)]`
4. **Remember reverse range syntax**: `range(len-1, 0, -1)`