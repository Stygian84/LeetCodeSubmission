class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        
        freq = Counter(croakOfFrogs)

        maximum = max(freq.values())

        for k,v in freq.items():
            if v%maximum!=0:
                return -1

        # if another c appear before k , frog+1-
        count = 0
        frog = defaultdict(int)

        for letter in croakOfFrogs:
            frog[letter]+=1

            if letter=="c":
                pass

            elif letter=="r":
                if frog[letter]>frog['c']:
                    return -1

            elif letter=="o":
                if frog[letter]>frog['r']:
                    return -1

            elif letter=="a":
                if frog[letter]>frog['o']:
                    return -1

            elif letter=="k":
                if frog[letter]>frog['a']:
                    return -1
                count=max(frog['c'],count)
                for item in 'croak':
                    frog[item]-=1
            

        return count