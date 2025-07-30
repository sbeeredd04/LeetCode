from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Original solution using nonlocal variable to track area
        """
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

    def maxAreaOfIslandOptimized(self, grid: List[List[int]]) -> int:
        """
        Optimized solution using return value accumulation instead of nonlocal
        """
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