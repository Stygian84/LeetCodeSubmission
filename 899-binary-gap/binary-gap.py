class Solution:
    def binaryGap(self, n: int) -> int:
        
        binary=bin(n)[2:]

        first_idx=None
        second_idx=None
        longest_dist=0
        for i in range(len(binary)):
            digit=binary[i]
            if digit=="1":
                if first_idx==None:
                    first_idx=i
                else:
                    second_idx=i
                    longest_dist=max(longest_dist,second_idx-first_idx)
                    first_idx=second_idx
        return longest_dist