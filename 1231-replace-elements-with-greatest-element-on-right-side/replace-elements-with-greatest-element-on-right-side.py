class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ls=[-1]*len(arr)
        a=copy.deepcopy(arr)
        a.sort()
        for i in range(len(arr)-1):
            a.remove(arr[i])
            ls[i]=a[-1]
        return ls