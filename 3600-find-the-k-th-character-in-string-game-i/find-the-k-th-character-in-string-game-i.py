class Solution:
    def kthCharacter(self, k: int) -> str:
        
        def add(x):
            current = list(x)
            temp = []
            for letter in current:
                res = ord(letter)+1
                if res>ord('z'):
                    res = ord('a')+res-ord('z')
                temp.append(chr(res))

            current.extend(temp)
            return "".join(current)

        initial = 'a'
        while len(initial)<k:
            initial = add(initial)
        
        return initial[k-1]