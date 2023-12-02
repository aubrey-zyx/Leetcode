# https://instant.1point3acres.cn/thread/1028061
# https://leetcode.com/discuss/interview-question/4147887/AMAZON-OA-oror-AWS/

import heapq
import math

def get_priorities(priorities):
    heap = []
    tmp = []
    for i in range(len(priorities)):
        heapq.heappush(heap, -priorities[i])

    while heap:
        cur_max = heapq.heappop(heap)

        if heap and heap[0] == cur_max:
            heapq.heappop(heap)
            heapq.heappush(heap, math.ceil(cur_max / 2))
        else:
            tmp.append(cur_max)

    return [-p for p in heap + tmp]

print(get_priorities([2, 1, 5, 10, 10, 1, 12]))


'''
import heapq
import math
def get_priorities(priorities):
    pq = []
    temp = [-1] * len(priorities)

    # have to push on negative 
    for i in range(len(priorities)):
        heapq.heappush(pq, (-priorities[i], i))

    while pq:
        curr_max = heapq.heappop(pq)
        curr_priority = curr_max[0]
        p2_idx = None

        while pq and pq[0][0] == curr_priority:
            curr_max = heapq.heappop(pq)
            if curr_max[0] == curr_priority:
                if not p2_idx:
                    p2_idx = curr_max[1]
                    temp[p2_idx] = -math.ceil(curr_max[0]/2)
                    heapq.heappush(pq, (math.ceil(curr_max[0]/2), p2_idx))
                else:
                    temp[curr_max[1]] = -curr_max[0]

    return [i for i in temp if i != -1]
'''