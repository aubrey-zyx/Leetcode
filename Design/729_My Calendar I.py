from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        idx = self.calendar.bisect_right((startTime, endTime))
        if (idx > 0 and startTime < self.calendar[idx - 1][1]) or (idx < len(self.calendar) and endTime > self.calendar[idx][0]):
            return False
        self.calendar.add((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)