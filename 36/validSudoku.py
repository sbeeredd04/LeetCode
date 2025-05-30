class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for i in range(0, 9)]
        column = [[] for i in range(0, 9)]
        box = [[] for i in range(0, 9)]

        #iterate throught the for loop adding row column and 
        for i in range(0, 9):
            for j in range(0, 9):
                
                #if the cell is not empty
                if board[i][j] != '.': 
                    
                    #check if the number is already in the ro
                    if board[i][j] in row[i]:
                        return False
                    row[i].append(board[i][j])
                    
                    #check if the number is already in the column
                    if board[i][j] in column[j]:
                        return False
                    column[j].append(board[i][j])
                    
                    #check if the number is already in the box
                    box_index = (i // 3) * 3 + (j // 3)
                    if board[i][j] in box[box_index]:
                        return False
                    box[box_index].append(board[i][j])
                    
        return True