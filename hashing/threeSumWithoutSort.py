def findTriplets(arr):
        # Your code here
        mp = {}
        n = len(arr)
        # res = []
        st = set()
        for i in range(n):
            for j in range(i+1,n):
                s = arr[i] + arr[j]
                if s not in mp:
                    mp[s] = []
                mp[s].append((i,j))
        for i in range(n):
            comp = -arr[i]
            if comp in mp:
                for idx in mp[comp]:
                    if idx[0] != i and idx[1] != i:
                        st.add(tuple(sorted([i,idx[0],idx[1]])))
        return [list(triplet) for triplet in st]
