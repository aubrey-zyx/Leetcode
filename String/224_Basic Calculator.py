class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        digit_power = 0
        num = 0

        for ch in s[::-1]:
            if ch.isdigit():
                num += int(ch) * (10 ** digit_power)
                digit_power += 1
            elif ch != " ":
                if digit_power:
                    # Save the num onto stack when encountering some non-digit
                    stack.append(num)
                    digit_power, num = 0, 0
                if ch == "(":
                    res = self.evaluate_expr(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(ch)

        # Push the last num to stack, if any
        if digit_power:
            stack.append(num)

        return self.evaluate_expr(stack)

    def evaluate_expr(self, stack):
        # If stack is empty or the expression starts with a symbol, append 0 to the stack
        # e.g. [1, '-', 2, '-'] -> [1, '-', 2, '-', 0]
        if not stack or type(stack[-1]) == str:
            stack.append(0)
        res = stack.pop()
        while stack and stack[-1] != ")":
            sign = stack.pop()
            if sign == "+":
                res += stack.pop()
            else:
                res -= stack.pop()
        return res