class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        minutes = []
        for time_point in timePoints:
            minutes.append(self.getMinutes(time_point))
        minutes.sort()
        ans = 720
        for i in range(len(minutes) - 1):
            ans = min(ans, minutes[i + 1] - minutes[i])
        ans = min(ans, 1440 - minutes[-1] + minutes[0])
        return ans

    def getMinutes(self, t: str):
        return int(t[:2]) * 60 + int(t[-2:])