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

    # DETAILED DEBUG VERSION for Mermaid Analysis
    def exist_debug_detailed(self, board: list[list[str]], word: str) -> bool:
        """
        Detailed debug version for algorithm analysis
        Tracks state transitions for mermaid diagram creation
        """
        visited = set()
        call_count = [0]
        state_log = []
        
        def track_debug(row, col, word_index, depth="", parent_call=""):
            call_count[0] += 1
            call_id = f"call_{call_count[0]}"
            
            # Log the state for mermaid diagram
            state_info = {
                'call_id': call_id,
                'row': row,
                'col': col, 
                'word_index': word_index,
                'depth': len(depth)//4,
                'parent': parent_call,
                'visited': visited.copy(),
                'looking_for': word[word_index] if word_index < len(word) else 'DONE'
            }
            
            print(f"{depth}[{call_id}] track({row}, {col}, {word_index})")
            
            # Check bounds first
            if not (0 <= row < len(board) and 0 <= col < len(board[0])):
                print(f"{depth}    -> OUT_OF_BOUNDS")
                state_info['result'] = 'OUT_OF_BOUNDS'
                state_log.append(state_info)
                return False
            
            current_char = board[row][col]
            print(f"{depth}    Cell[{row}][{col}] = '{current_char}', Looking for: '{word[word_index] if word_index < len(word) else 'DONE'}'")
            print(f"{depth}    Visited: {visited}")
            
            # Base case - found complete word
            if word_index == len(word):
                print(f"{depth}    -> SUCCESS! Word found!")
                state_info['result'] = 'SUCCESS'
                state_log.append(state_info)
                return True
            
            # Check if already visited
            if (row, col) in visited:
                print(f"{depth}    -> ALREADY_VISITED")
                state_info['result'] = 'ALREADY_VISITED'
                state_log.append(state_info)
                return False
                
            # Check character match
            if current_char != word[word_index]:
                print(f"{depth}    -> CHAR_MISMATCH (expected '{word[word_index]}', got '{current_char}')")
                state_info['result'] = 'CHAR_MISMATCH'
                state_log.append(state_info)
                return False

            # Character matches - add to visited and explore
            print(f"{depth}    -> MATCH! Adding ({row}, {col}) to visited")
            visited.add((row, col))
            state_info['action'] = 'ADDED_TO_VISITED'
            
            # Explore 4 directions
            directions = [
                (row + 1, col, "DOWN"),
                (row - 1, col, "UP"), 
                (row, col + 1, "RIGHT"),
                (row, col - 1, "LEFT")
            ]
            
            print(f"{depth}    Exploring 4 directions...")
            success_found = False
            
            for new_row, new_col, direction in directions:
                print(f"{depth}      Trying {direction} -> ({new_row}, {new_col})")
                if track_debug(new_row, new_col, word_index + 1, depth + "    ", call_id):
                    print(f"{depth}      {direction} SUCCESS!")
                    success_found = True
                    break
                print(f"{depth}      {direction} failed")
            
            # Backtrack
            print(f"{depth}    Backtracking: removing ({row}, {col}) from visited")
            visited.remove((row, col))
            
            if success_found:
                state_info['result'] = 'SUCCESS_VIA_CHILD'
                print(f"{depth}    -> SUCCESS via child path")
            else:
                state_info['result'] = 'ALL_DIRECTIONS_FAILED'
                print(f"{depth}    -> FAILED: all directions exhausted")
            
            state_log.append(state_info)
            return success_found

        # Main execution
        print(f"\nStarting Word Search for '{word}'")
        print("Board layout:")
        for i, row in enumerate(board):
            print(f"  Row {i}: {row}")
        print()
        
        # Try each possible starting position
        for start_row in range(len(board)):
            for start_col in range(len(board[0])):
                if board[start_row][start_col] == word[0]:
                    print(f"\nTRYING START: ({start_row}, {start_col}) = '{board[start_row][start_col]}'")
                    print("-" * 50)
                    
                    # Reset for each starting position
                    visited.clear()
                    
                    if track_debug(start_row, start_col, 0, "", "main"):
                        print(f"\nWORD FOUND! Starting from ({start_row}, {start_col})")
                        print(f"\nAlgorithm Analysis - State Log:")
                        for i, state in enumerate(state_log[-10:]):  # Show last 10 states
                            print(f"  {i+1}. Call {state['call_id']}: ({state['row']}, {state['col']}) -> {state['result']}")
                        return True
                    
                    print(f"FAILED from ({start_row}, {start_col})")
        
        print(f"\nWord '{word}' not found in board")
        return False
        
    # Quick test method
    def test_debug(self):
        """Quick test with a small example"""
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        print("="*60)
        print("TESTING WORD SEARCH DEBUG")
        print("="*60)
        return self.exist_debug_detailed(board, word)
