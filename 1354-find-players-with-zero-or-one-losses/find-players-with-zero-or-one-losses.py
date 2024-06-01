class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player=set()
        lost={}
        for item in matches:
            winner=item[0]
            loser=item[1]
            player.add(winner)
            lost[loser]=lost.get(loser,0)+1
        one_match=[]
        for key,values in lost.items():
            player.discard(key)
            if values==1:
                one_match.append(key)
        one_match.sort()

        all_match=list(player)
        all_match.sort()

        return [all_match,one_match]