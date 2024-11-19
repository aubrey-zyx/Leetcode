class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        cnt_target = Counter(target)
        A = [Counter(sticker) & cnt_target for sticker in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        stickers = ["".join(cnt_sticker.elements()) for cnt_sticker in A]

        n = len(target)
        # Store the minimum number of stickers needed to form each possible subset of the target string
        dp = [-1] * (1 << n)
        dp[0] = 0

        # Each state is represented as a bitmask
        # where a bit set to 1 indicates the presence of the corresponding character in the subset
        for state in range(1 << n):
            if dp[state] == -1:
                continue
            for sticker in stickers:
                now = state
                for letter in sticker:
                    for i, c in enumerate(target):
                        # If target already has the letter flipped, ignore
                        if (now >> i) & 1:
                            continue
                        # If the current letter matches, update the state by setting the corresponding bit to 1
                        if c == letter:
                            now |= 1 << i
                            break
                # If the new state (formed by adding the current sticker) is better (requires fewer stickers)
                # than the previously known best way to form that state, update the dp table.
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1

        return dp[-1]