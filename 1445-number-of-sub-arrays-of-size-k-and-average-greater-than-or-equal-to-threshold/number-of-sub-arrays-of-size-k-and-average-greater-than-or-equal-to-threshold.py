class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ls = deque([])
        total = 0
        count = 0
        for item in arr:
            if len(ls)==k:
                if total/k>=threshold:
                    count += 1
                total-=ls.popleft()

            if len(ls)<k:
                ls.append(item)
                total += item

        if total/k>=threshold:
            count += 1
        return count