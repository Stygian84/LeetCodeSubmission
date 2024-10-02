class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        res = 0

        ls = [] 
        for d,s in zip(dist,speed):
            ls.append((d/s))
        ls.sort(reverse=True)

        for i in range(len(dist)):
            t = ls.pop()
            if t>i:
                res+=1
            else:
                break
                
        return res