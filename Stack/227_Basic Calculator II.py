class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        num = 0
        prev_op = '+'

        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in '+-*/' or i == n - 1:
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                prev_op = s[i]
                num = 0
        return sum(stack)


# O(1) space
class Solution2:
    def calculate(self, s: str) -> int:
        n = len(s)
        prev_op = "+"
        res = 0
        last_num = cur_num = 0

        for i in range(n):
            if s[i].isdigit():
                cur_num = cur_num * 10 + int(s[i])
            if s[i] in "+-*/" or i == n - 1:
                if prev_op == "+" or prev_op == "-":
                    res += last_num
                    last_num = cur_num if prev_op == "+" else -cur_num
                elif prev_op == "*":
                    last_num = last_num * cur_num
                else:
                    last_num = int(last_num / cur_num)
                prev_op = s[i]
                cur_num = 0
        res += last_num
        return res