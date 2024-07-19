class Solution:
    def largestInteger(self, num: int) -> int:
        odd=[]
        odd_idx=[]
        even=[]
        even_idx=[]
        num=str(num)
        for idx,digit in enumerate(num):
            if int(digit)%2==0:
                even.append(digit)
                even_idx.append(idx)
            else:
                odd.append(digit)
                odd_idx.append(idx)
                
        even.sort(reverse=True)
        odd.sort(reverse=True)
        even_idx.sort()
        odd_idx.sort()
        
        ls=[""]*len(num)
        for digit,idx in zip(even,even_idx):
            ls[idx] = digit
        for digit,idx in zip(odd,odd_idx):
            ls[idx] = digit
        
        return int("".join(ls))