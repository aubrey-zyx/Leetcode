class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            alive = True
            while alive and asteroid < 0 and stack and stack[-1] > 0:
                alive = -asteroid > stack[-1]
                if -asteroid >= stack[-1]:
                    stack.pop()
            if alive:
                stack.append(asteroid)
        return stack