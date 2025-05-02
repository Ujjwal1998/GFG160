def diameterOfNAryTree(root):
    diameter = 0

    def dfs(node):
        if node is None:
            return 0
        nonlocal diameter
        max_dia = 0
        second_max_dia = 0
        for child in node.children:
            h = dfs(child)
            if h > max_dia:
                second_max_dia = max_dia
                max_dia = h
            elif h < max_dia and h > second_max_dia:
                second_max_dia = h
        diameter = max(diameter, max_dia + second_max_dia)
        return 1 + max_dia
