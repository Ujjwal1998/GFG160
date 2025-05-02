def lca(node, p, q):
    seen = set()
    while p:
        seen.add(p.val)
        p = p.parent
    while q:
        if q.val in seen:
            return q
        else:
            q = q.parent
