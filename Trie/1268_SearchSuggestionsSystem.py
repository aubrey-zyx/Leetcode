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