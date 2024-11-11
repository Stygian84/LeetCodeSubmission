class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        def isPrime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        def pickPrime(target,current):
            if target>=current:
                return -1
            diff = current-target
            for num in range(diff,-1,-1):
                if isPrime(num):
                    return current-num

            return -1
        

        for i in range(len(nums)):
            if i == 0:
                new_num = pickPrime(1, nums[i])
                if new_num != -1:
                    nums[i] = new_num
            else:
                new_num = pickPrime(nums[i-1]+1, nums[i])
                if new_num != -1:
                    nums[i] = new_num
            
                if nums[i]<=nums[i-1]:
                    return False
        return True