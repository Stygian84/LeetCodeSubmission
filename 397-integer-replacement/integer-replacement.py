class Solution:
    def integerReplacement(self, n: int) -> int:
        count=0
        while n>1:
            if n%2==0:
                n//=2
            else:
                if n == 3 or (n % 4 == 1):
                    n -= 1
                else:
                    n += 1
            count+=1
        return count
        '''if n==1:
            return 0
        count=1
        x=2
        while x<n:
            count+=1
            x*=2
            print(x,n,count)
        count+= min(x-n,n-x/2)
        return count'''