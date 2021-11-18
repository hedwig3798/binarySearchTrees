class RedBlackTree:
    def __init__(self, data=None):
        self.root = data
        self.leaf = None

    def insert(self, data, currentNode=None):

        if self.root is None:
            self.root = data
            self.root.color = "B"

        if currentNode is None:
            currentNode = self.root

        if data.key <= currentNode.key:
            if currentNode.left:
                self.insert(data, currentNode.left)
            else:
                data.parent = currentNode
                currentNode.left = data

        elif data.key > currentNode.key:
            if currentNode.right:
                self.insert(data, currentNode.right)
            else:
                data.parent = currentNode
                currentNode.right = data

        self.balance(currentNode)

    def balance(self, node):
        p = node.parent

        if p is None:
            node.color = "B"
        else:
            if p.color == "R":
                gp = p.parent
                u = None

                if gp.right == p:
                    u = gp.left
                elif gp.left == p:
                    u = gp.right

                if u is not None and u.color == "R":
                    p.color, u.color = "B", "B"
                    gp.color = "R"
                    self.balance(gp)
                else:
                    if p == gp.left and p.left == node:  # LL Case
                        gp.color, p.color = p.color, gp.color
                        self.R_R(gp)
                    elif p == gp.left and p.right == node:  # LR Case
                        self.R_L(p)
                        gp.color, node.color = node.color, G.color
                        self.R_R(gp)
                    elif p == gp.right and p.right == node:  # RR Case
                        gp.color, p.color = p.color, gp.color
                        self.R_L(gp)
                    elif p == gp.right and p.left == node:  # RL Case
                        self.R_R(p)
                        gp.color, node.color = node.color, gp.color
                        self.R_L(gp)

    # 로테이션 함수 ( parent 사용 )
    def R_R(self, node):
        child = node.left
        parent = node.parent

        if child.right is not None:
            child.right.parent = node

        node.left = child.right
        node.parent = child
        child.right = node
        child.parent = parent

        if parent is None:
            self.root = child
        elif parent is not None:
            if parent.left == node:
                parent.left = child
            elif parent.right == node:
                parent.right = child

    def R_L(self, node):
        child = node.right
        parent = node.parent

        if child.left is not None:
            child.left.parent = node

        node.right = child.left
        node.parent = child
        child.left = node
        child.parent = parent

        if parent is None:
            self.root = child
        elif parent is not None:
            if parent.left == node:
                parent.left = child
            elif parent.right == node:
                parent.right = child
