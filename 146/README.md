# LRU Cache - My Problem Analysis & Learning Journey

## Problem Statement
Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

**Operations Required:**
- `LRUCache(int capacity)` - Initialize with positive size capacity
- `int get(int key)` - Return value of key if exists, otherwise return -1
- `void put(int key, int value)` - Update value if key exists, otherwise add key-value pair

**Requirements:**
- If cache exceeds capacity when adding, remove the **least recently used** key
- Both `get` and `put` must run in **O(1) average time complexity**

## My Journey: From Naive to Optimal Solution

### 1. My Initial Thinking (What Didn't Work)

**My First Thought:**
```python
# This was my initial approach - WRONG!
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}  # Regular dict
        self.cap = capacity
        # But wait... how do I track "least recently used"?
```

**Why This Failed:**
- Regular `dict` in Python doesn't maintain insertion order in older versions
- Even if it did, there's **no way to track the "last recently used"** efficiently
- When I `get` a key, I need to **update its position** to mark it as recently used
- Regular dict can't do `move_to_end()` or track access order

**My Realization:**
> "I need something that combines the O(1) lookup of a hash table with the ability to track and reorder elements based on usage"

### 2. My Discovery: OrderedDict is Perfect!

**My Breakthrough Moment:**
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()  # This changes everything!
        self.cap = capacity
```

**Why OrderedDict Solved Everything:**
- **Maintains insertion order** - first item added is at the beginning
- **O(1) lookup** - still a hash table underneath
- **`move_to_end()` method** - can mark items as recently used in O(1)
- **`popitem(last=False)`** - can remove least recent item in O(1)

### 3. My Final Implementation Analysis

**What I Wrote (WORKING VERSION):**
```python
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Mark as recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # Update existing, mark recent
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)  # Remove oldest
```

### 4. Deep Dive: How My Algorithm Works

**Conceptual Model:**
```
OrderedDict acts like: [oldest] ← ... ← [newest]
- Left side: Least recently used (will be evicted first)
- Right side: Most recently used (safe from eviction)
```

**Example Walkthrough (capacity=2):**
```python
cache = LRUCache(2)

# Step 1: put(1, 1)
cache.put(1, 1)
# OrderedDict: {1: 1}
# State: [1] (1 is most recent)

# Step 2: put(2, 2) 
cache.put(2, 2)
# OrderedDict: {1: 1, 2: 2}
# State: [1, 2] (2 is most recent)

# Step 3: get(1) - This is the KEY operation!
result = cache.get(1)  # Returns 1
# OrderedDict: {2: 2, 1: 1}  # 1 moved to end!
# State: [2, 1] (1 is now most recent)

# Step 4: put(3, 3) - Triggers eviction
cache.put(3, 3)
# Before: {2: 2, 1: 1} → capacity exceeded
# After: {1: 1, 3: 3}   → 2 was evicted (was least recent)
# State: [1, 3] (3 is most recent)
```

### 5. Why My Solution is Mathematically Perfect

**Time Complexity Analysis:**

1. **`get(key)` = O(1):**
   ```python
   if key not in self.cache:        # O(1) hash lookup
       return -1
   self.cache.move_to_end(key)      # O(1) in OrderedDict!
   return self.cache[key]           # O(1) hash lookup
   ```

2. **`put(key, value)` = O(1):**
   ```python
   if key in self.cache:            # O(1) hash lookup
       self.cache.move_to_end(key)  # O(1) in OrderedDict!
   self.cache[key] = value          # O(1) hash assignment
   
   if len(self.cache) > self.cap:   # O(1) length check
       self.cache.popitem(last=False)  # O(1) remove from front!
   ```

**Space Complexity:** O(capacity) - exactly what we need

### 6. The Magic Behind OrderedDict

**What Makes This Work:**
```
OrderedDict internally maintains:
1. Hash table for O(1) key lookups
2. Doubly-linked list for O(1) insertion/deletion at any position
3. Pointers connecting hash table entries to linked list nodes
```

**Visual Representation:**
```
Hash Table:     Doubly-Linked List:
key1 → node1 ←→ [node1] ↔ [node2] ↔ [node3]
key2 → node2        ↑                   ↑
key3 → node3      oldest            newest
```

**My Understanding:**
- `move_to_end(key)` = Find node via hash (O(1)) + Move to end of list (O(1))
- `popitem(last=False)` = Remove first node from list (O(1)) + Update hash table (O(1))

### 7. Edge Cases I Handle Correctly

**Edge Case 1: Updating Existing Key**
```python
cache = LRUCache(2)
cache.put(1, 1)
cache.put(1, 100)  # Updates value, moves to end
# Result: {1: 100} - no capacity violation
```

**Edge Case 2: Getting Non-Existent Key**
```python
result = cache.get(999)  # Returns -1, no state change
```

**Edge Case 3: Capacity 1**
```python
cache = LRUCache(1)
cache.put(1, 1)  # {1: 1}
cache.put(2, 2)  # {2: 2} - 1 evicted immediately
```

**Edge Case 4: Mixed Operations**
```python
cache = LRUCache(2)
cache.put(1, 1)    # {1: 1}
cache.put(2, 2)    # {1: 1, 2: 2}
cache.get(1)       # {2: 2, 1: 1} - 1 moved to end
cache.put(3, 3)    # {1: 1, 3: 3} - 2 evicted (was least recent)
```

### 8. What I Did Exceptionally Well

**✅ My Strengths:**

1. **Recognized the Core Challenge:** I identified that tracking "recently used" order was the main difficulty

2. **Found the Perfect Data Structure:** OrderedDict is literally designed for this exact use case

3. **Efficient State Updates:** Every access correctly updates the usage order

4. **Clean Implementation:** My code is concise yet handles all edge cases

5. **Optimal Complexity:** Achieved true O(1) for both operations

### 9. Alternative Approaches I Could Have Used

**Approach 1: Hash Map + Doubly Linked List (Manual Implementation)**
```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> node
        
        # Dummy head and tail for easier manipulation
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_node(self, node):
        # Add node right after head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def remove_node(self, node):
        # Remove existing node
        prev_node = node.prev
        new_node = node.next
        prev_node.next = new_node
        new_node.prev = prev_node
```

**Why I Chose OrderedDict Instead:**
- **Less Code:** OrderedDict eliminates 50+ lines of linked list management
- **Less Bugs:** No manual pointer manipulation = fewer edge case errors
- **Same Performance:** Both achieve O(1) for get/put operations
- **More Readable:** Intent is clearer with high-level operations

**Approach 2: Hash Map + Move-to-Front List**
```python
# Another manual approach - similar complexity to above
```

**My Decision:** OrderedDict is the perfect abstraction for this problem!

### 10. Common Mistakes I Avoided

**❌ Mistake 1: Using Regular Dict + Timestamps**
```python
# BAD APPROACH
def get(self, key):
    if key in self.cache:
        self.cache[key] = (self.cache[key][0], time.time())  # Update timestamp
        return self.cache[key][0]
    return -1

def put(self, key, value):
    # Need to find minimum timestamp - O(n) operation!
```
**Why This Fails:** Finding LRU item requires O(n) scan of all timestamps

**❌ Mistake 2: Using List for Order Tracking**
```python
# BAD APPROACH  
def __init__(self, capacity):
    self.cache = {}
    self.order = []  # Track key order
    
def get(self, key):
    if key in self.cache:
        self.order.remove(key)    # O(n) operation!
        self.order.append(key)    # Mark as recent
```
**Why This Fails:** `list.remove()` is O(n), violating the O(1) requirement

**❌ Mistake 3: Forgetting to Update Order on `get`**
```python
def get(self, key):
    if key not in self.cache:
        return -1
    # MISSING: self.cache.move_to_end(key)
    return self.cache[key]
```
**Why This Fails:** `get` operations must mark items as recently used!

### 11. Building Intuition for LRU Problems

**🧠 Mental Model I Use:**
> "Think of it like a **stack of books on your desk**. Every time you read a book (get), you put it back on top. Every time you add a new book (put), it goes on top. When your desk is full, the book at the bottom (least recent) falls off."

**Key Insights for Similar Problems:**

1. **LRU = Order Matters:** You need a data structure that tracks **sequence**
2. **Recent = Safe:** Recently accessed items should be protected from eviction  
3. **Update on Access:** Every `get` operation changes the eviction order
4. **Evict From One End:** Always remove from the "least recent" side

**Pattern Recognition:**
- If you see "Least Recently Used" → Think OrderedDict or Manual Doubly-Linked List
- If you need O(1) access + O(1) reordering → OrderedDict is often perfect
- If you're manually managing order → You're probably making it too hard

### 12. Testing My Solution

**Test Cases I Verified:**
```python
# Test Case 1: Basic functionality
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2) 
assert cache.get(1) == 1     # Returns 1, moves 1 to end
cache.put(3, 3)              # Evicts 2 (least recent)
assert cache.get(2) == -1    # 2 was evicted
assert cache.get(3) == 3     # 3 exists
assert cache.get(1) == 1     # 1 still exists

# Test Case 2: Updating existing keys
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.put(1, 10)             # Update 1's value, move to end
cache.put(3, 3)              # Should evict 2, not 1
assert cache.get(2) == -1    # 2 evicted
assert cache.get(1) == 10    # 1 still there with new value

# Test Case 3: Capacity 1 edge case
cache = LRUCache(1)
cache.put(1, 1)
cache.put(2, 2)              # Immediately evicts 1
assert cache.get(1) == -1
assert cache.get(2) == 2
```

### 13. Performance Benchmarking

**My Solution Performance:**
- **Time:** O(1) for both get and put operations
- **Space:** O(min(capacity, total_items)) 
- **Real-world:** Extremely fast due to optimized C implementation of OrderedDict

**Compared to Manual Doubly-Linked List:**
- **Same Big O complexity**
- **Similar real-world performance** 
- **Much shorter and cleaner code**
- **Lower chance of implementation bugs**

### 14. When to Use Each Approach

**Use OrderedDict When:**
- ✅ You want clean, readable code
- ✅ You're in an interview and want to finish quickly
- ✅ You're prototyping or building production systems
- ✅ You trust well-tested library implementations

**Use Manual Doubly-Linked List When:**
- 🔧 Interviewer specifically asks for manual implementation
- 🔧 You want to demonstrate low-level data structure knowledge
- 🔧 You're working in a language without OrderedDict equivalent
- 🔧 You need custom modifications to the basic LRU behavior

### 15. My Key Takeaways & Learning

**What This Problem Taught Me:**

1. **Data Structure Choice is Critical:** The right data structure makes the solution trivial

2. **OrderedDict is Underrated:** Perfect for problems involving order + fast access

3. **Always Consider Libraries:** Don't reinvent the wheel unless specifically required

4. **LRU Pattern Recognition:** Cache problems often boil down to tracking access patterns

5. **O(1) Reordering:** Moving elements to maintain order can be O(1) with the right structure

**My Problem-Solving Framework:**
1. Identify the operations needed (lookup, insert, reorder, delete)
2. Find data structures that support all operations efficiently
3. Prefer proven library solutions over manual implementations
4. Test edge cases thoroughly (capacity limits, duplicate keys, etc.)

### 16. Related Problems to Master

**Similar Cache Problems:**
- LFU Cache (LC 460) - Frequency-based eviction instead of recency
- Design Twitter (LC 355) - Similar to LRU but with following relationships
- Insert Delete GetRandom O(1) (LC 380) - Another O(1) operations problem

**Data Structure Problems Using Similar Patterns:**
- Design Browser History (LC 1472) - Sequential access with current position
- Design Hit Counter (LC 362) - Time-based sliding window

## My Final Solution (Production Ready)

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move to end to mark as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key and mark as recently used
            self.cache.move_to_end(key)
        
        # Set/update the value
        self.cache[key] = value

        # Remove least recently used item if over capacity
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)  # Remove first (oldest) item
```

**My Memory Aid:** 
> "OrderedDict + move_to_end() + popitem(last=False) = Perfect LRU Cache"

**What Made My Implementation Successful:**
1. ✅ Correct identification of OrderedDict as the ideal data structure
2. ✅ Proper use of `move_to_end()` to update access order  
3. ✅ Correct handling of both new and existing keys in `put()`
4. ✅ Efficient eviction with `popitem(last=False)`
5. ✅ Clean, readable, and bug-free implementation

**My Final Reflection:**
This problem perfectly demonstrates that sometimes the best solution is recognizing when NOT to reinvent the wheel. OrderedDict gives me everything I need for an LRU cache - the insight was realizing that "maintaining order while allowing fast access" is exactly what it's designed for!