class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count=0
        
        def isGood(arr,i,j,k,b,c):
            if abs(arr[j]-arr[k])>b:
                return False
            if abs(arr[i]-arr[k])>c:
                return False
            return True
        
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if abs(arr[i]-arr[j])<=a:
                    for k in range(j+1,len(arr)):
                        if isGood(arr,i,j,k,b,c):
                            count+=1
        return count 