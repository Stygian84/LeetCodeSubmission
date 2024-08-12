class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        i = 0 
        j = 1
        n = len(arr)
        if k>=n:
            return max(arr)

        count = 0
        while i<n:
            #compare
            if arr[i]>arr[j]: # win
                count+=1
                j+=1 #next challenger
            
            else: # lose
                count=1
                i=j
                j=i+1
        
            if j==n:
                j=0
            if j==i:
                j+=1

            if count == k:
                return arr[i]
        return arr[i]