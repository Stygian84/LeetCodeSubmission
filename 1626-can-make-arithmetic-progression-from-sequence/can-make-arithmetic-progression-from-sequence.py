class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff=arr[1]-arr[0]
        for idx in range(1,len(arr)-1):
            if arr[idx+1]-arr[idx]==diff:
                continue
            else:
                return False
        return True