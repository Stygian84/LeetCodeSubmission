class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        n = len(code)

        if k==0:
            return [0]*n

        window = deque([])
        res = []
        total = 0
        code += code

        if k > 0:
            for i in range(2*n):
                if len(window)<k:
                    window.append(code[i])
                    total += code[i]
                else:
                    total -= window.popleft()
                    window.append(code[i])
                    total += code[i]
                    res.append(total)
            return res[:n]

        else:
            k = abs(k)
            code.reverse()
            for i in range(2*n):
                if len(window)<k:
                    window.append(code[i])
                    total += code[i]
                else:
                    total -= window.popleft()
                    window.append(code[i])
                    total += code[i]
                    res.append(total)
            return res[:n][::-1]