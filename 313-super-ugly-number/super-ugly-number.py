class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        res=[0]*(n)
        res[0]=1
        
        dc = {prime: 0 for prime in primes}

        i=1
        while i<n:
            next_ugly=None
            min_value=math.inf

            for prime in primes:
                current_value = res[dc[prime]] * prime
                if current_value < min_value:
                    min_value = current_value
                    next_ugly = prime
                    
            if min_value==res[i-1]:
                dc[next_ugly] += 1
                continue
            res[i] = min_value
            
            dc[next_ugly] += 1
            i+=1

        return res[-1]