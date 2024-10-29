class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # return group of duplicate file paths (which have same content)
        # format : "directory_path/file_name.txt(abcd)" abcd is the content
        # if root/file.txt its root directory

        storage = defaultdict(list)

        for p in paths:
            ls = p.split(" ") 
            root_directory = ls[0]
            
            for item in ls[1:]:
                #content is in bracket ()
                #before bracket is the subdirectory
                open_idx = item.index("(")
                subdirectory = item[:open_idx]
                content = item[open_idx+1:-1]
                #print(subdirectory,content)        
                storage[content].append( root_directory + "/" + subdirectory )
        #print(storage)
        res = []
        for v in storage.values():
            if len(v)>1:
                res.append(v)
        return res        