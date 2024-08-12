class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        
        def inverse(x):
            for i in range(len(x)):
                if x[i]=="0": x[i]="1"
                else: x[i]="0"
            return x[::-1]

        x = ["0"]
        for _ in range(n):
            x = x + ["1"] + inverse(x)

        return x[k-1]