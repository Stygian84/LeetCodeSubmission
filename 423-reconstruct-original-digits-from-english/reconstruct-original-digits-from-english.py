class Solution:
    def originalDigits(self, s: str) -> str:
        # one two three four five six seven eight nine
        freq = Counter(s)

        res = []

        def check(letter,word,digit):
            nonlocal res
            if letter in freq:
                count = freq[letter]
                res += [digit*freq[letter]]
                
                for item in word:
                    freq[item] -= count
                    if freq[item] == 0:
                        del freq[item]
        #letter to word
        dc = {"z":"zero0", "w":"two2", "u":"four4","x":"six6","g":"eight8",
                "o":"one1", "t":"three3", "f":"five5", "s":"seven7", "i":"nine9"}

        for k,v in dc.items():
            check(k,v[:-1],v[-1])
        
        # left with one1 three3 five5 seven7 nine9
        # if o exists, remove one
        # if t exists, remove three
        # if f exists, remove five
        # if s exists, remove seven
        # if n exists, remove nine
        
        res.sort()
        return "".join(res)