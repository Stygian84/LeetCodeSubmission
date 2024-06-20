class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        #def valid(a,b,c):
        #    return a+b>c and a+c>b and b+c>a
        n=len(nums)
        nums.sort()
        count=0
        for i in range(n-1,1,-1):
            a,b=0,i-1
            while a<b:
                if nums[a]+nums[b]>nums[i]:
                    count+=b-a
                    b-=1
                else:
                    a+=1
        return count
