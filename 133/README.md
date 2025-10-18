# 133. Clone Graph

## Problem Description

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Each node in the graph contains a `val` (int) and a list (`List[Node]`) of its neighbors.

**Note:**
- The number of nodes in the graph is in the range `[0, 100]`
- `1 <= Node.val <= 100`
- `Node.val` is unique for each node
- There are no repeated edges and no self-loops in the input graph
- The graph is connected and all nodes can be visited starting from the given node

## Example

```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
```

## Approach

The solution uses **Depth-First Search (DFS)** with a hash map to avoid cycles and ensure each node is cloned only once.

### Algorithm Steps:

1. **Hash Map for Tracking**: Use `oldToNew` dictionary to map original nodes to their clones
2. **DFS Function**: Recursively traverse the graph
3. **Base Case**: If node already exists in hash map, return the cloned node
4. **Clone Node**: Create a new Node with the same value
5. **Recursive Cloning**: Clone all neighbors recursively
6. **Return Clone**: Return the cloned node

### Key Insights:

- **Cycle Handling**: The hash map prevents infinite recursion in cyclic graphs
- **Deep Copy**: Each node and its neighbors are completely cloned
- **Connected Graph**: Since the graph is connected, DFS from any node will visit all nodes

## Time & Space Complexity

- **Time Complexity**: O(V + E) where V is the number of vertices and E is the number of edges
- **Space Complexity**: O(V) for the hash map and recursion stack

## Solution Code

```python
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
```

## Alternative Approaches

### 1. Breadth-First Search (BFS)
- Use a queue instead of recursion
- Same time/space complexity
- Better for very deep graphs

### 2. Iterative DFS
- Use a stack instead of recursion
- Avoids stack overflow for very deep graphs

## Related Problems

- [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [207. Course Schedule](https://leetcode.com/problems/course-schedule/)

## Tags

- Graph
- Depth-First Search
- Breadth-First Search
- Hash Table
- Recursion
