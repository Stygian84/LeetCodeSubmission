class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        crashTime=0
        time=0

        memory = [memory1,memory2]
        bits = 1
        while memory[0]-bits>=0 or memory[1]-bits>=0:
            if memory[0]>=memory[1]:
                memory[0]-=bits
            else:
                memory[1]-=bits
            time+=1
            bits+=1

        return [time+1] + memory

            