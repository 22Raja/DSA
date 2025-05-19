class Solution(object):
    def isValidSudoku(self, board):
        from collections import defaultdict
        column = defaultdict(set)
        row = defaultdict(set)
        square = defaultdict(set)


        for r in range(9):
            for c in range(9): 
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r] or board[r][c] in column[c] or board[r][c] in square[(r//3 , c//3 )]:
                    return False
                column[c].add(board[r][c])
                row[r].add(board[r][c])
                square[(r//3 , c//3 )].add( board[r][c])
        return True

        # Time Complexity - O(1)
        # Space Complexity - O(1)
         
                    
