class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        current_time = customers[0][0]
        
        total_waiting_time = 0 
        n = len(customers)

        for c in customers:
            if c[0] >= current_time:
                current_time = c[0] + c[1]
            else:
                current_time += c[1]
            total_waiting_time += current_time - c[0] 

        return total_waiting_time / n