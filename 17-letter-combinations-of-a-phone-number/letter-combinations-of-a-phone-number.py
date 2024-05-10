class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1 = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        first=[]
        second=[]
        third=[]
        fourth=[]
        output=[]
        try:
            for item in dict1[digits[0]]:
                first.append(item)
        except:
            return []
        try:
            for item in dict1[digits[1]]:
                second.append(item)
        except:
            return first
        
        for item in first:
            for items in second:
                output.append(item+items)
                
        try:
            for item in dict1[digits[2]]:
                third.append(item)
        except:
            return output
        
        temp_list=[]
        for item in output:
            for items in third:
                temp_list.append(item+items)
        output=temp_list
        
        try:
            for item in dict1[digits[3]]:
                fourth.append(item)
        except:
            return output
        
        temp_list=[]
        for item in output:
            for items in fourth:
                temp_list.append(item+items)
        output=temp_list

        return output