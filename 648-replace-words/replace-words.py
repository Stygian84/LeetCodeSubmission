class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ls=sentence.split()
        dictionary.sort()
        for i in range(len(ls)):
            for j in dictionary:
                if ls[i].startswith(j):
                    ls[i]=j
                    break
        return " ".join(ls)
        