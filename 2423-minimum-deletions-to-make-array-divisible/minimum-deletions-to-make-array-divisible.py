class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        s=set()

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
        return -1