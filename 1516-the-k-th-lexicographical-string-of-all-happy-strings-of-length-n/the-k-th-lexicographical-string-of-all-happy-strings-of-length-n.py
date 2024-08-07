class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = ""

        def backtrack(path):
            nonlocal k,res
            if len(path)==n:
                k-=1
                if k==0:
                    res="".join(path[:])
                return
            if res:
                return

            for item in "abc":
                if not path:
                    path.append(item)
                    backtrack(path)
                    path.pop()

                if (path and path[-1]!=item):
                    path.append(item)
                    backtrack(path)
                    path.pop()


        backtrack([])
        print(res)
        return res