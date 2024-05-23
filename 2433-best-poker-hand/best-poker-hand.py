class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits))==1:
            return "Flush"
        dc={}
        pair=False
        three=False
        for item in ranks:
            dc[item]=dc.get(item,0)+1
        for values in dc.values():
            if values>=3:
                three=True
            if values==2:
                pair=True
        if three:
            return "Three of a Kind"
        if pair:
            return "Pair"
        else:
            return "High Card"
        