import heapq
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        while 0 in amount:
            amount.remove(0)
        count=0
        while len(amount)>=2:
            biggest=max(amount)-1
            smallest=min(amount)-1
            amount.remove(biggest+1)
            amount.remove(smallest+1)
            if smallest > 0:
                amount.append(smallest)
            if biggest > 0:
                amount.append(biggest)
            count += 1
        if amount:
            return count+amount[0]
        else:
            return count