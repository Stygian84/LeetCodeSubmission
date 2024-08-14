class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        
        count = 0
        current = 1
        flag = None
        increasing = False

        for i in range(1,n):
            current+=1
            
            if arr[i]>arr[i-1]:#increasing
                increasing = True
                if flag == False:
                    current=2
                flag = True

            elif arr[i]<arr[i-1]: #decreasing
                if flag == None:
                    current = 1
                flag = False

            else:
                current = 1
                flag = None

            if increasing and flag == False:
                count = max(count,current)
 

       
        if count<3:
            return 0
        return count