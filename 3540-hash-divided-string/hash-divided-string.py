class Solution:
    def stringHash(self, s: str, k: int) -> str:
        def hashing(x):
            total = 0
            for letter in x:
                total+=ord(letter)-ord('a')
            
            total%=26
            return chr(total+ord('a'))

        result = []
        n = len(s)

        for i in range(0,n,k):
            result.append(hashing(s[i:i+k]))
        
        
        return "".join(result)