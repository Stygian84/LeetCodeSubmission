class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n=="0":
            return "1"
        if len(n)==1:
            return str(int(n)-1)
        
        length = len(n)
        candidates = set()
        
        prefix = n[:(length + 1) // 2]
        candidate1 = prefix + prefix[:-1][::-1] if length % 2 else prefix + prefix[::-1]
        candidates.add(candidate1)
        
        prefix = str(int(prefix) + 1)
        candidate2 = prefix + prefix[:-1][::-1] if length % 2 else prefix + prefix[::-1]
        candidates.add(candidate2)
        
        prefix = str(int(prefix) - 2)
        candidate3 = prefix + prefix[:-1][::-1] if length % 2 else prefix + prefix[::-1]
        candidates.add(candidate3)
        
        candidates.add("9" * (length - 1))
        candidates.add("1" + "0" * (length - 1) + "1")
        
        candidates.discard(n)
        return min(candidates, key = lambda x : (abs(int(x) - int(n)), int(x)))