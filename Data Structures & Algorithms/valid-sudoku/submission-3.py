class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            sett = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j]  in sett:
                        return False
                    else:
                        sett.add(board[i][j])
        

        for i in range(9):
            sett = set()
            for j in range(9):
                if board[j][i]  != ".":
                    if board[j][i]  in sett:
                        return False
                    else:
                        sett.add(board[j][i] )
        # 1. THE OUTER LOOPS: Pick the top-left corner of one of the 9 boxes
        for box_r in range(0, 9, 3):      # Rows: 0, 3, 6
            for box_c in range(0, 9, 3):  # Cols: 0, 3, 6
                
                # Reset the Hash Set for the new box we are about to scan
                # (Using a Set `set()` is mathematically faster than a List `[]` or Dict `{}`)
                seen = set()
                
                # 2. THE INNER LOOPS: Scan the 3x3 grid inside this specific box
                for i in range(3):        # 0, 1, 2
                    for j in range(3):    # 0, 1, 2
                        
                        # Add the inner offset to the outer anchor point
                        current_val = board[box_r + i][box_c + j]
                        
                        # 3. THE VALIDATION (Don't forget to ignore dots!)
                        if current_val != ".":
                            if current_val in seen:
                                return False
                            seen.add(current_val)
        return True
