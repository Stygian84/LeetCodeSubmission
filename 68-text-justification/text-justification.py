class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if len(words)==1:
            return [words[0].ljust(maxWidth," ")]
        res=[]

        temp_ls=[]
        temp_length=0
        words=deque(words)

        #Split into correct rows
        for i in range(len(words)):
            item=words.popleft()
            if temp_length+len(item)+len(temp_ls)<=maxWidth:
                temp_ls.append(item)
                temp_length+=len(item)
            else:
                temp_ls.append(temp_length)
                res.append(temp_ls)
                temp_ls=[item]
                temp_length=len(item)
        if temp_ls:
            res.append(temp_ls)

        #parse except last row
        def parse(ls,maxWidth):
            total_length=ls.pop()
            if len(ls)-1==0:
                res=" ".join(ls)
                return res.ljust(maxWidth)

            else:
                no_space=(maxWidth-total_length)//(len(ls)-1)
                first_space=(maxWidth-total_length)//(len(ls)-1)+(maxWidth-total_length)%(len(ls)-1)
                temp_str=""
                for i in range(len(ls)):
                    if first_space>no_space:
                        temp_str+=ls[i]+" "*no_space+" "
                        first_space-=1
                    elif i==len(ls)-1:
                        temp_str+=ls[i]
                    else:
                        temp_str+=ls[i]+" "*no_space
                return temp_str

        def parseLast(ls,maxWidth):
            res=" ".join(ls)
            return res.ljust(maxWidth)

        for i in range(len(res)-1):
            res[i]=parse(res[i],maxWidth)

        res[-1]=parseLast(res[-1],maxWidth)
        return res