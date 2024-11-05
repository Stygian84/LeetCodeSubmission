class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        library = defaultdict(list)

        for a,b in zip(s1,s2):
            library[b].append(a)
            library[a].append(b)
        

        def dfs(current,seen,smallest):
            seen.add(current)
            smallest = min(smallest,current)

            for letter in library[current]:
                if letter not in seen:
                    smallest = min(smallest, dfs(letter,seen,smallest))    

            return smallest

        new_library = {}

        for k in library:
            new_library[k] = dfs(k,set(),k)

        res = []
        for letter in baseStr:
            if letter in new_library:
                res += new_library[letter]
            else:
                res += letter
            
        return "".join(res)
        '''dc = {}
        for a,b in zip(s1,s2):
            if a<b:
                if b in dc:
                    dc[b] = min(dc[b],a)
                else:
                    dc[b]=a
            else:
                if a in dc:
                    dc[a] = min(dc[a],b)
                else:
                    dc[a]=b
        
        def dfs(key,minimum,seen):
            
            if key in dc and key not in seen:
                seen.add(key)
                minimum = min(dc[key],minimum)
                return dfs(dc[key],minimum,seen)
            else:
                return minimum

        res = []
        
        dc1 = {}
        for k,v in dc.items():
            dc1[k] = dfs(k,k,set())

        for letter in baseStr:
            if letter in dc1 and dc1[letter]<letter:
                res.append(dc1[letter])
            else:
                res.append(letter)
        
        return "".join(res)'''