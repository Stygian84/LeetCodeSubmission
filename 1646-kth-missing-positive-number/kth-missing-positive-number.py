class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ls=[]
        for i in range(1,len(arr)+k+1):
            if i in arr:
                continue
            else:
                ls.append(i)
        return ls[k-1]
        