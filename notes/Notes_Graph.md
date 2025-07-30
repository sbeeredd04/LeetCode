# Graph & Connected Components Notes

## Overview
Graph problems involve nodes connected by edges, representing relationships between entities. Connected components are groups of nodes that are reachable from each other. This is essential for network analysis, social graphs, and spatial problems.

## Core Concepts

### 1. Graph Representation
- **Adjacency Matrix**: 2D array where `matrix[i][j]` indicates connection between nodes i and j
- **Adjacency List**: Array of lists where each list contains neighbors of that node
- **Grid-based**: 2D grid where cells represent nodes and adjacency is based on position

### 2. Connected Components
A connected component is a subgraph where every pair of vertices is connected by a path.

```python
# Basic connected component pattern
def find_components(graph):
    visited = set()
    components = 0
    
    for node in graph:
        if node not in visited:
            dfs(node, graph, visited)
            components += 1
    
    return components
```

### 3. DFS vs BFS for Graph Traversal

**DFS (Depth-First Search):**
- Uses recursion or stack
- Explores as far as possible along each branch
- Better for connected components and path finding
- Space complexity: O(depth) for recursion stack

**BFS (Breadth-First Search):**
- Uses queue
- Explores all neighbors at current depth before moving deeper
- Better for shortest path problems
- Space complexity: O(width) for queue

## Key Patterns

### 1. Connected Components Counting

**Pattern:**
```python
def count_components(grid):
    if not grid:
        return 0
    
    components = 0
    visited = set()  # or in-place modification
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and (i,j) not in visited:
                dfs(i, j, grid, visited)
                components += 1
    
    return components
```

**Key Insights:**
- Count only when starting new exploration
- Mark visited nodes to avoid double counting
- Use either separate visited set or in-place modification

### 2. Grid-based Graph Traversal

**Direction Vectors Pattern:**
```python
# Four directions: down, right, up, left
directions = [[1,0], [0,1], [-1,0], [0,-1]]

# Eight directions (including diagonals)
directions = [[1,0], [0,1], [-1,0], [0,-1], 
              [1,1], [1,-1], [-1,1], [-1,-1]]

def dfs(r, c, grid):
    # Boundary check
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        return
    
    # Validity check
    if grid[r][c] == "0":
        return
    
    # Mark as visited
    grid[r][c] = "0"
    
    # Explore neighbors
    for dr, dc in directions:
        dfs(r + dr, c + dc, grid)
```

### 3. In-place vs Separate Visited Tracking

**In-place Modification:**
```python
# Change grid values to mark visited
grid[r][c] = "0"  # Mark as visited
```

**Separate Visited Array:**
```python
# Use separate 2D array
visited = [[False] * cols for _ in range(rows)]
visited[r][c] = True
```

**Set-based Tracking:**
```python
# Use set for coordinate tracking
visited = set()
visited.add((r, c))
```

### 4. Flood Fill Pattern

**Basic Flood Fill:**
```python
def flood_fill(image, sr, sc, newColor):
    if not image:
        return image
    
    old_color = image[sr][sc]
    if old_color == newColor:
        return image
    
    def dfs(r, c):
        if (r < 0 or c < 0 or 
            r >= len(image) or c >= len(image[0]) or 
            image[r][c] != old_color):
            return
        
        image[r][c] = newColor
        
        for dr, dc in [[1,0], [0,1], [-1,0], [0,-1]]:
            dfs(r + dr, c + dc)
    
    dfs(sr, sc)
    return image
```

## Common Problem Types

### 1. Island/Connected Component Counting
- **Problem**: Count number of connected regions
- **Pattern**: DFS/BFS with component counting
- **Example**: Number of Islands (LeetCode 200)

### 2. Area/Maximum Size Calculation
- **Problem**: Find largest connected component
- **Pattern**: DFS/BFS with size tracking
- **Example**: Max Area of Island (LeetCode 695)

### 3. Boundary Detection
- **Problem**: Find boundaries of connected regions
- **Pattern**: DFS with boundary condition checking
- **Example**: Surrounded Regions (LeetCode 130)

### 4. Shortest Path in Grid
- **Problem**: Find shortest path between two points
- **Pattern**: BFS with distance tracking
- **Example**: Shortest Path in Binary Matrix (LeetCode 1091)

## Implementation Templates

### DFS Template
```python
def dfs_template(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()  # or use in-place modification
    
    def dfs(r, c):
        # Base cases
        if (r < 0 or c < 0 or 
            r >= rows or c >= cols or 
            grid[r][c] == "0" or 
            (r,c) in visited):
            return
        
        # Mark as visited
        visited.add((r,c))
        # or: grid[r][c] = "0"
        
        # Explore neighbors
        for dr, dc in [[1,0], [0,1], [-1,0], [0,-1]]:
            dfs(r + dr, c + dc)
    
    # Main loop
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                dfs(r, c)
                count += 1
    
    return count
```

### BFS Template
```python
from collections import deque

def bfs_template(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    
    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        visited.add((start_r, start_c))
        
        while queue:
            r, c = queue.popleft()
            
            # Explore neighbors
            for dr, dc in [[1,0], [0,1], [-1,0], [0,-1]]:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < rows and 
                    0 <= nc < cols and 
                    grid[nr][nc] == "1" and 
                    (nr,nc) not in visited):
                    visited.add((nr,nc))
                    queue.append((nr,nc))
    
    # Main loop
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r, c)
                count += 1
    
    return count
```

## Optimization Techniques

### 1. Early Termination
```python
# Stop when target is found
if (r, c) == target:
    return True
```

### 2. Pruning Invalid Paths
```python
# Skip if current path is already longer than best
if current_length >= best_length:
    return
```

### 3. Memory Optimization
```python
# Use in-place modification instead of separate visited array
grid[r][c] = "0"  # Instead of visited[r][c] = True
```

### 4. Direction Optimization
```python
# Use direction vectors for cleaner code
directions = [[1,0], [0,1], [-1,0], [0,-1]]
for dr, dc in directions:
    dfs(r + dr, c + dc)
```

## Common Pitfalls

### 1. Infinite Recursion
- **Cause**: Not marking nodes as visited
- **Solution**: Always mark nodes before exploring

### 2. Boundary Errors
- **Cause**: Not checking grid boundaries
- **Solution**: Always check bounds before accessing

### 3. Double Counting
- **Cause**: Counting components during exploration
- **Solution**: Count only when starting new exploration

### 4. Wrong Direction Vectors
- **Cause**: Incorrect direction arrays
- **Solution**: Use systematic direction vectors

## Time & Space Complexity

### Time Complexity
- **DFS/BFS**: O(V + E) where V = vertices, E = edges
- **Grid traversal**: O(m × n) where m, n are grid dimensions
- **Connected components**: O(m × n) for grid-based problems

### Space Complexity
- **DFS recursion stack**: O(depth) in worst case
- **BFS queue**: O(width) in worst case
- **Visited tracking**: O(m × n) for grid problems
- **In-place modification**: O(1) additional space

## Advanced Concepts

### 1. Union-Find (Disjoint Set)
- **Use case**: Dynamic connectivity problems
- **Complexity**: Near O(1) for union/find operations
- **Applications**: Kruskal's algorithm, dynamic graph connectivity

### 2. Strongly Connected Components
- **Use case**: Directed graph analysis
- **Algorithm**: Tarjan's or Kosaraju's algorithm
- **Applications**: Dependency analysis, cycle detection

### 3. Articulation Points & Bridges
- **Use case**: Network reliability analysis
- **Algorithm**: DFS with low-link values
- **Applications**: Critical infrastructure identification

## Practice Problems by Difficulty

### Easy
- [200. Number of Islands](./200/README.md)
- [733. Flood Fill](#)
- [463. Island Perimeter](#)

### Medium
- [695. Max Area of Island](#)
- [130. Surrounded Regions](#)
- [994. Rotting Oranges](#)
- [1091. Shortest Path in Binary Matrix](#)

### Hard
- [827. Making A Large Island](#)
- [1192. Critical Connections](#)
- [947. Most Stones Removed with Same Row or Column](#)

## Key Takeaways

1. **Pattern Recognition**: Most graph problems follow connected components or shortest path patterns
2. **Traversal Choice**: DFS for components, BFS for shortest paths
3. **Visited Tracking**: Choose between in-place modification and separate tracking based on constraints
4. **Boundary Checking**: Always verify coordinates before accessing grid cells
5. **Direction Vectors**: Use systematic arrays for neighbor exploration
6. **Component Counting**: Count only when starting new exploration, not during traversal

## Resources

- **Visualization**: Use mermaid diagrams to understand graph structure
- **Practice**: Focus on grid-based problems first, then move to adjacency list problems
- **Patterns**: Master the connected components pattern before moving to advanced graph algorithms
- **Optimization**: Learn when to use DFS vs BFS based on problem requirements 