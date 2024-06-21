class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary=bin(n)[2:]

        prev=None
        for item in binary:
            if item==prev:
                return False
            prev=item

        return True