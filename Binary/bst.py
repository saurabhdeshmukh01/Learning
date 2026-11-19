class NOde:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Bst:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = NOde(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, current_node, value):
        if value < current_node.data:
            if current_node.left is None:
                current_node.left = NOde(value)
            else:
                self._insert_recursively(current_node.left, value)
        elif value > current_node.data:
            if current_node.right is None:
                current_node.right = NOde(value)
            else:
                self._insert_recursively(current_node.right, value)

    def inorder_traversal(self):
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        if node is not None:
            self._inorder_helper(node.left, result)
            result.append(node.data)
            self._inorder_helper(node.right, result)

btree = Bst()
btree.insert(10)
btree.insert(20)
btree.insert(30)
btree.insert(17)
btree.insert(28)
btree.insert(32)
btree.insert(23)
btree.insert(64)
btree.insert(92)
print("Inorder Traversal of the Binary search tree:", btree.inorder_traversal())