class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score=0
        if len(tokens)==1 and power<tokens[0]:
            return 0
        tokens.sort()
        i=0
        j=len(tokens)-1
        while i<=j:
            if tokens[i]<=power:
                power-=tokens[i]
                i+=1
                score+=1
            else:
                if j-i>1 and score>=1:
                    power+=tokens[j]
                    j-=1
                    score-=1
                else:
                    break
        return score