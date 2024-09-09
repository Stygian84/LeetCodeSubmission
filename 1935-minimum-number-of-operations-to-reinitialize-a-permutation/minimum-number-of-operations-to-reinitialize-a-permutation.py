class Solution:
    def reinitializePermutation(self, n: int) -> int:
        pos = 1
        count = 0

        while True:
            if pos%2==0:
                pos//=2
            else:
                pos = n//2 + (pos-1)//2
            
            count+=1

            if pos==1:
                return count
        '''arr = [0] * n

        perm = [i for i in range(n)]
        original = perm[:]
        
        count = 0

        while True:
            if count!=0:
                if perm==original:
                    return count
            
            for i in range(n):
                if i%2==0:
                    arr[i] = perm[i//2]
                else:
                    arr[i] = perm[n//2+(i-1)//2]
            perm = arr[:]
            count+=1'''
        
        
                    