class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result=[]
        for idx in range(len(words)):
            if x in words[idx]:
                result.append(idx)
        return result
        