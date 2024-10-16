class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        res = []
        
        # add previous shifts
        for i in range(len(shifts)-2,-1,-1):
            shifts[i]+=shifts[i+1]
        
        #print(shifts)
        for letter,shift in zip(s,shifts):
            new_ascii = ord(letter)+shift%26
            if new_ascii > ord('z'):
                new_letter = chr(new_ascii-ord('z')+ord('a')-1)
            else:
                new_letter = chr(new_ascii)
            res.append(new_letter)

        
        return "".join(res)