class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def get_words(i):
            line = []
            length = 0
            while i < len(words) and length + len(words[i]) <= maxWidth:
                line.append(words[i])
                length += len(words[i]) + 1
                i += 1
            return line

        def create_line(line, i):
            length = -1
            for word in line:
                length += len(word) + 1
            extra_spaces = maxWidth - length
            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extra_spaces
            gaps = len(line) - 1
            spaces_per_gap = extra_spaces // gaps
            uneven_spaces = extra_spaces % gaps
            for j in range(uneven_spaces):
                line[j] += " "
            for j in range(gaps):
                line[j] += " " * spaces_per_gap
            return " ".join(line)

        res = []
        i = 0
        while i < len(words):
            cur_line = get_words(i)
            i += len(cur_line)
            res.append(create_line(cur_line, i))
        return res