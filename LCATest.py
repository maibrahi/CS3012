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






if __name__ == '__main__':
    unittest.main()
