class BinaryTree:
    def __init__(self,root=None):
        self.root = root
        self.left = None
        self.right = None

    def setRoot(self,root):
        self.root = root

    def getRoot(self):
        return self.root

    def insertLeft(self,left):
        if self.left == None:
            self.left = BinaryTree(left)
        else:
            newLeft = BinaryTree(left)
            newLeft.left = self.left
            self.left = newLeft

    def getLeft(self):
        return self.left

    def insertRight(self,right):
        if self.right == None:
            self.right = BinaryTree(right)
        else:
            newRight = BinaryTree(right)
            newRight.right = self.right
            self.right = newRight

    def getRight(self):
        return self.right

    def preorder(self):
        print(self.getRoot())
        if self.getLeft() != None:
            self.getLeft().preorder()
        if self.getRight() != None:
            self.getRight().preorder()

    def inorder(self):
        if self.getLeft() != None:
            self.getLeft.inorder()
        print(self.getRoot())
        if self.getRight() != None:
            self.getRight().preorder()

    def postorder(self):
        if self.getLeft() != None:
            self.getLeft().postorder()
        if self.getRight() != None:
            self.getRight().postorder()
        print(self.getRoot())

    def levelorder(self):
        if self.root == None:
            return []
        queue = [self.root]
        result = []
        while len(queue) > 0:
            level = []
            for node in range(len(queue)):
                if queue[0].left != None:
                    level.append(queue[0].left)
                if queue[0].right != None:
                    level.append(queue[0].right)
                level.append(queue.pop(0).root)
            result.append(level)
        return result
