class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        vowel="aeiou"
        n=len(word)

        res=0
        i=0
        while i < n:
            if word[i] not in vowel:
                i += 1
                continue
            else:
                j = i
                dc2 = defaultdict(int)
                while j < n and word[j] in vowel:
                    dc2[word[j]] += 1
                    if all(dc2[v] > 0 for v in vowel):
                        res += 1
                    j += 1
                
                i += 1
        return res