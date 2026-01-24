# [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

## Problem Statement
You are given an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates where rain water can flow from that cell to **both** the Pacific and Atlantic oceans.

**Example:**
```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Visualization:
    Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Cells marked with () can flow to both oceans.
```

## Initial Approach & Intuition

> **"My initial brute force idea was actually right - check if water from each cell can flow to both oceans! But I looked at the hints and discovered the brilliant reverse intuition: instead of checking where water can flow TO from each cell, check what cells can reach Pacific and Atlantic FROM the ocean boundaries. Then find the intersection! The key insight is reversing the flow direction - water flows from higher to lower, so we reverse and check which cells can be reached from ocean edges following increasing or equal heights."**

## Initial Hunch and Hints

<details>
<summary>► My First Thoughts</summary>

When I first saw this problem, my immediate thought was:
> "I need to check from every cell if water can flow to both oceans. This sounds like running DFS from each cell to see if it reaches both boundaries!"

My initial brute force approach was:
1. **For each cell in the grid** - iterate through all cells
2. **Run DFS to check Pacific reachability** - can water flow to top or left edge?
3. **Run DFS to check Atlantic reachability** - can water flow to bottom or right edge?
4. **If both reachable** - add cell to result

The problem with this approach:
- Running DFS from every cell is **extremely inefficient** - O(m*n * m*n) time
- Lots of redundant work as we explore same paths multiple times
- I knew there had to be a better way!

After looking at hints, the **reverse insight** clicked:
> "Instead of asking 'Where can this cell flow TO?', ask 'What cells can REACH the ocean?'"
</details>

<details>
<summary>▲ Key Insights That Helped</summary>

- **Reverse the flow direction**: Instead of flowing downhill, think about reaching uphill from oceans
- **Two separate DFS runs**: Find all cells reachable from Pacific, then from Atlantic
- **Intersection is the answer**: Cells that can reach both oceans are in both sets
- **Start from ocean boundaries**: Pacific (top + left edges), Atlantic (bottom + right edges)
- **Flow condition reversal**: Original: `next_height <= current_height` (flow down). Reversed: `next_height >= prev_height` (reach up)
- **Use sets for visited tracking**: Efficient lookup and intersection operation
</details>

<details>
<summary>⚠ Common Pitfalls I Avoided</summary>

- **Brute force from every cell**: Would be O(m²*n²) - too slow!
- **Forgetting to handle edges properly**: Pacific is top+left, Atlantic is bottom+right
- **Wrong flow direction**: In reverse approach, water flows from lower to higher or equal
- **Not using sets for intersection**: Sets make finding common cells efficient
- **Revisiting cells**: Must track visited cells to avoid infinite loops
- **Off-by-one errors**: Boundary conditions need careful handling
</details>

## My Solution Analysis

### What I Implemented:

**Reverse DFS Approach (Optimal):**
```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prevHeight): 
            # Reverse: check if current height is LESS than previous (can't reach uphill)
            if ((r,c) in visit or 
                r < 0 or c < 0 or r == ROWS or c == COLS or 
                heights[r][c] < prevHeight): 
                return
            
            visit.add((r,c))
            # Explore all 4 directions with current height as new prevHeight
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        # Start from Pacific boundaries (top row and left column)
        for c in range(COLS): 
            dfs(0, c, pac, heights[0][c])          # Top row → Pacific
            dfs(ROWS-1, c, atl, heights[ROWS-1][c]) # Bottom row → Atlantic
        
        # Start from Pacific/Atlantic boundaries (left column and right column)
        for r in range(ROWS): 
            dfs(r, 0, pac, heights[r][0])          # Left column → Pacific
            dfs(r, COLS-1, atl, heights[r][COLS-1]) # Right column → Atlantic
        
        # Find intersection: cells reachable from both oceans
        res = []
        for r in range(ROWS): 
            for c in range(COLS): 
                if (r,c) in pac and (r,c) in atl: 
                    res.append([r,c])
        
        return res
```

### Key Design Decisions:

**1. Reverse Flow Intuition**
- **Normal flow**: Water flows from high → low (≥ to ≤)
- **Reverse flow**: Check what can reach ocean from low → high (≤ to ≥)
- **DFS condition**: `heights[r][c] >= prevHeight` (can climb up or stay same)

**2. Two Separate DFS Traversals**
```python
pac = set()  # Cells that can reach Pacific
atl = set()  # Cells that can reach Atlantic

# Run DFS from all Pacific boundary cells
for c in range(COLS):
    dfs(0, c, pac, heights[0][c])  # Top edge
for r in range(ROWS):
    dfs(r, 0, pac, heights[r][0])  # Left edge

# Run DFS from all Atlantic boundary cells  
for c in range(COLS):
    dfs(ROWS-1, c, atl, heights[ROWS-1][c])  # Bottom edge
for r in range(ROWS):
    dfs(r, COLS-1, atl, heights[r][COLS-1])  # Right edge
```

**3. Efficient Intersection Finding**
```python
# Find cells present in both sets
for r in range(ROWS):
    for c in range(COLS):
        if (r,c) in pac and (r,c) in atl:
            res.append([r,c])
```

**4. Boundary Checks in DFS**
```python
# Stop conditions:
if ((r,c) in visit or              # Already visited
    r < 0 or c < 0 or              # Out of bounds (left/top)
    r == ROWS or c == COLS or      # Out of bounds (right/bottom)
    heights[r][c] < prevHeight):   # Can't flow uphill
    return
```

## Algorithm Walkthrough

### Example: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

**Step 1: Pacific DFS from boundaries**

Starting from top row (Pacific boundary):
```
(0,0): height=1 → DFS explores: (0,1), (1,0)
(0,1): height=2 → DFS explores: (0,2), (1,1)
(0,2): height=2 → DFS explores: (0,3), (1,2)
(0,3): height=3 → DFS explores: (0,4), (1,3)
(0,4): height=5 → DFS explores: (1,4)
```

Starting from left column (Pacific boundary):
```
Continue from cells not yet visited...
```

**Pacific reachable set (pac):**
```
{(0,0), (0,1), (0,2), (0,3), (0,4),
 (1,0), (1,1), (1,2), (1,3), (1,4),
 (2,0), (2,1), (2,2),
 (3,0), (3,1),
 (4,0)}
```

**Step 2: Atlantic DFS from boundaries**

Starting from bottom row and right column...

**Atlantic reachable set (atl):**
```
{(0,4),
 (1,3), (1,4),
 (2,2), (2,3), (2,4),
 (3,0), (3,1), (3,2), (3,3), (3,4),
 (4,0), (4,1), (4,2), (4,3), (4,4)}
```

**Step 3: Find Intersection**

```python
Intersection (pac ∩ atl):
[(0,4), (1,3), (1,4), (2,2), (3,0), (3,1), (4,0)]
```

These are exactly the cells where water can flow to **both** oceans!

## Why This Approach is Brilliant

### Time Complexity: O(m * n)
- Each cell is visited at most twice (once for Pacific, once for Atlantic)
- DFS from boundaries covers all reachable cells efficiently
- Much better than O(m²*n²) brute force approach!

### Space Complexity: O(m * n)
- Two sets storing reachable cells: `pac` and `atl`
- Recursion stack depth in worst case: O(m * n)

### Why Reverse Flow Works:
**Forward thinking (Hard):**
- From cell (2,2) → "Can I reach Pacific AND Atlantic?"
- Need to explore all paths from this cell
- Repeat for EVERY cell = lots of redundant work

**Reverse thinking (Smart):**
- From Pacific edge → "What cells can I reach?"
- From Atlantic edge → "What cells can I reach?"  
- Intersection = cells reachable from both = answer!
- Each cell explored at most twice total

## What I Learned

### Problem-Solving Insight:
- **Sometimes reversing the perspective solves the problem elegantly**
- Instead of "where can I go from here?", ask "what can reach here?"
- This is a common pattern in graph problems!

### Technical Skills:
- **Multi-source BFS/DFS**: Starting from multiple boundary points simultaneously
- **Set intersection for efficient lookup**: O(1) membership test
- **Reverse flow conditions**: Understanding when to flip comparison operators

### Pattern Recognition:
This is a classic **multi-source graph traversal** problem:
- Start from multiple source nodes (ocean boundaries)
- Find all reachable nodes from each set of sources
- Find common nodes (intersection)

## Related Problems

- [200. Number of Islands](../200/README.md) - Basic DFS on grid
- [695. Max Area of Island](../695/README.md) - DFS with area calculation
- [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) - Reverse DFS from boundaries
- [1765. Map of Highest Peak](https://leetcode.com/problems/map-of-highest-peak/) - Multi-source BFS

## Time and Space Complexity

- **Time Complexity**: O(m * n) where m = rows, n = cols
  - Each cell visited at most twice (once for Pacific, once for Atlantic)
  
- **Space Complexity**: O(m * n)
  - Two sets storing visited cells: `pac` and `atl`
  - Recursion stack in worst case: O(m * n)

## Tags
- Graph
- Depth-First Search (DFS)
- Matrix
- Multi-Source Traversal
- Reverse Thinking
