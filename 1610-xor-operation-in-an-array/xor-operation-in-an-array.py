class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result=start
        for i in range(2,2*n,2):
            result^=start+i
        return result

        