import bisect


class MyCalendar:

    def __init__(self):
        self.low = 0
        self.high = 0
        self.ret = []
        self.ret_set = set()

    def book(self, start: int, end: int) -> bool:
        if self.low == self.high:
            self.low = start
            self.high = end
            bisect.insort_left(self.ret, start)
            bisect.insort_left(self.ret, end)
            self.ret_set.add((start, end))
            return True
        if self.high <= start:
            self.high = end
            bisect.insort_right(self.ret, start)
            bisect.insort_right(self.ret, end)
            self.ret_set.add((start, end))
            return True
        if self.low >= end:
            self.low = start
            bisect.insort_left(self.ret, start)
            bisect.insort_left(self.ret, end)
            self.ret_set.add((start, end))
            return True
        return self.check_in_middle(start, end)

    def check_in_middle(self, start, end):
        p = bisect.bisect_right(self.ret, start)
        if self.ret[p] >= end and (self.ret[p - 1], self.ret[p]) not in self.ret_set:
            bisect.insort_right(self.ret, start)
            bisect.insort_left(self.ret, end)
            self.ret_set.add((start, end))
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)