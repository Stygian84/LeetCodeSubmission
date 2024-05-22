class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        count=0
        initCapacityA=capacityA
        initCapacityB=capacityB
        for idx in range(len(plants)//2):
            if capacityA<plants[idx]:
                count+=1
                capacityA=initCapacityA-plants[idx]
            else:
                capacityA-=plants[idx]
            if capacityB<plants[-(idx+1)]:
                count+=1
                capacityB=initCapacityB-plants[-(idx+1)]
            else:
                capacityB-=plants[-(idx+1)]
        if len(plants)%2==1 and len(plants)>1:
            index=len(plants)//2
            if capacityA>capacityB:
                if capacityA<plants[index]:
                    count+=1
            else:
                if capacityB<plants[index]:
                    count+=1

        return count