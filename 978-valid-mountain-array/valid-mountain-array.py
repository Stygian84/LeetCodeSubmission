class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        state=None
        count=0
        for idx in range(len(arr)-1):
            if count>2:
                return False
            if arr[idx+1]>arr[idx]:
                if state==None or state==False:
                    state=True
                    count+=1
                    continue
            elif arr[idx+1]<arr[idx]:
                if state==None:
                    return False
                if state:
                    state=False
                    count+=1
                    continue
            else:
                return False
            print(count)
        if state:
            return False
        return True