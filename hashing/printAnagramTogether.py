def anagrams(arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        map = {}
        res = []
        for i in range(len(arr)):
            # print(arr[i])
            sorted_word = "".join(sorted(arr[i]))
            # print(sorted_word)
            if sorted_word not in map:
                map[sorted_word] = len(res)
                res.append([])
            res[map[sorted_word]].append(arr[i])
        return res
        # print(map)
        # res = []
        # for k,v in map:
        #     res.append(v)
        # print(res)
