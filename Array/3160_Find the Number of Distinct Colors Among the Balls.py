class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        colors = defaultdict(int)
        balls = {}

        for ball, color in queries:
            if ball in balls:
                prev_color = balls[ball]
                colors[prev_color] -= 1
                if colors[prev_color] == 0:
                    del colors[prev_color]
            balls[ball] = color
            colors[color] += 1
            res.append(len(colors))

        return res