class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        length=len(strs[0])
        for i in range(length):
            column=[]
            for index in range(len(strs)):
                column.append(strs[index][i])
            for idx in range(1,len(column)):
                if ord(column[idx])<ord(column[idx-1]):
                    count+=1
                    break
        return count

        