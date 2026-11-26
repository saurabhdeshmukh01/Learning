# BST using Linked List
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.cnt = 0
        self.lcnt = 0
       
    def insert(self, new_node):
        self.cnt += 1
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def del_node(self, rt, val):
        if rt is None:
            return
        if val < rt.data:
            rt.left = self.del_node(rt.left, val)
        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)
        else:
            if rt.left is None: # Node with right child only (or no child)
                self.cnt -= 1
                return rt.right
            if rt.right is None: # Node with left child only
                self.cnt -= 1
                return rt.left
            # Node with two children: find inorder successor (min in right subtree)
            temp = rt.right
            while temp.left:
                temp = temp.left
            rt.data = temp.data
            rt.right = self.del_node(rt.right, temp.data)
        return rt

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            if rt.left is None and rt.right is None:
                self.lcnt += 1
            self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    def level_order(self, rt):
        if rt is None:
            print("BST is empty")
            return
        arr = []
        cnt = 0  # for counting visited node
        level = 0
        arr.append(rt)
        while cnt < len(arr):
            node_count = len(arr) - cnt # number of nodes to be visited
            print("\n Level ", level, end = " ")
            for i in range(node_count):
                temp = arr[cnt]
                cnt += 1
                print(temp.data, end=" ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            level += 1
        print("\n Height of the tree: ",level - 1)

    def findminmax(self):
        if self.root is None:
            print("\nBST is empty")
            return
        temp = self.root
        while temp.left:
            temp = temp.left
        print("\nMin: ", temp.data)
        temp = self.root
        while temp.right:
            temp = temp.right
        print("Max: ", temp.data)

    def leafnodes(self, rt):
        if rt is None:
            return
        if rt.left is None and rt.right is None:
            print(rt.data, end=" ")
        self.leafnodes(rt.left)
        self.leafnodes(rt.right)


b1 = BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(4))
b1.insert(Node(50))

print("\nInorder: ")
b1.inorder(b1.root)
print("\nNo of nodes: ", b1.cnt)
print("\nPreorder: ")
b1.preorder(b1.root)
print("\nPostorder: ")
b1.postorder(b1.root)
print("\nLevel order: ")
b1.level_order(b1.root)
b1.findminmax()
print("\nLeaf nodes: ")
b1.leafnodes(b1.root)
b1.level_order(b1.root)
