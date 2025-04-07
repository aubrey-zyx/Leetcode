class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1_prefixes = set()

        for num in arr1:
            while num and num not in arr1_prefixes:
                arr1_prefixes.add(num)
                num //= 10

        res = 0

        for num in arr2:
            while num and num not in arr1_prefixes:
                num //= 10
            if num > 0:
                res = max(res, len(str(num)))

        return res


# Trie
class Solution2:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()

        for num in arr1:
            trie.insert(num)

        res = 0
        for num in arr2:
            size = trie.find_longest_prefix(num)
            res = max(res, size)
        return res


class TrieNode:
    def __init__(self):
        self.children = [None] * 10


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        cur = self.root
        num_str = str(num)
        for digit in num_str:
            i = int(digit)
            if not cur.children[i]:
                cur.children[i] = TrieNode()
            cur = cur.children[i]

    def find_longest_prefix(self, num):
        cur = self.root
        num_str = str(num)
        res = 0
        for digit in num_str:
            i = int(digit)
            if cur.children[i]:
                res += 1
                cur = cur.children[i]
            else:
                break
        return res