class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ls=[]
        count=0
        for idx in range(len(board)):
            for i in range(len(board[idx])):
                item=board[idx][i]
                if item=="X":
                    count+=1
                    ls.append([idx,i])
                    if [idx-1,i] in ls:
                        count-=1
                        continue
                    if [idx,i-1] in ls:
                        count-=1
                        continue
        return count