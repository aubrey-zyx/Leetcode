class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        n = len(s)
        sections = ceil(n / (2 * num_rows - 2))
        num_cols = sections * (num_rows - 1)
        matrix = [[""] * num_cols for _ in range(num_rows)]

        r = c = 0
        i = 0
        while i < n:
            # Move down
            while r < num_rows and i < n:
                matrix[r][c] = s[i]
                r += 1
                i += 1

            r -= 2
            c += 1

            # Move diagonally up
            while r > 0 and c < num_cols and i < n:
                matrix[r][c] = s[i]
                r -= 1
                c += 1
                i += 1

        res = ""
        for row in matrix:
            res += "".join(row)
        return res


class Solution2:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        n = len(s)
        res = []
        chars_in_section = 2 * num_rows - 2

        for r in range(num_rows):
            i = r
            while i < n:
                res.append(s[i])
                if r != 0 and r != num_rows - 1:
                    jump = chars_in_section - 2 * r
                    next_idx = i + jump
                    if next_idx < n:
                        res.append(s[next_idx])
                i += chars_in_section

        return "".join(res)