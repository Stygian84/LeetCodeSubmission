class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        total = 1
        print(pairs)
        current = pairs[0]
        for c,d in pairs[1:]:
            a,b = current
            if d<b and c>a:
                current = [c,d]
                continue
            if a==c:
                continue
            if c>b:
                current = [c,d]
                total+=1
            
        return total
    