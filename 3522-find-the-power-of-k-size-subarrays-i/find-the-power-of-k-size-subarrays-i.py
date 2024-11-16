class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        windows = deque([])
        n = len(nums)

        res = []
        
        for i in range(n):
            #check
            if len(windows)<k:
                windows.append(nums[i])
            else:            
                for j in range(1,len(windows)):
                    if windows[j]-windows[j-1]!=1:
                        res.append(-1)
                        break
                else:
                    res.append(windows[-1])
                windows.append(nums[i])
                windows.popleft()

        for j in range(1,len(windows)):
            if windows[j]-windows[j-1]!=1:
                res.append(-1)
                break
        else:
            res.append(windows[-1])
        return res
            