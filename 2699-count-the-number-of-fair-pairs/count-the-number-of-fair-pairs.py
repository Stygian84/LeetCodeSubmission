class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        n = len(nums)
        
        nums.sort()

        #find index of smallest and largest, res += (largest-smallest)
        # bisect

        res = 0
        #print(nums)
        for i in range(n):
            num = nums[i]
            smallest = lower-num
            largest = upper-num
            
            left = bisect.bisect_left(nums,smallest)
            right = bisect.bisect_right(nums,largest)
            #print(left,right)
            if right>i:
                if left>i:
                    res += right-left
                else:
                    res += right-i-1

        return res


        '''n = len(nums)
        ls = []
        for i in range(n):
            ls.append((nums[i],i))
        ls.sort()

        count = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if lower<=ls[i][0]+ls[j][0]<=upper:
                    if ls[i][1]<ls[j][1]:
                        count+=1
                else:
                    break 
        return count'''