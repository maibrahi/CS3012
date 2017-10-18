class Node:

    #Constructor for a node
     def __init__(self, key):
         self.key = key
         self.right = None
         self.left = None

def insert(root, node):
    if root is None:
        root = node

    else:
        if root.key < node.key:
            if root.right is None:
                root.right = node

            else:
                insert(root.right, node)

        else:
            if root.left is None:
                root.left = node

            else:
                insert(root.left, node)


def traverse(root, path, k):
    # base case
    if root is None:
        return False

    path.append(root.key)

    if root.key == k:
        return True

    if ((root.left != None and traverse(root.left, path, k)) or (root.right != None and traverse(root.right, path, k))):
        return True

    path.pop()
    return False


def findLCA(root, node1, node2):
    path1 = []
    path2 = []

    if (not traverse(root, path1, node1) or not traverse(root, path2, node2)):
        return -1

    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


def printBST(root):
    if root:
        printBST(root.left)
        print(root.key)
        printBST(root.right)


root = Node(50)
insert(root, Node(30))
insert(root, Node(20))
insert(root, Node(40))
insert(root, Node(70))
insert(root, Node(60))
insert(root, Node(80))

printBST(root)

print("LCA(LCA (20,40) = %d" % (findLCA(root, 20, 40)))