class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # use 3 hashmap 
        rows, cols, box = {}, {}, {}
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                rowVal = "Row " + str(r) + " has " + board[r][c] 
                colVal = "Col " + str(c) + " has " + board[r][c] 
                boxVal = "Box row: " + str(r//3)  + " col: " + str(c//3) + "has " + board[r][c]
                if rowVal in rows or colVal in cols or boxVal in box:
                    return False
                rows[rowVal] = True
                cols[colVal] = True
                box[boxVal] = True
        return True 