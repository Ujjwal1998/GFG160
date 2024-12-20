def insertInterval(intervals, newInterval):
        res = []
        idx = 0
        n = len(intervals)
        while idx < n and intervals[idx][1] < newInterval[0]:
            res.append(intervals[idx])
            idx += 1
        while idx < n and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(intervals[idx][0], newInterval[0])
            newInterval[1] = max(intervals[idx][1], newInterval[1])
            idx += 1
        res.append(newInterval)
        while idx < n:
            res.append(intervals[idx])
            idx += 1
        return res
