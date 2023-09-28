def lcaOfThreeNodesHelper(node, nodePath, root):
    # T --> O(N), S--> O(N)
    if root is None:
        return False

    nodePath.append(root)

    if root.data == node:
        return True

    leftSubtree = lcaOfThreeNodesHelper(node, nodePath, root.left)
    rightSubtree = lcaOfThreeNodesHelper(node, nodePath, root.right)

    if leftSubtree or rightSubtree:
        return True

    del nodePath[-1]
    return False



def lcaOfThreeNodes(root, node1, node2, node3):
    node1Path, node2Path, node3Path = [], [], []

    lcaOfThreeNodesHelper(node1, node1Path, root)
    lcaOfThreeNodesHelper(node2, node2Path, root)
    lcaOfThreeNodesHelper(node3, node3Path, root)

    i = 0 
    
    while (i < len(node1Path) and i < len(node2Path) and i < node3Path):
        if ( node1Path[i].data != node2Path[i].data or node1Path[i].data != node3Path[i].data or node2Path[i].data != node3Path[i].data:
            break
        i += 1
    return node1Path[i-1].data