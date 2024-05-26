class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res=[words[0]]
        prev_bit=groups[0]
        
        for idx in range(len(groups)):
            if prev_bit!=groups[idx]:
                res.append(words[idx])
                prev_bit=groups[idx]
        return res