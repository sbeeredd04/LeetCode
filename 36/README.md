# 36. Valid Sudoku

## Problem Statement
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

**Note:**
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

## Examples
```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: true
```

## Constraints
- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`

## Approach: Single Pass with Three Tracking Arrays

### Key Insights
1. **Single Pass Solution**: We can validate all three rules (row, column, box) in one iteration
2. **Box Index Calculation**: The crucial formula to map (i,j) coordinates to box index:
   ```python
   box_index = (i // 3) * 3 + (j // 3)
   ```
3. **Early Termination**: Return `False` immediately when any duplicate is found

### Box Index Mapping Explained
The 9x9 Sudoku board has 9 sub-boxes arranged in a 3x3 grid:
```
Box Layout:
[0] [1] [2]
[3] [4] [5] 
[6] [7] [8]
```

For any cell at position (i, j):
- `i // 3` gives the box row (0, 1, or 2)
- `j // 3` gives the box column (0, 1, or 2)
- `box_index = (i // 3) * 3 + (j // 3)` maps to the correct box

**Examples:**
- Cell (0,0) → Box 0: `(0//3)*3 + (0//3) = 0*3 + 0 = 0`
- Cell (1,4) → Box 1: `(1//3)*3 + (4//3) = 0*3 + 1 = 1`
- Cell (4,7) → Box 5: `(4//3)*3 + (7//3) = 1*3 + 2 = 5`
- Cell (8,8) → Box 8: `(8//3)*3 + (8//3) = 2*3 + 2 = 8`

### Implementation
```python
def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Initialize tracking arrays for each row, column, and box
    row = [[] for i in range(9)]
    column = [[] for i in range(9)]
    box = [[] for i in range(9)]
    
    # Iterate through each cell in the 9x9 board
    for i in range(9):
        for j in range(9):
            # Skip empty cells
            if board[i][j] != '.':
                current_num = board[i][j]
                
                # Check row validity
                if current_num in row[i]:
                    return False
                row[i].append(current_num)
                
                # Check column validity  
                if current_num in column[j]:
                    return False
                column[j].append(current_num)
                
                # Check box validity
                box_index = (i // 3) * 3 + (j // 3)
                if current_num in box[box_index]:
                    return False
                box[box_index].append(current_num)
    
    return True
```

### Time & Space Complexity
- **Time**: O(81) = O(1) - Fixed 9x9 board size
- **Space**: O(81) = O(1) - Maximum 81 elements across all tracking arrays

## Alternative Approaches

### Approach 2: Using Sets for O(1) Lookup
```python
def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                num = board[i][j]
                box_index = (i // 3) * 3 + (j // 3)
                
                if (num in rows[i] or 
                    num in cols[j] or 
                    num in boxes[box_index]):
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
    
    return True
```

### Approach 3: One-Liner with String Encoding
```python
def isValidSudoku(self, board: List[List[str]]) -> bool:
    seen = set()
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                num = board[i][j]
                if (f"row{i}-{num}" in seen or
                    f"col{j}-{num}" in seen or
                    f"box{(i//3)*3 + j//3}-{num}" in seen):
                    return False
                seen.add(f"row{i}-{num}")
                seen.add(f"col{j}-{num}")
                seen.add(f"box{(i//3)*3 + j//3}-{num}")
    return True
```

## Key Programming Concepts

### Matrix Iteration Patterns
```python
# Standard nested loops
for i in range(9):
    for j in range(9):
        # process board[i][j]

# Alternative with enumerate
for i, row in enumerate(board):
    for j, cell in enumerate(row):
        # process cell at (i, j)
```

### Box Index Formula Derivation
```
For a 9x9 grid divided into 3x3 boxes:
- Box row = i // 3 (which 3x3 row of boxes)
- Box col = j // 3 (which 3x3 col of boxes)  
- Linear index = box_row * 3 + box_col
- Therefore: box_index = (i // 3) * 3 + (j // 3)
```

## Common Mistakes & Tips
1. **Off-by-one errors**: Remember Python uses 0-based indexing
2. **Box calculation**: The formula `(i // 3) * 3 + (j // 3)` is crucial to memorize
3. **Empty cell handling**: Always check for `'.'` before processing
4. **Early return**: Return `False` immediately when duplicate found for efficiency
5. **Data structure choice**: Lists vs Sets vs String encoding - each has trade-offs

## Follow-up Questions
- Can you solve it in O(1) space? (Not possible due to need to track seen numbers)
- How would you modify this to solve the Sudoku? (Backtracking algorithm)
- What if the board size was N×N instead of 9×9? (Generalize the box formula) 

