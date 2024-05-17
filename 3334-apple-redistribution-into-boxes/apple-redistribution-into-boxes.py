class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples=sum(apple)
        new_cap=sorted(capacity, reverse=True)
        count=0
        for item in new_cap:
            apples-=item
            count+=1
            if apples<=0:
                break
        return count
        