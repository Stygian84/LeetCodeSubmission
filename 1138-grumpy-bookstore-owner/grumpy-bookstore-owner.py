class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        if minutes==len(customers):
            return sum(customers)
        zero=0
        ls=deque([])
        bonus=0
        max_bonus=0

        for c,g in zip(customers,grumpy):
            if g==0:
                zero+=c
            else:
                bonus+=c

            if len(ls)==minutes:
                removed=ls.popleft()
                if removed[1]==1:
                    bonus-=removed[0]
            ls.append([c,g])
            max_bonus=max(max_bonus,bonus)
            
        if len(ls)==minutes:
            max_bonus=max(max_bonus,bonus)

        return zero+max_bonus
