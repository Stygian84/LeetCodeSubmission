class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count=0
        candies = n
        for i in range(limit+1):
            a = n-i

            for j in range(limit+1):
                b = a-j

                for k in range(limit+1):
                    c = b-k
                    if c==0:
                        count+=1

        return count