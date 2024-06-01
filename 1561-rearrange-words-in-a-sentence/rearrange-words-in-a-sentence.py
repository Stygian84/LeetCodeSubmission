class Solution:
    def arrangeWords(self, text: str) -> str:
        ls=text.lower().split()

        ls2 = sorted(ls, key=lambda item: len(item))
        return " ".join(ls2).capitalize()