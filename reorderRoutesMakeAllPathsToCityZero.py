class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Build adjacency list (undirected)
        adj = [[] for _ in range(n)]
        # Track original directions
        edges = set()
        
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
            edges.add((a,b))
            
        visited = set()
        changes = 0
        
        def dfs(city):
            nonlocal changes
            visited.add(city)
            
            for neighbor in adj[city]:
                if neighbor not in visited:
                    # Check if we need to flip direction
                    if (city, neighbor) not in edges:
                        changes += 1
                    dfs(neighbor)
        
        dfs(0)
        return changes