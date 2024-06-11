class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_length=0
        current_str=deque([])
        dc={"T":0,"F":0}

        for item in answerKey:
            if min(dc["T"],dc["F"])>k:
                while min(dc["T"],dc["F"])>k:
                    dc[current_str.popleft()]-=1
                max_length=max(len(current_str),max_length)
            current_str.append(item)
            dc[item]+=1
            if min(dc["T"],dc["F"])==k:
                max_length=max(len(current_str),max_length)
        while min(dc["T"],dc["F"])>k:
            dc[current_str.popleft()]-=1
        max_length=max(len(current_str),max_length)

        return max_length
        