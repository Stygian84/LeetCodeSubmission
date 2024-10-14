class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        # dont remove bar 1 and n+2 and m+2
        #n ->hBars
        hBars.sort()
        vBars.sort()
        def maxLength(arr):
            count = 0
            max_length = 0
            for i in range(1,len(arr)):
                if arr[i]-arr[i-1]==1:
                    count+=1
                else:
                    max_length=max(max_length,count)
                    count=0
                    
            max_length=max(max_length,count)
            return max_length
        
        l1=maxLength(hBars)
        l2=maxLength(vBars)

        return (min(l1+2,l2+2))**2