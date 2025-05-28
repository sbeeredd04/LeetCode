class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        def dfs(room):
            # Mark current room as visited
            visited.add(room)
            
            # Try each key in current room
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)
        
        # Start from room 0
        dfs(0)
        
        # Check if we visited all rooms
        return len(visited) == len(rooms)