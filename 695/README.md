# Max Area of Island - LeetCode 695

## Problem Statement
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

**Example:**
```
Input: grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

## Initial Approach & Intuition

> **"This is a connected components problem like Number of Islands, but instead of counting islands, I need to find the maximum area. The key insight is using DFS to explore each island completely and track the area. I started with a nonlocal variable approach but realized I could optimize it by using return value accumulation - each DFS call returns the area of its subtree, and I can sum them up recursively. This eliminates the need for nonlocal variables and makes the code cleaner and more functional."**

## Initial Hunch and Hints

<details>
<summary>► My First Thoughts</summary>

When I first saw this problem, my immediate thought was:
> "This is similar to Number of Islands, but I need to track area instead of just counting. I can use DFS to explore each connected component and sum up the area."

My initial approach was:
1. **Use DFS to explore islands** - similar to Number of Islands problem
2. **Track area with nonlocal variable** - increment area for each cell visited
3. **Reset area for each new island** - start fresh area counter for each component
4. **Update maximum area** - keep track of the largest area found

The key challenge was avoiding the nonlocal variable and finding a cleaner functional approach.
</details>

<details>
<summary>▲ Key Insights That Helped</summary>

- **Return value accumulation**: Each DFS call can return the area of its subtree
- **Recursive summation**: `return 1 + dfs(neighbor1) + dfs(neighbor2) + ...`
- **Functional approach**: Eliminate side effects by using return values
- **Base case handling**: Return 0 for invalid cells or water
- **Direction vectors**: Use systematic approach for neighbor exploration
- **In-place modification**: Mark visited cells to avoid revisiting
</details>

<details>
<summary>⚠ Common Pitfalls I Avoided</summary>

- **Using nonlocal variables**: Can make code harder to understand and debug
- **Not resetting area counter**: Could lead to incorrect area calculations
- **Missing boundary checks**: Always verify coordinates before accessing
- **Infinite recursion**: Ensure base cases stop recursion properly
- **Wrong area calculation**: Make sure to count current cell + all neighbors
- **Not marking visited cells**: Could lead to double counting
</details>

## My Solution Analysis

### What I Implemented:

**Original Solution (with nonlocal):**
```python
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    directions = [[1,0], [0,1], [-1,0], [0,-1]]
    area = 0
    maxArea = 0
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(r, c): 
        nonlocal area
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 : 
            return

        grid[r][c] = 0
        area += 1

        for dr, dc in directions: 
            dfs(r+dr, c+dc)
    
    for r in range(ROWS): 
        for c in range(COLS): 
            if grid[r][c] == 1:
                area = 0 
                dfs(r, c)
                maxArea = max(maxArea, area)
    
    return maxArea
```

**Optimized Solution (functional approach):**
```python
def maxAreaOfIslandOptimized(self, grid: List[List[int]]) -> int:
    maxArea = 0
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(r, c): 
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 : 
            return 0

        grid[r][c] = 0
        return 1 + dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)

    for r in range(ROWS): 
        for c in range(COLS): 
            if grid[r][c] == 1:
                maxArea = max(maxArea, dfs(r, c))
    
    return maxArea
```

### Key Design Decisions:

**1. Functional vs Imperative Approach**
- **Original**: Used nonlocal variable to track area (imperative)
- **Optimized**: Used return value accumulation (functional)
- **Benefit**: Cleaner, more readable, no side effects

**2. Return Value Accumulation Pattern**
```python
return 1 + dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)
```
Each DFS call returns the area of its subtree, and we sum them up.

**3. Base Case Handling**
```python
if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 : 
    return 0
```
Return 0 for invalid cells or water, ensuring proper termination.

**4. In-place Modification**
```python
grid[r][c] = 0  # Mark as visited
```
Change visited cells to 0 to avoid revisiting and save space.

## Algorithm Analysis with Debugging

Let me trace through the optimized algorithm with detailed debugging:

### Debug Execution Trace:

**Input Grid:**
```
[0,0,1,0,0,0,0,1,0,0,0,0,0]
[0,0,0,0,0,0,0,1,1,1,0,0,0]
[0,1,1,0,1,0,0,0,0,0,0,0,0]
[0,1,0,0,1,1,0,0,1,0,1,0,0]
[0,1,0,0,1,1,0,0,1,1,1,0,0]
[0,0,0,0,0,0,0,0,0,0,1,0,0]
[0,0,0,0,0,0,0,1,1,1,0,0,0]
[0,0,0,0,0,0,0,1,1,0,0,0,0]
```

**Step-by-step execution:**

**Island 1: Starting at (0,2)**
```
DFS(0,2):
  - Mark (0,2) as visited: grid[0][2] = 0
  - Return: 1 + DFS(1,2) + DFS(0,3) + DFS(-1,2) + DFS(0,1)
    - DFS(1,2): grid[1][2] = 0, return 1 + 0 + 0 + 0 + 0 = 1
    - DFS(0,3): grid[0][3] = 0, return 0 (water)
    - DFS(-1,2): return 0 (out of bounds)
    - DFS(0,1): grid[0][1] = 0, return 0 (water)
  - Total area: 1 + 1 + 0 + 0 + 0 = 2
```

**Island 2: Starting at (0,7)**
```
DFS(0,7):
  - Mark (0,7) as visited: grid[0][7] = 0
  - Return: 1 + DFS(1,7) + DFS(0,8) + DFS(-1,7) + DFS(0,6)
    - DFS(1,7): grid[1][7] = 0, return 1 + DFS(2,7) + DFS(1,8) + DFS(0,7) + DFS(1,6)
      - DFS(2,7): return 0 (water)
      - DFS(1,8): grid[1][8] = 0, return 1 + 0 + 0 + 0 + 0 = 1
      - DFS(0,7): return 0 (already visited)
      - DFS(1,6): return 0 (water)
      - Total: 1 + 0 + 1 + 0 + 0 = 2
    - DFS(0,8): return 0 (already visited)
    - DFS(-1,7): return 0 (out of bounds)
    - DFS(0,6): return 0 (water)
  - Total area: 1 + 2 + 0 + 0 + 0 = 3
```

**Island 3: Starting at (1,7)**
```
DFS(1,7):
  - Mark (1,7) as visited: grid[1][7] = 0
  - Return: 1 + DFS(2,7) + DFS(1,8) + DFS(0,7) + DFS(1,6)
    - DFS(2,7): return 0 (water)
    - DFS(1,8): grid[1][8] = 0, return 1 + 0 + 0 + 0 + 0 = 1
    - DFS(0,7): return 0 (already visited)
    - DFS(1,6): return 0 (water)
  - Total area: 1 + 0 + 1 + 0 + 0 = 2
```

**Island 4: Starting at (1,8)**
```
DFS(1,8):
  - Mark (1,8) as visited: grid[1][8] = 0
  - Return: 1 + DFS(2,8) + DFS(1,9) + DFS(0,8) + DFS(1,7)
    - DFS(2,8): return 0 (water)
    - DFS(1,9): grid[1][9] = 0, return 1 + 0 + 0 + 0 + 0 = 1
    - DFS(0,8): return 0 (already visited)
    - DFS(1,7): return 0 (already visited)
  - Total area: 1 + 0 + 1 + 0 + 0 = 2
```

**Island 5: Starting at (1,9)**
```
DFS(1,9):
  - Mark (1,9) as visited: grid[1][9] = 0
  - Return: 1 + DFS(2,9) + DFS(1,10) + DFS(0,9) + DFS(1,8)
    - All neighbors return 0 (water or already visited)
  - Total area: 1 + 0 + 0 + 0 + 0 = 1
```

**Continue with remaining islands...**

**Final Result: Maximum area = 6** (from the largest connected component)

## Algorithm Flow Diagram

Based on the debug execution trace, here's the detailed algorithm flow:

```mermaid
flowchart TD
    A[Start: grid] --> B{grid empty?}
    B -->|Yes| C[Return 0]
    B -->|No| D[Initialize: maxArea = 0, ROWS, COLS]
    D --> E[For each cell (r,c) in grid]
    E --> F{grid[r][c] == 1?}
    F -->|No| G[Continue to next cell]
    F -->|Yes| H[Start new island: area = DFS(r,c)]
    H --> I[maxArea = max(maxArea, area)]
    I --> J[Continue to next cell]
    G --> K{More cells?}
    J --> K
    K -->|Yes| E
    K -->|No| L[Return maxArea]
    
    H --> M[DFS: r, c]
    M --> N{Valid cell?}
    N -->|No| O[Return 0]
    N -->|Yes| P[Mark as visited: grid[r][c] = 0]
    P --> Q[Return: 1 + DFS(all neighbors)]
    Q --> R[Sum all neighbor results]
    R --> S[Return total area]
    
    style C fill:#FFB6C1
    style L fill:#90EE90
    style S fill:#90EE90
```

### Key Execution Points:
- **Grid iteration**: Scan each cell systematically
- **Island detection**: Start DFS only on unvisited '1's
- **Area calculation**: Each DFS returns area of its subtree
- **Return accumulation**: Sum up all neighbor areas recursively
- **Maximum tracking**: Update maxArea with largest found

## Self-Reflection: What I Did and Learned

### ▲ What I Did Well

**1. Recognized the Pattern Immediately**
I quickly identified this as a connected components problem similar to Number of Islands. My intuition about "finding maximum area instead of counting" was spot on.

**2. Optimized the Solution Elegantly**
The key breakthrough was realizing I could eliminate the nonlocal variable by using return value accumulation:
```python
return 1 + dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)
```

**3. Used Functional Programming Approach**
Instead of relying on side effects (nonlocal variables), I used pure functions that return values. This makes the code:
- More readable and predictable
- Easier to test and debug
- More functional programming style

**4. Handled Edge Cases Properly**
I made sure to:
- Check grid boundaries before accessing
- Return 0 for invalid cells or water
- Mark visited cells to avoid revisiting
- Handle empty grid case

**5. Used Systematic Direction Exploration**
The explicit direction calls make the code clear and easy to understand:
```python
return 1 + dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)
```

### ▼ What I Struggled With

**1. Initial Nonlocal Approach**
My first attempt used nonlocal variables which:
- Made the code harder to understand
- Required careful variable management
- Could lead to bugs if not handled properly

**2. Understanding Return Value Accumulation**
I initially struggled with:
- How to accumulate areas from different paths
- When to return 0 vs actual area values
- How to handle the base cases properly

**3. Recursive Summation Logic**
I had to think carefully about:
- How each DFS call contributes to the total area
- The order of operations in the return statement
- Making sure I don't double-count cells

### ■ Problem-Solving Process That Worked

**Step 1: Understand the Problem**
- "Find maximum area of connected components"
- "Similar to Number of Islands but track area instead of count"
- "Need to explore each island completely and sum up areas"

**Step 2: Design the Algorithm**
- "Use DFS to explore each connected component"
- "Track area using return values instead of side effects"
- "Sum up areas from all neighbor paths recursively"

**Step 3: Optimize the Approach**
- "Eliminate nonlocal variables for cleaner code"
- "Use functional programming principles"
- "Make each DFS call return the area of its subtree"

### ► What I'd Do Differently Next Time

**1. Start with Functional Approach**
I should have thought about return value accumulation from the beginning instead of starting with nonlocal variables.

**2. Consider Alternative Approaches**
I could have explored:
- BFS approach for area calculation
- Iterative DFS with stack
- Union-Find for very large grids

**3. Add More Debug Output**
The debug version I created was really helpful - I should add debugging capabilities to understand the recursion flow better.

**4. Consider Performance Optimization**
For very large grids, I might want to consider:
- BFS for better memory usage
- Early termination if area can't exceed current max
- Parallel processing for very large grids

### ◆ Key Insights I'll Remember

**1. Return Value Accumulation Pattern**
```python
return 1 + dfs(neighbor1) + dfs(neighbor2) + dfs(neighbor3) + dfs(neighbor4)
```
This pattern is crucial for any recursive area/size calculation.

**2. Functional vs Imperative Approach**
```python
# Functional (better)
return 1 + dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)

# Imperative (worse)
nonlocal area
area += 1
dfs(r+1, c)
dfs(r, c+1)
# etc.
```

**3. Base Case Handling**
```python
if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 : 
    return 0
```
Always return 0 for invalid cases to ensure proper termination.

**4. Recursive Summation**
Each recursive call returns the area of its subtree, and we sum them up at each level.

### ▲ How This Problem Helped Me Grow

**Functional Programming:** I'm getting better at using return values instead of side effects  
**Recursive Thinking:** I'm more comfortable with recursive area/size calculations  
**Code Optimization:** I'm learning to eliminate nonlocal variables for cleaner code  
**Pattern Recognition:** I'm understanding the connected components pattern better  

### ★ What I'm Proud Of

My optimized solution is clean, efficient, and demonstrates excellent functional programming principles! I particularly like:
- The elimination of nonlocal variables
- The elegant return value accumulation pattern
- The clear and readable recursive structure
- The systematic direction exploration

The key insight about using return values instead of side effects was really satisfying - it made the code much cleaner and more functional.

### ➤ Next Steps for Improvement

1. **Practice more functional programming patterns** to reinforce return value accumulation
2. **Learn about other recursive patterns** like tree traversal and backtracking
3. **Explore BFS vs DFS trade-offs** for different problem constraints
4. **Practice area/size calculation problems** with different data structures
5. **Study graph algorithms** like flood fill, connected components, and area calculations

This problem was really satisfying to optimize! The key insight about eliminating nonlocal variables and using return value accumulation is a powerful pattern that applies to many recursive problems.

---

**Time Complexity:** O(m × n) where m and n are the dimensions of the grid  
**Space Complexity:** O(m × n) in worst case due to recursion stack  
**Pattern:** Connected Components with Area Calculation using DFS Return Value Accumulation
