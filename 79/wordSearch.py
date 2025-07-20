class Solution:

    def inBounds(self, i, j, board):
        return 0 <= i < len(board) and 0 <= j < len(board[0])

    def exist(self, board: list[list[str]], word: str) -> bool:
        
        visited = set()
        
        def track(i, j, curr):
            
            if curr == len(word):  # FIXED: was i == len(word)
                return True
            
            if not self.inBounds(i, j, board) or (i, j) in visited or board[i][j] != word[curr]:
                return False

            visited.add((i, j))
            res = (track(i + 1, j, curr + 1) or
                   track(i - 1, j, curr + 1) or
                   track(i, j + 1, curr + 1) or
                   track(i, j - 1, curr + 1))
            visited.remove((i, j))
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if track(i, j, 0):
                        return True
        return False

    # DEBUG VERSION: Uncomment to see algorithm in action!
    def exist_debug(self, board: list[list[str]], word: str) -> bool:
        """
        Debug version that shows step-by-step execution
        Usage: solution.exist_debug(board, word)
        """
        visited = set()
        call_count = [0]
        
        def track_debug(row, col, word_index, depth=""):
            call_count[0] += 1
            print(f"{depth}📞 Call #{call_count[0]}: track({row}, {col}, {word_index})")
            
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                print(f"{depth}🔍 Looking for '{word[word_index] if word_index < len(word) else 'DONE'}' at board[{row}][{col}] = '{board[row][col]}'")
            else:
                print(f"{depth}🔍 Looking at OUT_OF_BOUNDS position ({row}, {col})")
                
            print(f"{depth}📍 Visited: {visited}")
            
            # Base case
            if word_index == len(word):
                print(f"{depth}🎉 SUCCESS! Found complete word!")
                return True
            
            # Check bounds
            if not (0 <= row < len(board) and 0 <= col < len(board[0])):
                print(f"{depth}❌ Out of bounds")
                return False
                
            # Check visited
            if (row, col) in visited:
                print(f"{depth}❌ Already visited")
                return False
                
            # Check character match
            if board[row][col] != word[word_index]:
                print(f"{depth}❌ Character mismatch: expected '{word[word_index]}', got '{board[row][col]}'")
                return False

            print(f"{depth}✅ Match found! Adding ({row}, {col}) to visited")
            visited.add((row, col))
            
            print(f"{depth}🔄 Exploring 4 directions from ({row}, {col})...")
            
            # Explore all 4 directions with more detailed logging
            directions = [
                (row + 1, col, "DOWN"),
                (row - 1, col, "UP"), 
                (row, col + 1, "RIGHT"),
                (row, col - 1, "LEFT")
            ]
            
            for new_row, new_col, direction in directions:
                print(f"{depth}  🧭 Trying {direction} to ({new_row}, {new_col})")
                if track_debug(new_row, new_col, word_index + 1, depth + "    "):
                    print(f"{depth}  ✅ {direction} path succeeded!")
                    visited.remove((row, col))
                    return True
                print(f"{depth}  ❌ {direction} path failed")
            
            print(f"{depth}⬅️ Backtracking: removing ({row}, {col}) from visited")
            visited.remove((row, col))
            print(f"{depth}❌ All directions failed from ({row}, {col})")
            return False

        # Main loop with debugging
        print(f"\n🎯 Starting Word Search for '{word}'")
        print("📋 Board:")
        for i, row in enumerate(board):
            print(f"   {i}: {row}")
        print()
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    print(f"\n🚀 Trying starting position ({row}, {col}) = '{board[row][col]}'")
                    print("="*60)
                    if track_debug(row, col, 0):
                        print(f"\n🏆 WORD '{word}' FOUND starting from ({row}, {col})!")
                        return True
                    print(f"💔 Failed starting from ({row}, {col})")
        
        print(f"\n😞 Word '{word}' not found anywhere in the board")
        return False
