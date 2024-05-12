class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ls=[0]*len(s)
        for i in range(len(indices)):
            ls[indices[i]]=s[i]
        return "".join(ls)