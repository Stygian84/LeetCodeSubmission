class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dc={} # dc key: table no , value=dict( key: menu , value: freq)
        menu=set()
        table=set()

        for item in orders:
            dc[item[1]]=dc.get(item[1],{})
            dc[item[1]][item[2]]=dc[item[1]].get(item[2],0)+1
            table.add(int(item[1]))
            menu.add(item[2])
        first_row=["Table"]
        menu=list(menu)
        menu.sort()
        table=list(table)
        table.sort()

        for item in menu:
            first_row.append(item)

        res=[first_row]
        for idx in table:
            temp_ls=[str(idx)]
            for item in menu:
                temp_ls.append(str(dc[str(idx)].get(item,"0")))
            res.append(temp_ls)

        return res