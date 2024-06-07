class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square=[[0]*9]
        def isValid(ls):
            dc={}
            for item in ls:
                if item!=".":
                    dc[item]=dc.get(item,0)+1
                    if dc[item]>1:
                        return False
            return True
        def generate_square(x_offset,y_offset,board):
            square=[]
            for i in range(3):
                for j in range(3):
                    square.append(board[i+x_offset][j+y_offset])
            return square

        for i in range(9):
            if isValid(board[i])==False:
                return False
            ls=[] #check column
            for j in range(9):
                if board[j][i]!=".":
                    ls.append(board[j][i])
            if isValid(ls)==False:
                return False

            
        for i in range(0,9,3):
            for j in range(0,9,3):
                square=generate_square(i,j,board)
                if isValid(square)==False:
                        return False
        return True

        '''for i in range(9):
            for row in board[i]:
                row_content=[]
                for item in row:
                    if item!=".":
                        row_content.append(item)
                set_row=set(row_content)
                if(len(row_content)!=len(set_row)):
                    return False

            
            column_content=[]
            for row in range(9):
                if board[row][i]!=".":
                    column_content.append(board[row][i])
            set_column=set(column_content)

            if(len(column_content)!=len(set_column)):
                    return False
        return True'''