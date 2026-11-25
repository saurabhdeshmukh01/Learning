class Node:
    def __init__(self, token):
        self.token = token
        self.left = None
        self.right = None

class HospitalBST:
    def __init__(self):
        self.root = None

    # 1. Insert a patient token number
    def insert(self, root, token):
        if root is None:
            return Node(token)
        if token < root.token:
            root.left = self.insert(root.left, token)
        elif token > root.token:
            root.right = self.insert(root.right, token)
        return root

    # 2. Search for a token number
    def search(self, root, token):
        if root is None:
            return False
        if root.token == token:
            return True
        elif token < root.token:
            return self.search(root.left, token)
        else:
            return self.search(root.right, token)

    # 3 & 5. Display all token numbers in sorted order (Inorder Traversal)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.token, end=" ")
            self.inorder(root.right)

    # Helper to find the minimum node (used for Task 4 and Deletion)
    def find_min_node(self, node):
        current = node
        while current and current.left is not None:
            current = current.left
        return current

    # 4. Find smallest and largest token numbers
    def find_min(self, root):
        if root is None:
            return None
        return self.find_min_node(root).token

    def find_max(self, root):
        if root is None:
            return None
        current = root
        while current.right is not None:
            current = current.right
        return current.token

    # 5. Delete a token number
    def delete(self, root, token):
        if root is None:
            return root

        if token < root.token:
            root.left = self.delete(root.left, token)
        elif token > root.token:
            root.right = self.delete(root.right, token)
        else:
            # Case 1 & 2: Node with 0 or 1 child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Node with 2 children (replace with inorder successor)
            temp = self.find_min_node(root.right)
            root.token = temp.token
            root.right = self.delete(root.right, temp.token)

        return root


# --- Execution of Tasks ---
bst = HospitalBST()
tokens = [50, 30, 70, 20, 40, 60, 80, 10]

# Task 1: Insert token numbers into BST
for t in tokens:
    bst.root = bst.insert(bst.root, t)

# Task 2: Search for token number 40
target = 40
found = bst.search(bst.root, target)
print(f"Search for token {target}: {'Found' if found else 'Not Found'}\n")

# Task 3: Display all token numbers in sorted order
print("Patient Tokens in Sorted Order:")
bst.inorder(bst.root)
print("\n")

# Task 4: Find smallest and largest token numbers
print(f"Smallest Token Number: {bst.find_min(bst.root)}")
print(f"Largest Token Number:  {bst.find_max(bst.root)}\n")

# Task 5: Delete token number 70 and display updated BST
bst.root = bst.delete(bst.root, 70)
print("Updated BST after deleting token 70 (Sorted Order):")
bst.inorder(bst.root)
print()