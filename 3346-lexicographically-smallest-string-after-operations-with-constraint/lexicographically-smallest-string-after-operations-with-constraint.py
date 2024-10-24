class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        # make each letter as small as possible starting from left

        ls = list(s)

        for i in range(len(ls)):
            letter = ls[i]

            #check if getting to a is faster from front or back
            
            diff = min(ord(letter)-ord('a'), ord('z')-ord(letter)+1) 
            if k-diff<0:
                ls[i] = chr(ord(letter) - k)
            else:
                ls[i] = 'a'

            k-=diff
            if k <= 0:
                break

        return "".join(ls)