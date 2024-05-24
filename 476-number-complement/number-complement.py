class Solution:
    def findComplement(self, num: int) -> int:
        length=len(bin(num))-2
        binary=(1<<length)-1
        return num^binary



        