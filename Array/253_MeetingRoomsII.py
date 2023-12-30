class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for s, e in intervals:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()

        i = j = 0
        count = 0
        res = 0
        while i < len(start):
            if start[i] < end[j]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            res = max(res, count)

        return res


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort()
        for i in intervals:
            if not heap or i[0] < heap[0]:
                heapq.heappush(heap, i[1])
            else:
                heapq.heapreplace(heap, i[1])
        return len(heap)