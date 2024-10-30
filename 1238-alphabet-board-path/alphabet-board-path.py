class Solution:
    def alphabetBoardPath(self, target: str) -> str:

        # check if go down to 'z' is not out of boundary / if go up from z
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        n = len(board)
        m = len(board[0])

        location = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                location[board[i][j]]=(i,j)
        
        res = []
        start = (0,0)
        for letter in target:
            position = location[letter]
            if start == position:
                res.append("!")
                continue
            rows = position[0]-start[0]
            cols = position[1]-start[1]
            
            if letter=="z":
                if cols>0:
                    res.append("R"*cols)
                elif cols<0:
                    res.append("L"*(-cols))

                if rows>0:
                    res.append("D"*rows)
                elif rows<0:
                    res.append("U"*(-rows))

            else:
                if rows>0:
                    res.append("D"*rows)
                elif rows<0:
                    res.append("U"*(-rows))

                if cols>0:
                    res.append("R"*cols)
                elif cols<0:
                    res.append("L"*(-cols))

            res.append("!")
            
            start = position
        
        return "".join(res)