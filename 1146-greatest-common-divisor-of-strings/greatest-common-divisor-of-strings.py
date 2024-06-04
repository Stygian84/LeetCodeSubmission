class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ""
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        length_gcd = gcd(len(str1), len(str2))
        
        return str1[:length_gcd]