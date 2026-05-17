class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def preOrder(self):
        if self is None:
            return
        print(self.data, end=", ")
        self.preOrder(self.left)
        self.preOrder(self.right)

    def inOrder(self):
        if self is None:
            return
        self.inOrder(self.left)
        print(self.data, end=", ")
        self.inOrder(self.right)

    def postOrder(self):
        if self is None:
            return
        self.postOrder(self.left)
        self.postOrder(self.right)
        print(self.data, end=", ")

    def search(self, target):
        if self is None:
            return None
        elif self.data == target:
            return self
        elif target < self.data:
            return self.search(self.left, target)
        else:
            return self.search(self.right, target)




