import LCA
import unittest


class MyTestCase(unittest.TestCase):

    def test_insert(self):
        root=LCA.Node(1)
        LCA.insert(root, LCA.Node(2))
        LCA.insert(root, LCA.Node(3))
        LCA.insert(root, LCA.Node(4))
        LCA.insert(root, LCA.Node(5))
        LCA.insert(root, LCA.Node(6))
        LCA.insert(root, LCA.Node(7))
        self.assertEqual('1,2,3,4,5,6,7',LCA.printBST(root))



if __name__ == '__main__':
    unittest.main()
