class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        s1 = ""        
        total = 0
        #convert
        for letter in s:
            s1+=str(ord(letter)-ord('a')+1)
        
        #transform 1
        for digit in s1:
            total+=int(digit)
        if k==1:
            return total
        k-=1

        #transform k-1
        for _ in range(k):
            temp = 0
            for digit in str(total):
                temp+=int(digit)
            total = temp

        return total