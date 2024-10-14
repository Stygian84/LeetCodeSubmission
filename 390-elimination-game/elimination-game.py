class Solution:
    def lastRemaining(self, n: int) -> int:
        
        
        #flag = 0 , move forward
        # +1 (0), +2(1), +4(0), +8(1)
        res = 1
        step = 1
        flag = 0

        while n>1:
            if not flag or n%2==1:
                res+=step
            step*=2
            n//=2
            flag ^= 1

        return res
        '''if n==1:
            return 1
        temp = [i for i in range(1,n+1)]

        # take odd idx , then even idx
        #flag = 1 odd idx, flag = 0 even idx
        res = []
        def recurse(arr,flag):
            if len(arr)==1:
                return arr[0]
            arr = [ arr[i] for i in range(len(arr)) if i%2==flag  ]
            return recurse(arr,flag^1)

        return recurse(temp,1)'''


        '''if n==1:
            return 1

        initial = [i for i in range(1,n+1)]

        def forward(arr):
            res = []
            for i in range(1,len(arr),2):
                res.append(arr[i])
            return res
        def backward(arr):
            res = []
            for i in range(len(arr)-2,-1,-2):
                res.append(arr[i])
            return res[::-1]
        

        while len(initial)>1:
            initial = forward(initial)
            #print(initial)
            if len(initial)==1:
                return initial[0]
            initial = backward(initial)
            #print(initial)
            if len(initial)==1:
                return initial[0]'''