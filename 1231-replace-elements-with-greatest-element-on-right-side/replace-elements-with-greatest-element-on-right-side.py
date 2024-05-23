class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]
        for i in range(len(arr)-1,0,-1):
            res.append(max(res[-1],arr[i]))
        return res[::-1]