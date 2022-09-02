import collections
import string


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for i in string.punctuation:
            paragraph = paragraph.replace(i, ' ').lower()
        words = paragraph.split()
        cnt = collections.Counter(words)
        cnt_order = sorted(cnt.items(), key=lambda x:x[1], reverse=True)
        for i in range(len(cnt_order)):
            if cnt_order[i][0] not in banned:
                return cnt_order[i][0]