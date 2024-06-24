class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(a,b):
            while b != 0:
                a, b = b, a % b
            return a
        
        count=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if gcd(int(str(nums[i])[0]),int(str(nums[j])[-1]))==1:
                    count+=1
        return count
