class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)

        for item in cpdomains:
            ls = item.split(" ")
            frequency = int(ls[0])
            websites = ls[1].split(".")
            
            #print(websites)
            
            for i in range(len(websites)):
                current = ".".join(websites[i:])
                domains[current] += frequency
        
        #print(domains)

        res = []
        for k,v in domains.items():
            res.append(" ".join([str(v),k]))
        return res