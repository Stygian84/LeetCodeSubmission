class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        diff = defaultdict(int)

        for t in tasks:
            diff[t]+=1
        
        res = 0
        for v in diff.values():
            if v==1:
                return -1
            # 7 -> 3 3 1 invalid
            # 7 -> 2 2 3 valid
            # 5 -> 2 3
            # 6 -> 3 3
            res += math.ceil(v/3)
        
        return res