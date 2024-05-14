class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words=0
        for item in sentences:
            length=len(item.split())
            if length>max_words:
                max_words=length
        return max_words
        