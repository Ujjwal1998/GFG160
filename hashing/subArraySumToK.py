def countSubarrays(arr, k):
        res = 0
        prefix_map = {0:1}
        prefix_sum = 0
        for i in range(len(arr)):
            prefix_sum += arr[i]
            if (prefix_sum - k) in prefix_map:
                res += prefix_map[prefix_sum - k]
            # else:
                # if prefix_sum not in prefix_map:
                #     prefix_map[prefix_sum] = 1
                # else:
                #     prefix_map[prefix_sum] += 1
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum,0) + 1
        return res
