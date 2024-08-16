class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        n = len(nums)
        max_num = max(nums)
        freq = [[0] * (max_num + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for num in range(max_num + 1):
                freq[i][num] = freq[i - 1][num]
            freq[i][nums[i - 1]] += 1

        res = []
        for a, b in queries:
            a += 1  
            b += 1
            present = []
            for num in range(max_num + 1):
                if freq[b][num] - freq[a - 1][num] > 0:
                    present.append(num)
            
            if len(present) < 2:
                res.append(-1)
            else:
                min_diff = math.inf
                for i in range(1, len(present)):
                    min_diff = min(min_diff, present[i] - present[i - 1])
                res.append(min_diff)
        
        return res
        '''def getRes(x):
            n=len(x)
            minimum=math.inf
            for i in range(n):
                for j in range(i+1,n):
                    if x[i]!=x[j]:
                        minimum=min(minimum,abs(x[i]-x[j]))
            if minimum==math.inf:
                return -1
            return minimum

        
        res=[]
        for a,b in queries:
            res.append(getRes(nums[a:b+1]))
        
        return res'''