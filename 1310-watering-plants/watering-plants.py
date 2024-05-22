class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        total=0
        init_capacity=capacity
        for idx in range(len(plants)):
            if capacity<plants[idx]:
                capacity=init_capacity
                total+=2*idx
            total+=1
            capacity-=plants[idx]
        return total