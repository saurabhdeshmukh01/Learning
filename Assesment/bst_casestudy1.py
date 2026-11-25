class Node:
    def __init__(self, product_id):
        self.id = product_id
        self.left = None
        self.right = None

class ProductBST:
    def __init__(self):
        self.root = None

    # 1. Insert product ID
    def insert(self, root, product_id):
        if root is None:
            return Node(product_id)
        if product_id < root.id:
            root.left = self.insert(root.left, product_id)
        elif product_id > root.id:
            root.right = self.insert(root.right, product_id)
        return root

    # 2 & 5. Inorder Traversal (Ascending Order)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.id, end=" ")
            self.inorder(root.right)

    # 5. Preorder Traversal
    def preorder(self, root):
        if root:
            print(root.id, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # 5. Postorder Traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.id, end=" ")

    # 3. Search for a product ID
    def search(self, root, product_id):
        if root is None:
            return False
        if root.id == product_id:
            return True
        elif product_id < root.id:
            return self.search(root.left, product_id)
        else:
            return self.search(root.right, product_id)

    # Helper to find minimum node (used in deletion and Task 6)
    def find_min_node(self, node):
        current = node
        while current and current.left is not None:
            current = current.left
        return current

    # 4. Delete a product ID
    def delete(self, root, product_id):
        if root is None:
            return root

        if product_id < root.id:
            root.left = self.delete(root.left, product_id)
        elif product_id > root.id:
            root.right = self.delete(root.right, product_id)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest in right subtree)
            temp = self.find_min_node(root.right)
            root.id = temp.id
            root.right = self.delete(root.right, temp.id)

        return root

    # 6. Find Minimum and Maximum product IDs
    def find_min(self, root):
        if root is None:
            return None
        return self.find_min_node(root).id

    def find_max(self, root):
        if root is None:
            return None
        current = root
        while current.right is not None:
            current = current.right
        return current.id


# --- Execution of Tasks ---
bst = ProductBST()
product_ids = [150, 100, 200, 75, 125, 175, 250, 60, 90, 110]

# Task 1: Create BST
for pid in product_ids:
    bst.root = bst.insert(bst.root, pid)

# Task 2: Display product IDs in ascending order
print("Product IDs in Ascending Order (Inorder):")
bst.inorder(bst.root)
print("\n")

# Task 3: Search for product ID 175
target = 175
found = bst.search(bst.root, target)
print(f"Search for Product ID {target}: {'Exists' if found else 'Does not exist'}\n")

# Task 4: Delete product ID 100
bst.root = bst.delete(bst.root, 100)
print("Deleted Product ID 100.\n")

# Task 5: Display BST using Inorder, Preorder, and Postorder traversals
print("Inorder Traversal:   ", end="")
bst.inorder(bst.root)
print("\nPreorder Traversal:  ", end="")
bst.preorder(bst.root)
print("\nPostorder Traversal: ", end="")
bst.postorder(bst.root)
print("\n")

# Task 6: Find minimum and maximum product IDs
print(f"Minimum Product ID: {bst.find_min(bst.root)}")
print(f"Maximum Product ID: {bst.find_max(bst.root)}")