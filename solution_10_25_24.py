class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        root = TrieNode()
        for f in folder:
            foldlist = (f.split("/"))[1:]
            print(foldlist)
            node = root
            for dr in foldlist:
                if dr not in node.children:
                    node.children[dr] = TrieNode()
                node = node.children[dr]

            node.end = True
        
        ret = []
        for f in folder:
            cur = root
            foldlist = (f.split("/"))[1:]
            issub = False

            for i, fname in enumerate(foldlist):
                nex = cur.children[fname]

                if nex.end and i != len(foldlist) - 1:
                    issub = True
                cur = nex
            if not issub:
                ret.append(f)

        return ret
