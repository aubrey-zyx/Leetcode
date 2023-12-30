class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        ht = collections.defaultdict(list)
        for prod in products:
            i = 0
            while i < len(prod) and i < len(searchWord):
                if prod[i] != searchWord[i]:
                    break
                i += 1
                ht[prod[:i]].append(prod)
        for val in ht.values():
            val.sort()

        for i in range(len(searchWord)):
            matches = ht[searchWord[: i + 1]]
            if len(matches) > 3:
                res.append(matches[: 3])
            else:
                res.append(matches)
            i += 1

        return res


# Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def insert(root, word):
            cur = root
            for c in word:
                if c not in c.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
                cur.words.append(word)
                cur.words.sort()
                if len(cur.words) > 3:
                    cur.words.pop()

        root = TrieNode()
        for prod in products:
            insert(root, prod)

        res = []
        cur = root
        flag = False
        for c in searchWord:
            if flag or c not in cur.children:
                res.append([])
                flag = True
            else:
                cur = cur.children[c]
                res.append(cur.words)

        return res