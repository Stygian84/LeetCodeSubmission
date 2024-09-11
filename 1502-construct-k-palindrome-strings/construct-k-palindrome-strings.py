class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)==k:
            return True
        if len(s)<k:
            return False

        freq = Counter(s)

        count = 0
        for v in freq.values():
            if v%2==1:
                count+=1
        if count>k:
            return False
        return True