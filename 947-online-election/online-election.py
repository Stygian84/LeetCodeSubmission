class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        #keep track which has the max votes at which time then store it
        self.votes = defaultdict(int)
        winner = persons[0]
        max_vote = -1

        self.history = defaultdict(int)
        self.history[0] = winner

        for candidate, time in zip(persons,times):
            self.votes[candidate]+=1
            if self.votes[candidate] >= max_vote:
                max_vote = self.votes[candidate]
                winner = candidate
            self.history[time] = winner        

        self.last = time
        #print(self.history)


    def q(self, t: int) -> int:
        if t >= self.last:
            return self.history[self.last]

        if t in self.history:
            return self.history[t]
        
        else:
        
            while t not in self.history:
                t-=1
            return self.history[t]
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)