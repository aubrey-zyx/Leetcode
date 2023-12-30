class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = collections.Counter(s)
        lst = sorted(s)
        lst.sort(key=cnt.get, reverse=True)

        n = len(s)
        if n < 2:
            return s

        mid = (n + 1) // 2
        if lst[mid] == lst[0]:
            return ""

        left, right = lst[:mid], lst[mid:]
        for i in range(len(left)):
            lst[i * 2] = left[i]
        for i in range(len(right)):
            lst[i * 2 + 1] = right[i]

        return "".join(lst)


class Solution2:
    def reorganizeString(self, s: str) -> str:
        res = ""
        cnt = collections.Counter(s)
        if max(cnt.values()) > (len(s) + 1) // 2:
            return res

        heap = []
        for ch, freq in cnt.items():
            heapq.heappush(heap, (-freq, ch))

        prev = (0, None)
        while heap:
            freq, ch = heapq.heappop(heap)
            res += ch
            if prev[0] < 0:
                heapq.heappush(heap, prev)
            prev = (freq + 1, ch)

        return res


class Solution3:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        cnt = collections.Counter(s)
        if max(cnt.values()) > (n + 1) // 2:
            return ""

        res = []
        heap = []
        for ch, freq in cnt.items():
            heapq.heappush(heap, (-freq, ch))

        while len(heap) > 1:
            _, ch1 = heapq.heappop(heap)
            _, ch2 = heapq.heappop(heap)
            res.extend([ch1, ch2])
            cnt[ch1] -= 1
            cnt[ch2] -= 1
            if cnt[ch1] > 0:
                heapq.heappush(heap, (-cnt[ch1], ch1))
            if cnt[ch2] > 0:
                heapq.heappush(heap, (-cnt[ch2], ch2))

        if heap:
            res.append(heap[0][1])

        return "".join(res)