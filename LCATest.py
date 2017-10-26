import LCA
import unittest


class MyTestCase(unittest.TestCase):

    def testStandard(self):
        root = LCA.Node(1)
        root.left = LCA.Node(2)
        root.right = LCA.Node(3)
        root.left.left = LCA.Node(4)
        root.left.right = LCA.Node(5)
        root.right.left = LCA.Node(6)
        root.right.right = LCA.Node(7)
        self.assertEqual(2,LCA.findLCA(root, 4, 5, ))

    def test2Nodes(self):
        root = LCA.Node(1)
        root.left = LCA.Node(2)
        self.assertEqual(1,LCA.findLCA(root, 1, 2, ))



    def testEmpty(self):
        self.assertEqual(-1,LCA.findLCA(None, None, None, ))

    def testNotPath(self):
        root = LCA.Node(1)
        root.left = LCA.Node(2)
        root.right = LCA.Node(3)
        root.left.left = LCA.Node(4)
        self.assertEqual(-1, LCA.findLCA(root, 2, 9, ))

#            ---------------u-----------
#           |               |          |    for this DAG here the LCA of X and Y are both Z and Y
#           |               ▼          |    W and Q have no LCA
#           |    w--------->v          |
#           |    |          |          |
#           |    |-->z----- |          ▼
#           ▼    |   |      ▼          q
#           x <------       y<---------

     def testDagStandard(self):
        root = Node('u')
    w = Node('w')
    z = Node('z')
    y = Node('y')
    q = Node('q')
    x = Node('x')
    v = Node('v')
    root.children = [q,x,v]
    w.children = [v,z,x]
    v.parents = [w,root]
    v.children = [y]
    z.parents = [w]
    z.children = [y,x]
    q.parents = [root]
    q.children = [y]
    x.parents = [z,root,w]
    y.parents = [q,v,z]

    lca = LCA(root, 'x','y')

    i=0
    while (i < len(lca)):
        print"%d" % (lca[i])



if __name__ == '__main__':
    unittest.main()
