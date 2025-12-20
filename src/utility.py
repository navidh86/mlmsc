class Queue:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.insert(0, item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0

def find_lca(tree, nodes):
    names = set([node.name for node in nodes])
    for node in tree.postorder():
        if node.is_tip():
            tips = set([node.name])
        else:
            tips = set([x.name for x in node.tips()])
        if tips.issuperset(names):
            return node.name
        
    print("LCA not found for nodes:", names)
        
    return ""


def notung_string(treeNode, speciesTree):
    if hasattr(treeNode, 'eventType'):
        if treeNode.eventType == 'loss':    
            if not treeNode.is_tip():
                lca = find_lca(speciesTree, treeNode.tips())
            else:
                lca = treeNode.name

            return lca + "*LOST" + f"[&&NHX:S={lca}:NT-L=Y]"

    if treeNode.is_tip():
        return treeNode.name + f"[&&NHX:S={treeNode.name}:B={treeNode.length}]"
    
    tree = "("
    for i, child in enumerate(treeNode.children):
        tree += notung_string(child, speciesTree)
        if i != len(treeNode.children) - 1:
            tree += ","
    tree += ")"

    tree += f"[&&NHX:S={find_lca(speciesTree, treeNode.tips())}"

    if hasattr(treeNode, 'eventType'):
        if treeNode.eventType == 'duplication':
            tree += ":D=Y"

    if treeNode.is_root():
        tree += "];\n"
    else:
        tree += f":B={treeNode.length}]"
    return tree
        