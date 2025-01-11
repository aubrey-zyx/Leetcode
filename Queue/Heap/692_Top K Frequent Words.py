# Brute Force
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        return sorted(list(cnt.keys()), key=lambda x: (-cnt[x], x))[:k]


# Min Heap
class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self.word > other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        heap = []
        for word, freq in cnt.items():
            heapq.heappush(heap, Word(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)
        return [w.word for w in sorted(heap, reverse=True)]