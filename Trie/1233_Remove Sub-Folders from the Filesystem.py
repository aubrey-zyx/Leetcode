class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]
        for i in range(1, len(folder)):
            last = res[-1]
            last += "/"
            if not folder[i].startswith(last):
                res.append(folder[i])
        return res


# Trie
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}


class Solution2:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        for path in folder:
            folders = path.split("/")
            cur = root
            for folder_name in folders:
                if folder_name not in cur.children:
                    cur.children[folder_name] = TrieNode()
                cur = cur.children[folder_name]
            cur.is_end = True

        res = []
        for path in folder:
            folders = path.split("/")
            cur = root
            is_subfolder = False
            for i, folder_name in enumerate(folders):
                child = cur.children[folder_name]
                if child.is_end and i != len(folders) - 1:
                    is_subfolder = True
                    break
                cur = child

            if not is_subfolder:
                res.append(path)

        return res