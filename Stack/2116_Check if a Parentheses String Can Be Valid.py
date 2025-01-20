class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        opens = []
        unlocked = []

        for i, c in enumerate(s):
            if locked[i] == "0":
                unlocked.append(i)
            elif c == "(":
                opens.append(i)
            elif c == ")":
                if opens:
                    opens.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while opens and unlocked and opens[-1] < unlocked[-1]:
            opens.pop()
            unlocked.pop()
        if opens:
            return False
        return True


# O(1) space
class Solution2:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        opens = 0
        unlocked = 0

        for i, c in enumerate(s):
            if locked[i] == "0":
                unlocked += 1
            elif c == "(":
                opens += 1
            elif c == ")":
                if opens > 0:
                    opens -= 1
                elif unlocked:
                    unlocked -= 1
                else:
                    return False

        balance = 0
        for i, c in enumerate(s[::-1]):
            if locked[i] == "0":
                balance -= 1
                unlocked -= 1
            elif c == "(":
                balance += 1
                opens -= 1
            elif c == ")":
                balance -= 1
            if balance > 0:
                return False
            if unlocked == 0 and opens == 0:
                break
        if opens > 0:
            return False
        return True