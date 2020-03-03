class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self, val):
        self.root = TreeNode(val)

    def insert(self, new_val):
        if self.root:
            curr = self.root
            while curr != None:
                if new_val > curr.val:
                    if not curr.right:
                        curr.next = TreeNode(new_val)
                    else:
                        curr = curr.right
                elif new_val < curr.val:
                    if not curr.left:
                        curr.left = TreeNode(new_val)
                    else:
                        curr = curr.left
        else:
            self.root = TreeNode(new_val)

    def search(self, new_val):
        curr = self.root
        while curr != None:
            if new_val == curr.val:
                return True
            elif new_val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        return False

    def delete_leaf(self, new_val):
        if self.root:
            prev = None
            curr = self.root
            while curr:
                if new_val == curr.val:
                    if not curr.left and not curr.right:
                        if curr == prev.left:
                            prev.left = None
                        else:
                            prev.right = None
                elif new_val < curr.val:
                    prev,curr = curr,curr.left
                else:
                    prev,curr = curr,curr.right

    def traversal(self):
        if self.root:
            self.traversal(self.root.left)
            print(self.root.val)
            self.traversal(self.root.right)

    def traversal_iterative(self):
        stack = []
        curr = self.root
        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            print(curr.val)
            curr = curr.right
