# Rotting Oranges - LeetCode 994

## Problem Statement
You are given an `m x n` grid where each cell can have one of three values:
- `0` representing an empty cell
- `1` representing a fresh orange
- `2` representing a rotten orange

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

**Example:**
```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Explanation: 
- Minute 0: [2,1,1] → [2,2,1] → [2,2,2]
- Minute 1: [1,1,0] → [2,1,0] → [2,2,0]
- Minute 2: [0,1,1] → [0,2,1] → [0,2,2]
- Minute 3: [0,2,2] → [0,2,2] (no more fresh oranges)
```

## Initial Approach & Intuition

> **"This is a level-order traversal problem where all rotten oranges affect their neighbors simultaneously. I initially tried DFS but realized it couldn't handle multiple rotten oranges properly. BFS is perfect because each level represents one minute, and all rotten oranges at the same level affect their neighbors at the same time. The key insight is using a queue to process all rotten oranges level by level, ensuring accurate time calculation."**

## Initial Hunch and Hints

<details>
<summary>My First Thoughts</summary>

When I first saw this problem, my immediate thought was:
> "This is similar to flood fill, but I need to track time and handle multiple rotten oranges. I can use DFS to explore from each rotten orange and calculate the maximum time needed."

My initial approach was:
1. **Use DFS to explore from each rotten orange** - similar to flood fill problems
2. **Track time with recursive calls** - increment time for each level of recursion
3. **Handle multiple rotten oranges** - process each rotten orange independently
4. **Calculate maximum time** - find the longest time needed to rot all oranges

The key challenge was realizing that DFS couldn't handle the simultaneous nature of the problem correctly.
</details>

<details>
<summary>Key Insights That Helped</summary>

- **Level-by-level processing**: Each BFS level represents one minute
- **Simultaneous effects**: All rotten oranges affect neighbors at the same time
- **Queue-based approach**: Process all rotten oranges at current level before moving to next
- **Fresh orange tracking**: Count fresh oranges and decrement as they rot
- **Boundary checking**: Always verify coordinates before accessing grid
- **Time increment**: Add one minute after processing all oranges at current level
</details>

<details>
<summary>⚠ Common Pitfalls I Avoided</summary>

- **Using DFS for simultaneous effects**: DFS processes each rotten orange independently
- **Complex time calculation**: Recursive time tracking was error-prone
- **Not tracking fresh oranges**: Need to count and decrement fresh oranges
- **Missing boundary checks**: Always verify grid bounds before accessing
- **Incorrect level processing**: Must process all oranges at current level together
- **Wrong termination condition**: Check if fresh oranges remain after processing
</details>

## My Solution Analysis

### What I Implemented:

**BFS Solution (Correct Approach):**
```python
def orangesRotting(self, grid: List[List[int]]) -> int:
    q = collections.deque()
    fresh = 0
    time = 0

    # Step 1: Count fresh oranges and collect rotten oranges
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append((r, c))

    # Step 2: BFS level by level
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while fresh > 0 and q:
        length = len(q)  # Process all oranges at current level
        for i in range(length):
            r, c = q.popleft()

            # Check all 4 directions
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(len(grid))
                    and col in range(len(grid[0]))
                    and grid[row][col] == 1
                ):
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
        time += 1  # One minute has passed
    
    return time if fresh == 0 else -1
```

### Key Design Decisions:

**1. BFS vs DFS Approach**
- **Initial**: Tried DFS with recursive time tracking
- **Final**: Used BFS with level-by-level processing
- **Benefit**: Natural handling of simultaneous effects

**2. Level-by-Level Processing**
```python
length = len(q)  # Capture all rotten oranges at current level
for i in range(length):
    r, c = q.popleft()
    # Process this rotten orange
time += 1  # Increment time after processing all at current level
```

**3. Fresh Orange Tracking**
```python
fresh = 0  # Count initially
# ... count fresh oranges ...
fresh -= 1  # Decrement when orange becomes rotten
return time if fresh == 0 else -1  # Check if any remain
```

**4. Boundary and State Checking**
```python
if (row in range(len(grid))
    and col in range(len(grid[0]))
    and grid[row][col] == 1
):
```
Check bounds and ensure we only process fresh oranges.

## Algorithm Analysis with Debugging

Let me trace through the BFS algorithm with detailed debugging:

### Debug Execution Trace:

**Input Grid:**
```
[2,1,1]
[1,1,0]
[0,1,1]
```

**Step-by-step execution:**

**Initialization:**
```
- Fresh oranges: 6 (positions: (0,1), (0,2), (1,0), (1,1), (2,1), (2,2))
- Rotten oranges: 1 (position: (0,0))
- Queue: [(0,0)]
- Time: 0
```

**Minute 0:**
```
Process all rotten oranges at level 0:
- Pop (0,0)
  - Check (0,1): grid[0][1] = 1 → rot it → grid[0][1] = 2, fresh = 5
  - Check (0,-1): out of bounds
  - Check (1,0): grid[1][0] = 1 → rot it → grid[1][0] = 2, fresh = 4
  - Check (-1,0): out of bounds
- Queue: [(0,1), (1,0)]
- Time: 1
```

**Minute 1:**
```
Process all rotten oranges at level 1:
- Pop (0,1)
  - Check (0,2): grid[0][2] = 1 → rot it → grid[0][2] = 2, fresh = 3
  - Check (0,0): grid[0][0] = 2 (already rotten)
  - Check (1,1): grid[1][1] = 1 → rot it → grid[1][1] = 2, fresh = 2
  - Check (-1,1): out of bounds
- Pop (1,0)
  - Check (1,1): grid[1][1] = 2 (already rotten)
  - Check (1,-1): out of bounds
  - Check (2,0): grid[2][0] = 0 (empty)
  - Check (0,0): grid[0][0] = 2 (already rotten)
- Queue: [(0,2), (1,1)]
- Time: 2
```

**Minute 2:**
```
Process all rotten oranges at level 2:
- Pop (0,2)
  - Check (0,3): out of bounds
  - Check (0,1): grid[0][1] = 2 (already rotten)
  - Check (1,2): grid[1][2] = 0 (empty)
  - Check (-1,2): out of bounds
- Pop (1,1)
  - Check (1,2): grid[1][2] = 0 (empty)
  - Check (1,0): grid[1][0] = 2 (already rotten)
  - Check (2,1): grid[2][1] = 1 → rot it → grid[2][1] = 2, fresh = 1
  - Check (0,1): grid[0][1] = 2 (already rotten)
- Queue: [(2,1)]
- Time: 3
```

**Minute 3:**
```
Process all rotten oranges at level 3:
- Pop (2,1)
  - Check (2,2): grid[2][2] = 1 → rot it → grid[2][2] = 2, fresh = 0
  - Check (2,0): grid[2][0] = 0 (empty)
  - Check (3,1): out of bounds
  - Check (1,1): grid[1][1] = 2 (already rotten)
- Queue: [(2,2)]
- Time: 4
```

**Minute 4:**
```
Process all rotten oranges at level 4:
- Pop (2,2)
  - All neighbors are either out of bounds, empty, or already rotten
- Queue: [] (empty)
- Fresh: 0
- Return: 4
```

**Final Result: 4 minutes**

## Algorithm Flow Diagram

Based on the debug execution trace, here's the detailed algorithm flow:

```mermaid
flowchart TD
    A[Start: grid] --> B[Initialize: q = deque, fresh = 0, time = 0]
    B --> C[Count fresh oranges and collect rotten oranges]
    C --> D[Queue empty?]
    D -->|Yes| E[Return -1 if fresh > 0, else time]
    D -->|No| F[length = len(q)]
    F --> G[Process all oranges at current level]
    G --> H[Pop rotten orange from queue]
    H --> I[Check all 4 directions]
    I --> J{Valid fresh orange?}
    J -->|Yes| K[Rot the orange: grid[row][col] = 2]
    K --> L[Add to queue: q.append((row, col))]
    L --> M[Decrement fresh: fresh -= 1]
    M --> N{More directions?}
    N -->|Yes| I
    N -->|No| O{More oranges at current level?}
    O -->|Yes| H
    O -->|No| P[Increment time: time += 1]
    P --> Q{fresh > 0 and queue not empty?}
    Q -->|Yes| F
    Q -->|No| E
    
    style E fill:#90EE90
    style P fill:#FFB6C1
```

### Key Execution Points:
- **Initialization**: Count fresh oranges and collect all rotten oranges
- **Level processing**: Process all rotten oranges at current level before moving to next
- **Time tracking**: Increment time after processing each level
- **State management**: Track fresh oranges and update grid in-place
- **Termination**: Stop when no fresh oranges remain or queue is empty

## Self-Reflection: What I Did and Learned

### ▲ What I Did Well

**1. Recognized the Pattern Eventually**
I initially tried DFS but quickly realized it couldn't handle the simultaneous nature of the problem. My switch to BFS was the right decision.

**2. Implemented Level-by-Level Processing Correctly**
The key insight was using `length = len(q)` to capture all rotten oranges at the current level and processing them together before incrementing time.

**3. Used Proper State Tracking**
I correctly tracked:
- Fresh orange count (decrement as they rot)
- Time increment (after processing each level)
- Grid state (mark oranges as rotten in-place)

**4. Handled Edge Cases Properly**
I made sure to:
- Check grid boundaries before accessing
- Only process fresh oranges (value 1)
- Handle empty queue and remaining fresh oranges
- Return -1 when impossible to rot all oranges

**5. Used Queue-Based BFS**
The deque approach was perfect for:
- Level-by-level processing
- Simultaneous effect simulation
- Accurate time calculation

### ▼ What I Struggled With

**1. Initial DFS Approach**
My first attempt used DFS which:
- Processed each rotten orange independently
- Made time calculation complex and error-prone
- Couldn't handle simultaneous effects properly

**2. Understanding Simultaneous Effects**
I initially struggled with:
- How to process multiple rotten oranges at the same time
- When to increment time
- How to avoid double-counting effects

**3. Level-by-Level Processing**
I had to think carefully about:
- How to capture all rotten oranges at current level
- When to move to the next time step
- How to ensure all effects happen simultaneously

### ■ Problem-Solving Process That Worked

**Step 1: Understand the Problem**
- "Find minimum time for all oranges to rot"
- "Multiple rotten oranges affect neighbors simultaneously"
- "Need level-by-level processing to track time accurately"

**Step 2: Design the Algorithm**
- "Use BFS for level-by-level processing"
- "Track fresh oranges and decrement as they rot"
- "Increment time after processing each level"

**Step 3: Optimize the Approach**
- "Use queue to process all rotten oranges at current level"
- "Check boundaries and only process fresh oranges"
- "Return -1 if any fresh oranges remain"

### ► What I'd Do Differently Next Time

**1. Start with BFS from the Beginning**
I should have recognized this as a level-order traversal problem immediately instead of trying DFS first.

**2. Consider Alternative Approaches**
I could have explored:
- Multi-source BFS for better performance
- Union-Find for very large grids
- Early termination optimizations

**3. Add More Debug Output**
The debug version was really helpful - I should add debugging capabilities to understand the level-by-level flow better.

**4. Consider Performance Optimization**
For very large grids, I might want to consider:
- Early termination if no fresh oranges remain
- Parallel processing for very large grids
- Memory optimization for sparse grids

### ◆ Key Insights I'll Remember

**1. Level-by-Level Processing Pattern**
```python
length = len(q)  # Capture current level
for i in range(length):
    # Process all oranges at current level
time += 1  # Increment after processing level
```

**2. Simultaneous Effects Require BFS**
```python
# BFS (correct) - processes all at same level
while q:
    length = len(q)
    for i in range(length):
        # Process all rotten oranges simultaneously

# DFS (incorrect) - processes independently
def dfs(r, c):
    # Each rotten orange processed separately
```

**3. Fresh Orange Tracking**
```python
fresh = 0  # Count initially
# ... count fresh oranges ...
fresh -= 1  # Decrement when rotting
return time if fresh == 0 else -1
```

**4. Boundary and State Checking**
```python
if (row in range(len(grid))
    and col in range(len(grid[0]))
    and grid[row][col] == 1
):
```
Always check bounds and ensure valid state transitions.

### ▲ How This Problem Helped Me Grow

**Algorithm Selection:** I'm getting better at choosing BFS vs DFS based on problem requirements  
**Simultaneous Processing:** I understand level-by-level processing better  
**State Management:** I'm more comfortable tracking multiple states (fresh count, time, grid)  
**Problem Recognition:** I can identify "minimum time" + "simultaneous effects" = BFS  

### ★ What I'm Proud Of

My BFS solution is clean, efficient, and correctly handles the simultaneous nature of the problem! I particularly like:
- The level-by-level processing approach
- The accurate time tracking
- The proper state management
- The clear and readable structure

The key insight about using BFS for simultaneous effects was really satisfying - it made the problem much simpler and more accurate.

### ➤ Next Steps for Improvement

1. **Practice more BFS problems** to reinforce level-by-level processing
2. **Learn about multi-source BFS** for problems with multiple starting points
3. **Explore BFS vs DFS trade-offs** for different problem constraints
4. **Practice simultaneous effect problems** with different data structures
5. **Study graph algorithms** like flood fill, connected components, and time-based simulations

This problem was really satisfying to solve correctly! The key insight about using BFS for simultaneous effects is a powerful pattern that applies to many time-based simulation problems.

---

**Time Complexity:** O(m × n) where m and n are the dimensions of the grid  
**Space Complexity:** O(m × n) in worst case due to queue storage  
**Pattern:** Level-by-Level BFS for Simultaneous Effects with Time Tracking
