class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        num=numsDivide[0]

        for i in range(1,len(numsDivide)):
            num=math.gcd(num,numsDivide[i])
            
        nums.sort()
        for i, val in enumerate(nums):
            if num % val == 0:
                return i
        return -1
        '''s=set()

        heapq.heapify(nums)
        count=0

        while nums:
            smallest = heapq.heappop(nums)
            
            if smallest in s:
                count+=1
                continue
            else:
                for num in numsDivide:
                    if num%smallest!=0:
                        count+=1
                        break
                else:
                    return count
            s.add(smallest)

        if nums:
            return count
        return -1'''