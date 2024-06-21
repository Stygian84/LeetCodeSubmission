class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        one=[]
        for i in range(len(mat)):
            row=mat[i]
            one.append((row.count(1),i))
        one.sort()
        res=[]
        for i in range(k):
            res.append(one[i][-1])
        return res