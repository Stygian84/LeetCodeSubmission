class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Y = comes at ith hour
        # N = no customers

        n = len(customers)

        Y = customers.count("Y")
        N = 0

        res = n
        current_penalty = math.inf

        for i in range(n):
            penalty = Y + N
            if penalty < current_penalty:
                res = i
                current_penalty = penalty

            if customers[i]=="Y":
                Y-=1
            elif customers[i]=="N":
                N+=1
        
        penalty = Y + N
        if penalty < current_penalty:
            res = n
            
        return res