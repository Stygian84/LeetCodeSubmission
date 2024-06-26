class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        n=len(s)
        res=[""]*numRows

        curr_row=0
        down=False

        for letter in s:
            res[curr_row]+=letter
            if curr_row==0 or curr_row==numRows-1:
                down = not down

            if down:
                curr_row+=1
            else:
                curr_row-=1
                
        return ''.join(res)
