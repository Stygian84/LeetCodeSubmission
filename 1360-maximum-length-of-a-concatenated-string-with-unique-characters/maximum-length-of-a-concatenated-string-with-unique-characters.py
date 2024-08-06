class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        n = len(arr)
        maximum = 0
        def backtrack(start,path,seen,total):
            nonlocal maximum
            maximum = max(total,maximum)
            if start == n:
                return

            for i in range(start,n):
                word = arr[i]
                if len(word)>len(set(word)):
                    continue
                for letter in word:
                    if letter in seen:
                        break
                else:
                    prev_seen = seen.copy()
                    for letter in word:
                        seen.add(letter)
                    path.append(word)
                    backtrack(i+1,path,seen,total+len(word))
                    path.pop()
                    seen = prev_seen
                


        backtrack(0,[],set(),0)
        return maximum