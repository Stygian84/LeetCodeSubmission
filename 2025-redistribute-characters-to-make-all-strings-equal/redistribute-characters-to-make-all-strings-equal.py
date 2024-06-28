class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dc=defaultdict(int)
        for word in words:
            for letter in word:
                dc[letter]+=1

        n=len(words)
        for value in dc.values():
            if value%n!=0:
                return False
        return True