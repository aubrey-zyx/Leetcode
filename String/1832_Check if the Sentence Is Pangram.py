class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set(sentence)
        return len(seen) == 26


class Solution2:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = [False] * 26
        for c in sentence:
            seen[ord(c) - ord('a')] = True
        return all(seen)