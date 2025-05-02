from collections import deque


class MovingAverage:
    def __init__(self, size):
        self.q = deque()
        self.size = size
        self.avg = 0

    def next(self, num):
        self.q.append(num)
        self.avg += num
        if len(self.q) > self.size:
            head = self.q.popleft()
            self.avg -= head
        return sum(self.q) / len(self.q)
