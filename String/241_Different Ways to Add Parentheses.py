class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []

        # Base case: empty string
        if len(expression) == 0:
            return res

        # Base case: single digit
        if len(expression) == 1:
            return [int(expression)]

        # Base case: two-digit number
        if len(expression) == 2 and expression[0].isdigit():
            return [int(expression)]

        # Recursive case: split the expression at each operator
        for i, c in enumerate(expression):
            if c.isdigit():
                continue

            left_res = self.diffWaysToCompute(expression[:i])
            right_res = self.diffWaysToCompute(expression[i + 1:])

            # Combine results from left and right subexpressions
            for left_val in left_res:
                for right_val in right_res:
                    if c == "+":
                        res.append(left_val + right_val)
                    elif c == "-":
                        res.append(left_val - right_val)
                    elif c == "*":
                        res.append(left_val * right_val)
        return res


# With memoization & pass in indices to avoid creating substrings
class Solution2:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(start, end):
            if (start, end) in memo:
                return memo[(start, end)]

            res = []

            # Base case: single digit
            if start == end:
                return [int(expression[start])]

            # Base case: two-digit number
            if end - start == 1 and expression[start].isdigit():
                return [int(expression[start: end + 1])]

            # Recursive case: split the expression at each operator
            for i in range(start, end + 1):
                c = expression[i]
                if c.isdigit():
                    continue

                left_res = compute(start, i - 1)
                right_res = compute(i + 1, end)

                # Combine results from left and right subexpressions
                for left_val in left_res:
                    for right_val in right_res:
                        if c == "+":
                            res.append(left_val + right_val)
                        elif c == "-":
                            res.append(left_val - right_val)
                        elif c == "*":
                            res.append(left_val * right_val)

            memo[(start, end)] = res

            return res

        memo = {}
        return compute(0, len(expression) - 1)