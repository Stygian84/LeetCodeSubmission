class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i=0
        j=0
        n=len(name)
        m=len(typed)

        if n>m:
            return False

        while i<n and j<m:
            countA=0
            countB=0
            if name[i]==typed[j]:
                while i<n-1 and name[i]==name[i+1]:
                    countA+=1
                    i+=1
                while j<m-1 and typed[j]==typed[j+1]:
                    countB+=1
                    j+=1
                if countA>countB:
                    return False
                i+=1
                j+=1
            else:
                return False
        if i < n:
            return False
        while j < m:
            if typed[j] != name[-1]:
                return False
            j += 1
        return True