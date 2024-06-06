class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''     
        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern_map = {}
        seen_values = set()

        for char, word in zip(pattern, words):
            if char in pattern_map:
                if pattern_map[char] != word:
                    return False
            else:
                if word in seen_values:
                    return False
                pattern_map[char] = word
                seen_values.add(word)

        return True'''
        dc={}
        ls=s.split()
        if len(pattern) != len(ls):
            return False



        for i in range(len(pattern)):
            if pattern[i] in dc:
                if ls[i]!=dc[pattern[i]]:
                    return False
            else:
                dc[pattern[i]]=ls[i]

        seen_values = set()
        duplicate_values = set()

        for value in dc.values():
            if value in seen_values:
                duplicate_values.add(value)
            else:
                seen_values.add(value)

        if len(duplicate_values)>0:
            return False
            
        return True
        