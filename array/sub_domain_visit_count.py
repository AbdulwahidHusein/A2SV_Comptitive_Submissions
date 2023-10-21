class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dc = {}
        for cdomain in cpdomains:
            count, domain = cdomain.split()
            count = int(count)
            sd = domain.split(".")

            for i in range(len(sd)):
                sbd = '.'.join(sd[i:])
                try:
                    dc[sbd] += count
                except:
                    dc[sbd] = count
        arr = []
        for dom in dc:
            arr.append(str(dc[dom])+" "+dom)
        return arr
        