class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def check (a):
            i,j=0,0
            while i <len(s) and j<len(a):
                if s[i]!=a[j]:
                    return False

                length_s=1
                length_a=1

                while i+1<len(s) and s[i]==s[i+1]:
                    i+=1
                    length_s+=1
                while j+1<len(a) and a[j]==a[j+1]:
                    j+=1
                    length_a+=1
                if length_s<3 and length_a!=length_s:
                    return False
                if length_a > length_s:
                    return False
                #move to next letter
                i+=1
                j+=1
            return i==len(s) and j==len(a)
                

        count=0
        for item in words:
            if check(item):
                count+=1
        return count