class Solution:
    def aggressiveCows(self, stalls, k):
        def is_possible(stalls, k, min_dist):
            count_cows = 1
            last_cow = stalls[0]
            for i in range(1, len(stalls)):
                if stalls[i] - last_cow >= min_dist:
                    count_cows += 1
                    last_cow = stalls[i]
                    if count_cows >= k:
                        return True
            return False

        n = len(stalls)
        stalls.sort()
        low = 0
        hi = stalls[-1] - stalls[0]
        res = -1
        while low <= hi:
            mid = (hi + low) // 2
            if is_possible(stalls, k, mid):
                res = mid
                low = mid + 1
            else:
                hi = mid - 1
            # print(low,hi,mid,res)
        return res
