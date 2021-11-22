class treaps:
    def __init__(self, data=None):
        self.root = data

    def insert(self, data, currentNode=None):

        if self.root is None:
            self.root = data
            self.root.parent = None
            return

        if currentNode is None:
            currentNode = self.root

        if data.property >= currentNode.property:
            currentParent = currentNode.parent
            data.parent = currentParent
            currentNode.parent = data

            if currentParent is not None:
                if currentNode == currentParent.right:
                    currentParent.right = data

                elif currentNode == currentParent.left:
                    currentParent.left = data

            if data.key >= currentNode.key:
                data.left = currentNode
                return

            else:
                data.right = currentNode
                return

        else:
            if data.key >= currentNode.key:
                if currentNode.right:
                    self.insert(data, currentNode.right)
                    return
                else:
                    currentNode.right = data
                    data.parent = currentNode
                    return
            else:
                if currentNode.left:
                    self.insert(data, currentNode.left)
                    return
                else:
                    currentNode.left = data
                    data.left = currentNode
                    return

        return
