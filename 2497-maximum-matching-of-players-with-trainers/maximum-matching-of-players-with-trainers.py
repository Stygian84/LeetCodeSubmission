class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        count=0

        n=len(trainers)
        m=len(players)

        i,j=0,0
        while i<m and j<n:
            if trainers[j]>=players[i]:
                j+=1
                i+=1
                count+=1
                continue
            else:
                j+=1
        return count
        '''trainers.sort()
        players.sort()

        count=0
        n=len(trainers)
        idx=0
        for i in range(len(players)):
            for j in range(idx,n):
                if trainers[j]>=players[i]:
                    idx=j+1
                    count+=1
                    break
                
        return count'''