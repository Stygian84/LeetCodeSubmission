class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)
        dc={}
        for i in range(n//2):
            dc[arr[i]]=dc.get(arr[i],0)+1
            dc[arr[-i-1]]=dc.get(arr[-i-1],0)+1
            if dc[arr[i]]>(n//4):
                return arr[i]
            if dc[arr[-i-1]]>(n//4):
                return arr[-i-1]
        return arr[0]