class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        # sum = power of 2

        answer = [1]
        prev = 1
        for _ in range(22):
            prev*=2
            answer.append(prev)
        
        freq = defaultdict(int)
        res = 0

        for value in deliciousness:
            for power in answer:
                if power >= value:
                    target = power-value

                    if target in freq:
                        res += freq[target]
            freq[value]+=1

        return res % (10**9 + 7)
