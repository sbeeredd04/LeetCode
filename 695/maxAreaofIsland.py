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

    def maxAreaOfIslandDebug(self, grid: List[List[int]]) -> int:
        """
        DEBUG VERSION: Shows detailed flow with all debugging information
        """
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        direction_names = ["DOWN", "RIGHT", "UP", "LEFT"]
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        call_id = 0  # Track unique call IDs

        def print_grid_state(title=""):
            """Helper to print current grid state"""
            print(f"\n{title} - Current Grid State:")
            for i, row in enumerate(grid):
                print(f"  Row {i}: {row}")
            print()

        def dfs(r, c, area, depth=0, parent_call=""):
            nonlocal call_id
            current_call = f"DFS_{call_id}"
            call_id += 1
            
            indent = "  " * depth
            print(f"{indent}🔵 {current_call} ENTER: dfs({r}, {c}, area={area}) [Depth: {depth}]")
            print(f"{indent}   Parent: {parent_call}")
            
            # Check if out of bounds or water
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                print(f"{indent}❌ {current_call} OUT OF BOUNDS: ({r}, {c})")
                print(f"{indent}   Returning: 0")
                return 0
                
            if grid[r][c] == 0:
                print(f"{indent}❌ {current_call} WATER CELL: grid[{r}][{c}] = 0")
                print(f"{indent}   Returning: 0")
                return 0

            # Mark as visited and increment area
            old_value = grid[r][c]
            grid[r][c] = 0
            area += 1
            
            print(f"{indent}✅ {current_call} LAND CELL: grid[{r}][{c}] = {old_value} → 0")
            print(f"{indent}   Area after marking: {area}")
            
            # Show grid state after marking
            print_grid_state(f"{indent}   Grid after marking ({r},{c})")
            
            total_area = area
            print(f"{indent}🔄 {current_call} EXPLORING DIRECTIONS:")
            
            # Explore each direction
            for i, (dr, dc) in enumerate(directions):
                new_r, new_c = r + dr, c + dc
                print(f"{indent}   Direction {i+1}: {direction_names[i]} ({dr}, {dc}) → ({new_r}, {new_c})")
                
                direction_area = dfs(new_r, new_c, area, depth + 1, current_call)
                total_area += direction_area
                
                print(f"{indent}   {direction_names[i]} returned: {direction_area}")
                print(f"{indent}   Total area so far: {total_area}")
            
            print(f"{indent}🔴 {current_call} EXIT: Returning total_area = {total_area}")
            print(f"{indent}   Final grid state for this call:")
            print_grid_state(f"{indent}   ")
            
            return total_area

        print("=" * 80)
        print("DEBUGGING MAX AREA OF ISLAND")
        print("=" * 80)
        print(f"Grid dimensions: {ROWS} x {COLS}")
        print("\nInitial Grid State:")
        print_grid_state("Initial")
        
        # Main loop
        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 1:
                    print(f"\n{'='*60}")
                    print(f"🔍 STARTING NEW ISLAND at ({r}, {c})")
                    print(f"{'='*60}")
                    
                    area = dfs(r, c, 0, 0, "MAIN")
                    maxArea = max(maxArea, area)
                    
                    print(f"\n📊 Island completed:")
                    print(f"   Area found: {area}")
                    print(f"   Current maxArea: {maxArea}")
                    print(f"{'='*60}")
                else:
                    print(f"⏭️  Skipping cell ({r}, {c}): grid[{r}][{c}] = {grid[r][c]}")
        
        print(f"\n🎯 FINAL RESULT: maxArea = {maxArea}")
        print("=" * 80)
        return maxArea

    def maxAreaOfIslandBrokenDebug(self, grid: List[List[int]]) -> int:
        """
        DEBUG VERSION OF YOUR BROKEN CODE: Shows why it doesn't work
        """
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        direction_names = ["DOWN", "RIGHT", "UP", "LEFT"]
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        call_id = 0

        def print_grid_state(title=""):
            print(f"\n{title} - Current Grid State:")
            for i, row in enumerate(grid):
                print(f"  Row {i}: {row}")
            print()

        def dfs(r, c, area, depth=0, parent_call=""):
            nonlocal call_id
            current_call = f"DFS_{call_id}"
            call_id += 1
            
            indent = "  " * depth
            print(f"{indent}🔵 {current_call} ENTER: dfs({r}, {c}, area={area}) [Depth: {depth}]")
            print(f"{indent}   Parent: {parent_call}")
            
            # Check if out of bounds or water
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                print(f"{indent}❌ {current_call} OUT OF BOUNDS: ({r}, {c})")
                print(f"{indent}   Returning: 0")
                return 0
                
            if grid[r][c] == 0:
                print(f"{indent}❌ {current_call} WATER CELL: grid[{r}][{c}] = 0")
                print(f"{indent}   Returning: 0")
                return 0

            # Mark as visited and increment area
            old_value = grid[r][c]
            grid[r][c] = 0
            area += 1
            
            print(f"{indent}✅ {current_call} LAND CELL: grid[{r}][{c}] = {old_value} → 0")
            print(f"{indent}   Area after marking: {area}")
            print_grid_state(f"{indent}   Grid after marking ({r},{c})")
            
            print(f"{indent}🔄 {current_call} EXPLORING DIRECTIONS (BROKEN LOGIC):")
            
            # BROKEN LOGIC: This is where the problem occurs
            for i, (dr, dc) in enumerate(directions):
                new_r, new_c = r + dr, c + dc
                print(f"{indent}   Direction {i+1}: {direction_names[i]} ({dr}, {dc}) → ({new_r}, {new_c})")
                print(f"{indent}   Calling dfs({new_r}, {new_c}, {area})")
                
                direction_area = dfs(new_r, new_c, area, depth + 1, current_call)
                print(f"{indent}   {direction_names[i]} returned: {direction_area}")
                
                # ❌ BROKEN: Adding returned area to current area
                old_area = area
                area += direction_area
                print(f"{indent}   ❌ BROKEN LOGIC: area = {old_area} + {direction_area} = {area}")
                print(f"{indent}   This creates DOUBLE COUNTING!")
            
            print(f"{indent}🔴 {current_call} EXIT: Returning area = {area}")
            print(f"{indent}   Final grid state for this call:")
            print_grid_state(f"{indent}   ")
            
            return area

        print("=" * 80)
        print("DEBUGGING BROKEN VERSION - WHY IT DOESN'T WORK")
        print("=" * 80)
        print(f"Grid dimensions: {ROWS} x {COLS}")
        print("\nInitial Grid State:")
        print_grid_state("Initial")
        
        # Main loop
        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 1:
                    print(f"\n{'='*60}")
                    print(f"🔍 STARTING NEW ISLAND at ({r}, {c})")
                    print(f"{'='*60}")
                    
                    area = dfs(r, c, 0, 0, "MAIN")
                    maxArea = max(maxArea, area)
                    
                    print(f"\n📊 Island completed:")
                    print(f"   Area found: {area}")
                    print(f"   Current maxArea: {maxArea}")
                    print(f"{'='*60}")
                else:
                    print(f"⏭️  Skipping cell ({r}, {c}): grid[{r}][{c}] = {grid[r][c]}")
        
        print(f"\n🎯 FINAL RESULT: maxArea = {maxArea}")
        print("=" * 80)
        return maxArea 