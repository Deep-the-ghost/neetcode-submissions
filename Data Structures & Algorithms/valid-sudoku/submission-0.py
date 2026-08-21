class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        for row in board:
            num = []
            for n in row:
                if n != ".":
                    num.append(n)
            if len(num) != len(set(num)):
                return False


        for col in range(9):
            num = []
            for row in board:
                if row[col] != ".":
                    num.append(row[col])
            if len(num) != len(set(num)):
                return False


        for row in range(0,9,3):
            for col in range(0,9,3):
                num = []
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j] != ".":
                            num.append(board[i][j])
                if len(num) != len(set(num)):
                    return False

        return True                        
