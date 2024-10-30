class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        ls_n = list(str(n))
        length = len(ls_n)

        pointer = length
        for i in range(length-1,0,-1):
            if ls_n[i]<ls_n[i-1]:
                pointer = i
                ls_n[i-1] = str(int(ls_n[i-1])-1)
        
        for i in range(pointer,length):
            ls_n[i]="9"
        return int("".join(ls_n))