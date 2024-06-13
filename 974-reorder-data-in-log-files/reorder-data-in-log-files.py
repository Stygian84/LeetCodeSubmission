class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log=[]
        digit_log=[]
        res=[]
        for item in logs: #split into 2 diff type of log
            ls=item.split()
            if ls[1].isdigit():
                digit_log.append(item)
            else:
                letter_log.append(item)

        #sort letter_log
        def is_greater(a,b): #a>b
            ls_a=a.split()
            ls_b=b.split()
            for item1,item2 in zip(ls_a[1:],ls_b[1:]):
                if item1!=item2: #if diff check which one greater
                    
                    for first,second in zip(item1,item2):
                        if ord(first)>ord(second):
                            return True
                        elif ord(first)<ord(second):
                            return False
                    if len(item1)>len(item2):
                        return True
                    break
            else:
                if len(ls_a)>len(ls_b):
                    return True
                #all same check identifier
                i=0
                for item1,item2 in zip(ls_a[0],ls_b[0]):
                    if item1!=item2:
                        return ord(item1)>ord(item2)
                    
        
        #bubble sort letter_log
        for i in range(len(letter_log)):
            for j in range(len(letter_log)-i-1):
                if is_greater(letter_log[j], letter_log[j+1]):
                    letter_log[j], letter_log[j+1] = letter_log[j+1], letter_log[j]
        res=letter_log+digit_log
        return res