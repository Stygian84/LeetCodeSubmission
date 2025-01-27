class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key = lambda x:(-int(x[1]),x[0]),reverse = True)
        
        n = numberOfUsers
        mentions = [0]*n

        offline = set() #id
        offline_dc = defaultdict(list) #time = list[id]

        for item in events:
            timestamp = int(item[1])

            if offline_dc:
                minimum = min(offline_dc.keys())
                while timestamp >= minimum:
                    for id in offline_dc[minimum]:
                        offline.remove(id)
                    del offline_dc[minimum]
                    
                    if offline_dc:
                        minimum = min(offline_dc.keys())
                    else:
                        break

            if item[0]=="MESSAGE":
                mentions_string = item[-1]
                if mentions_string == "ALL":
                    for i in range(n):
                        mentions[i]+=1

                elif mentions_string == "HERE":
                    for i in range(n):
                        if i not in offline:
                            mentions[i]+=1

                else:
                    ids = mentions_string.split()
                    for id in ids:
                        mentions[int(id[2:])]+=1
            else:
                offline_id = int(item[-1])
                offline.add(offline_id)
                offline_dc[timestamp+60].append(offline_id)
        

        return mentions