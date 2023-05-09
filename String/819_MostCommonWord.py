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


'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split(r'\W+', paragraph.lower())     # split string into words by spaces and punctuation
        words = filter(lambda x: x not in banned + [''], words)
        return Counter(words).most_common(1)[0][0]
'''


'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split(r'\W+', paragraph.lower())
        words = [w for w in words if w not in set(banned + [''])]
        return max(words, key=words.count)
'''