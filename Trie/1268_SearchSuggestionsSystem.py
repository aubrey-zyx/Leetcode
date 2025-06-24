# Hashmap
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


# Two Pointers
class Solution2:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(products)
        products.sort()
        l, r = 0, n - 1
        res = []
        for i, c in enumerate(searchWord):
            while l <= r and (i >= len(products[l]) or products[l][i] != c):
                l += 1
            while l <= r and (i >= len(products[r]) or products[r][i] != c):
                r -= 1
            res.append([products[j] for j in range(l, min(l + 3, r + 1))])
        return res


# Binary Search
class Solution3:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, prefix, i = [], "", 0
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix, i)
            res.append([prod for prod in products[i: i + 3] if prod.startswith(prefix)])
        return res


# Trie
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.words = []


class Solution4:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def insert(root, word):
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
                if len(cur.words) < 3:
                    cur.words.append(word)

        root = TrieNode()
        products.sort()
        for prod in products:
            insert(root, prod)

        res = []
        cur = root
        for c in searchWord:
            cur = cur.children[c]
            res.append(cur.words)
        return res