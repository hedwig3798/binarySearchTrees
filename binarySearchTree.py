class binarySearchTree:

    def __init__(self, data=None):
        self.root = data

    # 삽입 연산 ( 재귀호출 사용 )
    def insert(self, data, currentNode=None):

        if self.root is None:
            self.root = data
            return

        if currentNode is None:
            currentNode = self.root

        if data.key <= currentNode.key:
            if currentNode.left:
                self.insert(currentNode.left, data)
            else:
                currentNode.left = data

        elif data.key > currentNode.key:
            if currentNode.right:
                self.insert(currentNode.right, data)
            else:
                currentNode.right = data
