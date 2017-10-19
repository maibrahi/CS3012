import LCA
import unittest


class MyTestCase(unittest.TestCase):

    def test(self):
        root = LCA.Node(1)
        root.left = LCA.Node(2)
        root.right = LCA.Node(3)
        root.left.left = LCA.Node(4)
        root.left.right = LCA.Node(5)
        root.right.left = LCA.Node(6)
        root.right.right = LCA.Node(7)
        self.assertEqual(2,LCA.findLCA(root, 4, 5, ))



if __name__ == '__main__':
    unittest.main()
