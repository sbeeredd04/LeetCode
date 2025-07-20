# Word Search - LeetCode 79

## Problem Statement
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example:**
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE" 
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

## Initial Hunch and Hints
<details>
<summary>🤔 My First Thoughts</summary>

When I first saw this problem, my immediate thought was:
> "This looks like I need to explore the board systematically, trying to match letters one by one!"

My initial hunch was to:
1. **Start from top-left corner (0,0)** and try to find the word
2. **Explore in all 4 directions** (up, down, left, right) 
3. **Keep track of which letters I've used** so I don't revisit the same cell

But I quickly realized two major issues:
- **What if the first letter isn't at (0,0)?** The word could start anywhere!
- **How do I avoid revisiting cells?** I need some way to mark visited cells

This led me to the solution approach below!
</details>

<details>
<summary>💡 Key Insights That Helped</summary>

- **Try every possible starting position**: Don't assume the word starts at (0,0)
- **Backtracking is perfect here**: Explore a path, and if it doesn't work, backtrack and try another
- **Use a visited set**: Track which cells we've used in the current path
- **Remember to clean up**: Remove cells from visited set when backtracking
</details>

<details>
<summary>🚨 Common Pitfalls I Avoided</summary>

- **Forgetting to try all starting positions**: Initially I thought about starting from (0,0) only
- **Not cleaning up visited set**: After exploring a path, I need to remove the cell from visited
- **Mixing up indices**: It's easy to confuse board indices with word character indices
</details>

## My Solution Analysis

### What I Implemented:
```python
class Solution:
    def inBounds(self, i, j, board):
        return 0 <= i < len(board) and 0 <= j < len(board[0])

    def exist(self, board: list[list[str]], word: str) -> bool:
        visited = set()
        
        def track(i, j, curr):
            if i == len(word):  # ⚠️ BUG: Should be curr == len(word)
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
```

### Issues I Found in My Code:


## Algorithm Analysis with Debugging

Let me trace through the algorithm step by step with debugging output:

### Example Trace: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"

```python
def exist_with_debug(self, board: list[list[str]], word: str) -> bool:
    visited = set()
    call_count = [0]  # Use list to modify in nested function
    
    def track(row, col, word_index, depth=""):
        call_count[0] += 1
        print(f"{depth}Call #{call_count[0]}: track({row}, {col}, {word_index}) - Looking for '{word[word_index] if word_index < len(word) else 'DONE'}'")
        print(f"{depth}Current cell: board[{row}][{col}] = '{board[row][col] if 0 <= row < len(board) and 0 <= col < len(board[0]) else 'OUT_OF_BOUNDS'}'")
        print(f"{depth}Visited so far: {visited}")
        
        # Base case: found the complete word
        if word_index == len(word):
            print(f"{depth}✅ SUCCESS! Found complete word!")
            return True
        
        # Check bounds
        if not (0 <= row < len(board) and 0 <= col < len(board[0])):
            print(f"{depth}❌ Out of bounds!")
            return False
            
        # Check if already visited
        if (row, col) in visited:
            print(f"{depth}❌ Already visited this cell!")
            return False
            
        # Check character match
        if board[row][col] != word[word_index]:
            print(f"{depth}❌ Character mismatch! Expected '{word[word_index]}', got '{board[row][col]}'")
            return False

        print(f"{depth}✓ Character match! Adding ({row}, {col}) to visited")
        visited.add((row, col))
        
        # Explore all 4 directions
        print(f"{depth}Exploring 4 directions...")
        result = (track(row + 1, col, word_index + 1, depth + "  ") or  # Down
                 track(row - 1, col, word_index + 1, depth + "  ") or  # Up
                 track(row, col + 1, word_index + 1, depth + "  ") or  # Right
                 track(row, col - 1, word_index + 1, depth + "  "))    # Left
        
        # Backtrack: remove from visited
        print(f"{depth}Backtracking: removing ({row}, {col}) from visited")
        visited.remove((row, col))
        
        result_str = "SUCCESS" if result else "FAILED"
        print(f"{depth}Returning {result_str} for position ({row}, {col})")
        return result

    # Try starting from every cell
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == word[0]:
                print(f"\n🔍 Trying starting position ({row}, {col}) with character '{board[row][col]}'")
                if track(row, col, 0):
                    print(f"\n🎉 WORD FOUND starting from ({row}, {col})!")
                    return True
                print(f"❌ Failed starting from ({row}, {col})")
    
    print("\n😞 Word not found anywhere!")
    return False
```

## Algorithm Flow Diagram

Based on the debugging trace, here's how the algorithm works:

```mermaid
flowchart TD
    A[Start: For each cell in board] --> B{Cell == word[0]?}
    B --No--> A
    B --Yes--> C[Call track(row, col, 0)]
    
    C --> D[track function starts]
    D --> E{word_index == len(word)?}
    E --Yes--> F[🎉 SUCCESS! Return True]
    E --No--> G{Valid position & not visited & char match?}
    
    G --No--> H[❌ Return False]
    G --Yes--> I[Add to visited set]
    
    I --> J[Explore 4 directions]
    J --> K[track(row+1, col, word_index+1)]
    J --> L[track(row-1, col, word_index+1)]
    J --> M[track(row, col+1, word_index+1)]
    J --> N[track(row, col-1, word_index+1)]
    
    K --> O{Any direction returns True?}
    L --> O
    M --> O  
    N --> O
    
    O --Yes--> P[Remove from visited & Return True]
    O --No--> Q[Remove from visited & Return False]
    
    P --> R[Backtrack complete]
    Q --> R
    
    F --> S[Word found!]
    H --> T{More starting positions?}
    R --> T
    T --Yes--> A
    T --No--> U[Word not found]
    
    style F fill:#90EE90
    style S fill:#90EE90
    style H fill:#FFB6C1
    style U fill:#FFB6C1
```

## Self-Reflection: What I Did and Learned

### 💪 What I Did Well

**1. Recognized the Pattern Immediately**
I'm getting really good at spotting backtracking problems! The moment I saw "explore paths" and "can't reuse cells," I knew this was a classic DFS + backtracking situation. That pattern recognition is getting stronger with each problem I solve.

**2. Thought About All Starting Positions**
Initially, my brain wanted to just start from (0,0), but I quickly caught myself thinking "wait, what if the word doesn't start there?" That's growth! I'm learning to question my first assumptions and think about edge cases upfront.

**3. Used the visited Set Correctly**  
I knew I needed to track visited cells, and more importantly, I remembered to **remove cells from the visited set during backtracking**. This is crucial - if I don't clean up, I might miss valid paths later.

**4. Separated Concerns with Helper Function**
Creating the `inBounds` helper function was smart - it keeps the main logic clean and makes the code more readable. I'm getting better at writing modular code!

### 🤔 What I Struggled With


### 🧠 Problem-Solving Process That Worked

**Step 1: High-Level Strategy**
- "I need to find a word in a grid by exploring adjacent cells"
- "This screams DFS + backtracking to me"
- "I'll need to try every possible starting position"

**Step 2: Handle the Details**  
- "I need to avoid revisiting cells in the current path"
- "But I should allow revisiting cells in different paths"
- "So I need to add/remove from visited set during backtracking"

**Step 3: Implementation**
- Start with the main loop to try each starting position
- Implement the recursive backtracking function
- Handle bounds checking, visited tracking, and character matching

### 🎯 What I'd Do Differently Next Time

**1. Start with Crystal Clear Variable Names**
```python
# Instead of: track(i, j, curr)
# Use: track(board_row, board_col, word_index)
```
This would have saved me so much debugging time!

**2. Write the Base Case First**
I should have started with `if word_index == len(word): return True` and worked backwards. Getting the base case right first prevents a lot of bugs.

**3. Add Debug Prints Early**  
I spent time trying to trace through the logic in my head. Next time, I'll add debug prints right away to see exactly what's happening.

**4. Test Small Examples First**
I should test with a 2x2 grid and a 3-letter word first, then work up to larger examples.

### 🔍 Key Insights I'll Remember

**1. Backtracking Template Recognition**  
This problem perfectly follows the backtracking template:
```python
def backtrack(state):
    if base_case: return result
    if invalid: return False
    
    # Choose
    make_choice()
    
    # Explore  
    result = backtrack(new_state)
    
    # Unchoose (backtrack)
    undo_choice()
    
    return result
```

**2. Visited Set Pattern**
For grid traversal problems:
- Add to visited before exploring
- Remove from visited after exploring (cleanup)
- This allows the same cell to be used in different paths

**3. Multiple Starting Points**
Don't assume problems start from a specific position. Often you need to try all possible starting points.

### 📈 How This Problem Helped Me Grow

**Pattern Recognition:** I'm getting faster at identifying DFS + backtracking problems  
**Edge Case Thinking:** I caught the "multiple starting positions" requirement early  
**Code Organization:** Using helper functions makes complex problems more manageable  
**Debugging Skills:** I'm learning to add strategic debug output to trace algorithm execution

### 🎉 What I'm Proud Of

Even with the variable naming issues, my core algorithm logic was solid! I understood:
- Need to try all starting positions  
- Need to use backtracking with visited tracking
- Need to explore all 4 directions
- Need to clean up state during backtracking

That shows my backtracking fundamentals are getting strong, even if my implementation details need work.

### 🚀 Next Steps for Improvement  

1. **Practice more grid-based backtracking problems** to reinforce the patterns
2. **Always use descriptive variable names** - no shortcuts with i, j, k
3. **Write base cases first** in recursive functions  
4. **Add debug output early** in complex recursive algorithms
5. **Test with simple examples** before moving to complex test cases

This problem was really fun to solve, and even though I made some implementation mistakes, I feel like my problem-solving approach is getting much stronger! 🎯

---

**Time Complexity:** O(N × M × 4^L) where N×M is board size, L is word length  
**Space Complexity:** O(L) for recursion depth and visited set  
**Pattern:** DFS + Backtracking with state cleanup
