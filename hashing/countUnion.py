def findUnion(a, b):
        # code here
        a.sort()
        b.sort()
        ptr1 = 0
        ptr2 = 0
        res = set()
        while ptr1 < len(a) and ptr2 < len(b):
            res.add(a[ptr1])
            res.add(b[ptr2])
            if a[ptr1] < b[ptr2]:
                ptr1 += 1
            elif a[ptr1] > b[ptr2]:
                ptr2 += 1
            else:
                ptr1 += 1
                ptr2 += 1
        while ptr1 < len(a):
            # print(ptr1,len(a))
            res.add(a[ptr1])
            ptr1 += 1
        while ptr2 < len(b):
            res.add(b[ptr2])
            ptr2 += 1
        # print(res)
        return len(res)
