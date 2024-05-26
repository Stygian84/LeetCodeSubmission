class Solution:
    def minimumMoves(self, s: str) -> int:
        if "X" not in s:
            return 0
        count=0
        idx=0
        for item in s:
            if idx>0:
                idx-=1
                continue
            if item=="X":
                idx=2
                count+=1
        return count
