class AVL:
    def __init__(self, data=None):
        self.root = data

    # 높이 함수
    def height(self, data):
        if data is None:
            return 0
        else:
            return data.height

    # 삽입
    def insert(self, data, currentNode=None):

        if self.root is None:
            self.root = data
            self.root.height = 0
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

        currentNode.height = max(self.height(currentNode.left), self.height(currentNode.right)) + 1
        self.balance(currentNode)

    # 양쪽 밸런스 수치 가져옴
    def BF(self, node):
        return self.height(node.left) - self.height(node.right)

    # 밸런스 맞추기
    def balance(self, node):
        if self.BF(node) > 1:
            if self.BF(node.left) < 0:
                node.left = self.R_L(node.left)
            node.left = self.R_R(node.left)

        elif self.BF(node) < -1:
            if self.BF(node.left) < 0:
                node.right = self.R_L(node.right)
            node.right = self.R_R(node.right)

        return node

    # 로테이션 함수 ( parent 사용 하지 않음 )
    def R_R(self, node):
        temp = node.left

        node.left = temp.right
        temp.right = node

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        temp.height = max(self.height(temp.right), self.height(temp.left)) + 1

        return temp

    def R_L(self, node):
        temp = node.right

        node.left = temp.left
        temp.left = node

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        temp.height = max(self.height(temp.right), self.height(temp.left)) + 1

        return temp
