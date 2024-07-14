class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def multiply_dict(d, factor):
            for key in d:
                d[key] *= factor
            return d
        
        stack = [collections.defaultdict(int)]
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(collections.defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)
                top = stack.pop()
                multiply_dict(top, multiplier)
                for key, value in top.items():
                    stack[-1][key] += value
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                element = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)
                stack[-1][element] += count
        
        final_counts = stack.pop()
        result = []
        
        for element in sorted(final_counts.keys()):
            result.append(element)
            if final_counts[element] > 1:
                result.append(str(final_counts[element]))
        
        return ''.join(result)