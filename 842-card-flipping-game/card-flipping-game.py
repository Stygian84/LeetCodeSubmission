class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        # get the smallest number on either front or backs
        # if 1 card has that number, its invalid
        # if no answer return 0
        res = math.inf
        duplicates = set()

        for a,b in zip(fronts,backs):
            if a==b:
                duplicates.add(a)
        
        for a,b in zip(fronts,backs):
            if a!=b:
                if a not in duplicates and a<res:
                    res = a
                if b not in duplicates and b<res:
                    res = b


        if res==math.inf:
            return 0
        return res