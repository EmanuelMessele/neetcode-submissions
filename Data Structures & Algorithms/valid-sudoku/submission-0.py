class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we are given a list of list 9x9 sudoku
        # we must confirm it is a valid suduku board
            # 1 - 9 rows
            # 1- 9 colums
            # 1- 9 boxes

        # implemenation: 
            # make a library for each ---> rows, cols, 3x3 boxes
            # for rows and cols --> the key will be each row or col
            # for 3x3 boxes, we can turn our 3x3 box into one line and make it part of our dictionary
            # using duplicates we can tell whether their is a duplicate number in the values within our dictionary
            
            for row in range(9):
                seen = set()
                for j in range(9):
                    if not board[row][j] == ".":
                        if board[row][j] in seen:
                            return False
                        else:
                            seen.add(board[row][j])

            for col in range(9):
                seen = set()
                for i in range(9):
                    if not board[i][col] == ".":
                        if board[i][col] in seen:
                            return False
                        else:
                            seen.add(board[i][col])

            for square in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        row = (square // 3) * 3 + i # 0 0 0, 1 1 1, 2 2 2 ----> 0
                        col = (square % 3) * 3 + j # 0 1 2, 0 1 2, 0 1 2 ----> 3
                        if not board[row][col] == ".":
                            if board[row][col] in seen:
                                return False
                            else:
                                seen.add(board[row][col])

            return True
               
            

                
        