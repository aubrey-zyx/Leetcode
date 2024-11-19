# O(52m + n)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res_l, res_r = -1, len(s)
        cnt_win = Counter()
        cnt_t = Counter(t)

        l = 0
        for r, c in enumerate(s):
            cnt_win[c] += 1
            while cnt_win >= cnt_t:
                if r - l < res_r - res_l:
                    res_l, res_r = l, r
                cnt_win[s[l]] -= 1
                l += 1

        return "" if res_l < 0 else s[res_l: res_r + 1]

# O(m + n)
class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        cnt_t = Counter(t)
        cnt_win = defaultdict(int)
        min_len = float("inf")
        res_l = res_r = None
        formed = 0
        required = len(cnt_t)

        l = 0
        for r in range(len(s)):
            c = s[r]
            cnt_win[c] += 1
            if c in cnt_t and cnt_win[c] == cnt_t[c]:
                formed += 1
            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res_l = l
                    res_r = r
                lc = s[l]
                cnt_win[lc] -= 1
                if lc in cnt_t and cnt_win[lc] < cnt_t[lc]:
                    formed -= 1
                l += 1

        return "" if min_len == float("inf") else s[res_l: res_r + 1]


# O(m + n), but when |filtered_S| <<< |S|, the complexity would reduce
# the number of iterations would be 2 * |filtered_S| + |S| + |T|
class Solution3:
    def minWindow(self, s: str, t: str) -> str:
        cnt_t = Counter(t)
        cnt_win = Counter()
        required = len(cnt_t)
        formed = 0
        res_l, res_r = -1, len(s)

        # Filter all characters from s into a new list along with their index
        # The filtering criteria is that the character should be present in t
        filtered_s = []
        for i, ch in enumerate(s):
            if ch in cnt_t:
                filtered_s.append((i, ch))

        l = 0
        for r in range(len(filtered_s)):
            c = filtered_s[r][1]
            cnt_win[c] += 1
            if cnt_win[c] == cnt_t[c]:
                formed += 1
            while l <= r and formed == required:
                if filtered_s[r][0] - filtered_s[l][0] < res_r - res_l:
                    res_l, res_r = filtered_s[l][0], filtered_s[r][0]
                lc = filtered_s[l][1]
                cnt_win[lc] -= 1
                if cnt_win[lc] < cnt_t[lc]:
                    formed -= 1
                l += 1

        return "" if res_l < 0 else s[res_l: res_r + 1]