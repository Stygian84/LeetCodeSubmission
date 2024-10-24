class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        #count no of 3consecutive A and B or more
        alice = 0
        bob = 0
        n = len(colors)
        window = deque([])

        for i in range(n):
            if len(window)<3:
                window.append(colors[i])
            else:
                word = "".join(window)
                if word=="AAA":
                    alice+=1
                elif word=="BBB":
                    bob+=1
                window.popleft()
                window.append(colors[i])
        
        word = "".join(window)
        if word=="AAA":
            alice+=1
        elif word=="BBB":
            bob+=1
            
        return alice>bob