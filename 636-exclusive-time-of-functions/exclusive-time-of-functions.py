class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack=[]

        res=[0]*n
        prev_timestamp=0


        for element in logs:
            #parse logs
            function,start,timestamp=element.split(":")
            function=int(function)
            timestamp=int(timestamp)
            
            if start=="start":
                if stack:
                    res[stack[-1]] += timestamp - prev_timestamp
                stack.append(function)
                prev_timestamp = timestamp
            else:
                res[stack.pop()] += timestamp - prev_timestamp + 1
                prev_timestamp = timestamp + 1
        return res