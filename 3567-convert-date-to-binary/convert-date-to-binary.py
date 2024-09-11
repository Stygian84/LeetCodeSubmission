class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ls = date.split("-")

        for i in range(len(ls)):
            ls[i]=bin(int(ls[i]))[2:]
        
        return "-".join(ls)