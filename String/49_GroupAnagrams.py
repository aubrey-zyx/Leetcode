class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            ht[key].append(str)
        return list(ht.values())


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for str in strs:
            cnt = [0] * 26
            for c in str:
                cnt[ord(c) - ord("a")] += 1
            ht[tuple(cnt)].append(str)
        return list(ht.values())