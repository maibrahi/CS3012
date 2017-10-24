class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key = key
        self.parents = [] #can be more than 1 parent
        self.children = [] #can be more than 2 children
        self.count = 0
        self.flag = False

def LCA(root,x,y):
    lca=[]
    XNode = findNode(root,x)
    YNode = findNode(root, y)
    if(XNode.key == -1 | YNode.key == -1):
        print "invalid graph"
    elif(XNode.key == -2 | YNode.key == -2):
        print "invalid nodes"
    else:
        AncestorsFlag(XNode)
        AncestorCount(YNode)
        GetLca(root,lca)


def AncestorCount(node):
    i=0
    j=0
    if (node.flag == True):
        while (i < len(node.parents)):
            node.parents[i].count+=1
            i += 1
    while (j < len(node.parents)):
        AncestorCount(node.parents[j])
        j += 1


def GetLca(root,lca):
    i=0
    if(root.flag == True & root.count == 0):
        lca.append(root.key)
    while (i < len(root.children)):
        AncestorsFlag(root.children[i])




def AncestorsFlag(node):
    node.flag = True
    i = 0
    while (i < len(node.parents)):
        AncestorsFlag(node.parents[i])
        i+=1


def findNode(root,k):
    returnable = None
    if root is None:
        return Node(-1)
    if root.key == k:
        return root

    i = 0
    while (i < len(root.children)):
        returnable = findNode(root.children[i],k)
        i+=1
        if(returnable.key != -1 & returnable.key != -2):
            return returnable

    return Node(-2)





#    if root is None:
#        return path
#
#        # Store this node is path vector. The node will be
#        # removed if not in path from root to k
#    path.append(root.key)
#
#    # See if the k is same as root's key
#    if root.key == k:
#        return path
#
#    i = 0
#    while (i < len(root.parents):


