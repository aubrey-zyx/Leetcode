class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        cows = 0
        for c in set(secret):
            cows += min(secret.count(c), guess.count(c))
        cows -= bulls
        return f"{bulls}A{cows}B"