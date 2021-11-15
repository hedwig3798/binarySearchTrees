class binarySearchTree:

    def __init__(self, data=None):
        self.root = data

    def insert(self, data):

        if self.root is None:
            self.root = data
            return

        now = self.root

        while True:
            if now.key <= data.key:
                if now.right is None:
                    now.right = data
                    data.parent = now
                    return
                else:
                    now = now.right

            else:
                if now.left is None:
                    now.left = data
                    data.parent = now
                    return
                else:
                    now = now.left
