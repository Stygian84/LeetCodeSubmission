class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        queue = deque(i for i in range(1,n+1))
        start=-1
        while len(queue)>1:
            start+=k
            if start>n-1:
                start = start%n
            del queue[start]
            start-=1
            n-=1

        return queue.pop()

            
            
        