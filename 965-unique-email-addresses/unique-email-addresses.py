class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for idx in range(len(emails)):
            temp_str=""
            before=True
            plus=False
            for item in emails[idx]:
                if before:
                    if item=="+":
                        plus=True
                        continue
                    if item==".":
                        continue
                if item=="@":
                    before=False
                    plus=False
                if plus:
                    continue
                temp_str+=item
            emails[idx]=temp_str
        return len(list(set(emails)))
        