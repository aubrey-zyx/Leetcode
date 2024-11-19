class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_hash(s):
            shift = ord(s[0])
            after = []
            for c in s:
                after.append(chr((ord(c) - shift) % 26 + ord('a')))
            return "".join(after)

        ht = defaultdict(list)
        for string in strings:
            key = get_hash(string)
            ht[key].append(string)
        return list(ht.values())


class Solution2:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_hash(s):
            diff = []
            for a, b in zip(string, string[1:]):
                diff.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
            return "".join(diff)

        ht = defaultdict(list)
        for string in strings:
            key = get_hash(string)
            ht[key].append(string)
        return list(ht.values())