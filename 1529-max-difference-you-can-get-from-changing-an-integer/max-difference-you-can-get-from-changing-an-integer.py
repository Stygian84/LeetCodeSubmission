class Solution:
    def maxDiff(self, num: int) -> int:

        highest = list(str(num))
        lowest = list(str(num))
        if highest == ["1"]*len(highest):
            return int("8"*len(highest))


        replaced = highest[0]
        if len(highest)>1 and highest[0] == "9":
            for j in range(1,len(highest)):
                if highest[j]=="9":
                    continue
                else:
                    replaced = highest[j]
                    break
            
        for i in range(len(highest)):
            if highest[i] == replaced:
                highest[i] = "9"
        

        replaced = lowest[0]
        if len(lowest)>1 and lowest[0] == "1":
            
            for k in range(len(lowest)):
                if lowest[k]=="1" or lowest[k]=="0":
                    continue
                else:
                    replaced = lowest[k]
                    break
            if replaced == "1" or replaced == "0":
                pass
            else:
                for j in range(len(lowest)):
                    if lowest[j] == replaced:
                        lowest[j] = "0"
        else:    
            for j in range(len(lowest)):
                if lowest[j] == replaced:
                    lowest[j] = "1"
        print(highest,lowest)
        return int("".join(highest))-int("".join(lowest))
        