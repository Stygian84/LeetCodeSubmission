class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        a,b=0,0 #keep track of o and x
        winA,winB = False,False

        diagonal = []
        diagonal2 = []
        for i in range(3):
            row = board[i]
            if row == "XXX":
                winB=True
            elif row == "OOO":
                winA=True

            column = []

            for j in range(3):
                item = row[j]
                column.append(board[j][i])
                if item == "O":
                    a+=1
                elif item == "X":
                    b+=1
                if i==j:
                    diagonal.append(item)
                if i+j==2:
                    diagonal2.append(item)

            if column == ["X","X","X"]:
                winB = True
            elif column == ["O","O","O"]:
                winA = True

        if diagonal == ["X","X","X"] or diagonal2 == ["X","X","X"]:
            winB = True
        if diagonal == ["O","O","O"] or diagonal2 == ["O","O","O"]:
            winA = True
        
        if winA and winB:
            return False
        if winB and b<=a:
            return False
        if winA and a<b:
            return False
        if b-a!=1 and b-a!=0:
            return False
        return True