from typing import List, Dict, Tuple
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build the graph
        graph = defaultdict(dict)
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value
        
        def bfs(start: str, end: str) -> float:
            if start not in graph or end not in graph:
                return -1.0
            queue = deque([(start, 1.0)])
            visited = set()
            while queue:
                current, product = queue.popleft()
                if current == end:
                    return product
                visited.add(current)
                for neighbor, value in graph[current].items():
                    if neighbor not in visited:
                        queue.append((neighbor, product * value))
            return -1.0
        
        results = []
        for dividend, divisor in queries:
            results.append(bfs(dividend, divisor))
        
        return results
