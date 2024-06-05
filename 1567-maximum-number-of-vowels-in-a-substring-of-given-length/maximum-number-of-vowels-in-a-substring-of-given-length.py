from collections import deque
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowel=0
        current_string=deque([])
        current_count=0
        vowels="aeiou"
        for i in range(len(s)):
            
            if len(current_string)==k:
                max_vowel=max(max_vowel,current_count)
                if current_string.popleft() in vowels:
                    current_count-=1
            if s[i] in vowels:
                current_count+=1
            current_string.append(s[i])
        if len(current_string)==k:
            max_vowel=max(max_vowel,current_count)
            if current_string.popleft() in vowels:
                current_count-=1
        return max_vowel