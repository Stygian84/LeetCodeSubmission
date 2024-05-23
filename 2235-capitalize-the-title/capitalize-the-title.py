class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ls=title.split()
        for idx in range(len(ls)):
            ls[idx]=ls[idx].lower()
            if len(ls[idx])>2:
                ls[idx]=ls[idx].capitalize()
        return " ".join(ls)
        