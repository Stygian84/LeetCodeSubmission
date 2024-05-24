class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook=[]
        pawn=[]
        for i in range(8):
            for j in range(8):
                location=[i,j]
                ele=board[i][j]
                if ele=="R":
                    rook.append(location)
                elif ele=="p":
                    pawn.append(location)
        rook_x=rook[0][0]
        rook_y=rook[0][1]
        count = 0
        for pawn_x, pawn_y in pawn:
            if pawn_x == rook_x:
                start, end = min(rook_y, pawn_y), max(rook_y, pawn_y)
                if all(board[pawn_x][i] == "." for i in range(start + 1, end)):
                    count += 1
            elif pawn_y == rook_y:
                start, end = min(rook_x, pawn_x), max(rook_x, pawn_x)
                if all(board[i][rook_y] == "." for i in range(start + 1, end)):
                    count += 1
        return count