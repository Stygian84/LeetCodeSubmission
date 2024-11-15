class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        prefix = []
        suffix = []

        for i in range(n):
            if not prefix or arr[i]>=prefix[-1]:
                prefix.append(arr[i])
            else:
                break
        
        for j in range(n-1,i,-1):
            if not suffix or arr[j]<=suffix[-1]:
                suffix.append(arr[j])
            else:
                break
        
        if not suffix:
            return n-len(prefix)
        if not prefix:
            return n-len(suffix)

        suffix.reverse()

        res = min(n-len(suffix),n-len(prefix))

        for i in range(len(prefix)):
            j = bisect.bisect_left(suffix,prefix[i]) 
            res = min(res, n - (i+1) - (len(suffix)-j))
                
        return res

