class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks=sorted(score, reverse=True)
        result=[]
        for item in score:
            rank = ranks.index(item)+1
            if rank == 1:
                result.append("Gold Medal")
            elif rank == 2:
                result.append("Silver Medal")
            elif rank == 3:
                result.append("Bronze Medal")
            else:
                result.append(f"{rank}")
        return result