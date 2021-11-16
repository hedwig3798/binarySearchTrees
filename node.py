class Node:
    def __init__(self, data=None):

        # 모든 트리에 사용
        self.key = data
        self.right = None
        self.left = None

        # AVL 트리에 사용
        self.height = 0

        # RB 트리에 사용
        self.parent = None
        self.color = "R"


if __name__ == "__main__":
    print("this is node class\n")
