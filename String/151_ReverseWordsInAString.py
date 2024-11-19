class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)


class Solution2:
    def reverseWords(self, s: str) -> str:
        l, r = 0, len(s) - 1
        while l <= r and s[l] == " ":
            l += 1
        while l <= r and s[r] == " ":
            r -= 1
        queue = deque()
        word = []
        while l <= r:
            if s[l] == " " and word:
                queue.appendleft("".join(word))
                word = []
            elif s[l] != " ":
                word.append(s[l])
            l += 1
        queue.appendleft("".join(word))
        return " ".join(queue)