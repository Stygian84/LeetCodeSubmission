class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n=len(deck)
        res=[]
        while len(res)<n-1:
            res.insert(0,deck.pop())
            length=len(res)
            res[:]=[res[-1]]+res[:length-1]
        res.insert(0,deck.pop())
        return res
