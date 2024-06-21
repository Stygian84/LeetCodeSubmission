class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res=[]
        min_diff=math.inf
        for i in range(len(arr)-1):
            j=i+1
            diff=arr[j]-arr[i]
            if diff<min_diff:
                res=[[arr[i],arr[j]]]
                min_diff=diff
            elif diff==min_diff:
                res.append([arr[i],arr[j]])
        return res