class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        count = 1
        original = a[:]

        if len(b)<len(a):
            if b in a:
                return 1
            a+=original
            if b in a:
                return 2
            else:
                return -1

        while b not in a:
            if len(a)>=len(b)*2:
                return -1
            a = a+original
            count += 1
        
        return count