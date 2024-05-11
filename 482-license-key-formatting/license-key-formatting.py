class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace("-","")
        s=s[::-1]
        str1=""
        for idx in range(len(s)):
            if (idx)%k==0:
                str1+="-"
                str1+=s[idx].upper()
            else:
                str1+=s[idx].upper()
        return str1[1:][::-1]
            