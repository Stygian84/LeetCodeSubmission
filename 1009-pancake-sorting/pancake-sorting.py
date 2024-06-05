class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res=[]
        n=len(arr)
        def flip(arr,k):
            arr=arr[:k][::-1]+arr[k:]
            return arr
        for i in range(n):
            max_idx=arr.index(max(arr[:n-i]))
            res.append(max_idx+1)
            arr=flip(arr,max_idx+1)
            res.append(n-i)
            arr=flip(arr,len(arr[:n-i]))
        return res
