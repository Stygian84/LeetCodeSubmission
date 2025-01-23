class Solution:
    def calculateScore(self, s: str) -> int:
        
        def reverse(x):
            if x<"m":
                return chr(ord('z')-((ord(x)-ord('a'))))
            else:
                return chr(ord('a')+((ord('z')-ord(x))))
        score = 0

        n = len(s)

        index = defaultdict(list)

        for i in range(n):
            letter = s[i]
            mirror = reverse(letter)
            if mirror in index and len(index[mirror])>0:
                score += i-index[mirror].pop()
            else:
                index[letter].append(i)
        
        return score