class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count=0
        arr=deque([])

        for digit in str(num):
            arr.append(digit)
            if len(arr)>k:
                arr.popleft()
            if len(arr)==k:
                number=int("".join(arr))
                if number!=0 and num%number==0:
                    count+=1
        return count