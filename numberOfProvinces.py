class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def dfs(city):
            visited.add(city)
            # Check connections to all other cities
            for next_city in range(n):
                if isConnected[city][next_city] == 1 and next_city not in visited:
                    dfs(next_city)
        
        # Check each city
        for city in range(n):
            if city not in visited:
                dfs(city)
                provinces += 1
                
        return provinces