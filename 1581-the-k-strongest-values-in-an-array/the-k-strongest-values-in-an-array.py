class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        def findMedian(arr):
            return arr[(len(arr)-1)//2]
        
        sorted_arr=sorted(arr)
        median=findMedian(sorted_arr)
        
        def sort_key(x):
            return (abs(x - median), x)
        res = sorted(sorted_arr, key=sort_key, reverse=True)
        
        return res[:k]