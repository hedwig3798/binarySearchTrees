class splay:
    def __init__(self, data=None):
        self.root = data

    # 삽입
    def insert(self, data):

        node = data
        y = None
        x = self.root

        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        # splay the node
        self.splay(node)

    def splay(self, node):
        while node.parent is not None:
            if node.parent.parent is None:
                if node is node.parent.left:
                    self.R_R(node.parent)
                else:
                    self.R_L(node.parent)
            elif node is node.parent.left and node.parent is node.parent.parent.left:
                self.R_R(node.parent.parent)
                self.R_R(node.parent)
            elif node is node.parent.right and node.parent is node.parent.parent.right:
                self.R_L(node.parent.parent)
                self.R_L(node.parent)
            elif node is node.parent.right and node.parent is node.parent.parent.left:
                self.R_L(node.parent.parent)
                self.R_R(node.parent)
            else:
                self.R_R(node.parent.parent)
                self.R_L(node.parent)

    # 로테이션 함수 ( parent 사용 하지 않음 )
    def R_R(self, node):
        temp = node.left
        node.left = temp.right

        if temp.right is not None:
            temp.right.parent = node

        temp.parent = node.parent

        if node.parent is None:
            self.root = temp
        elif node is node.parent.right:
            node.parent.right = temp
        else:
            node.parent.left = temp

        temp.right = node
        node.parent = temp

    def R_L(self, node):
        temp = node.right

        if temp.left:
            temp.left.parent = node

        temp.parent = node.parent

        if node.parent is None:
            self.root = temp
        elif node is node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp
        node.right = temp.left
        temp.left = node
