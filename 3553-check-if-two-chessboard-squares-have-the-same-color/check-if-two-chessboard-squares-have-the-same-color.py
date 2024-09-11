class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        
        letterA=coordinate1[0]
        letterB=coordinate2[0]

        numA=int(coordinate1[1])
        numB=int(coordinate2[1])

        if (ord(letterB)-ord(letterA))%2==0:
            return numA%2==numB%2
        else:
            return numA%2!=numB%2