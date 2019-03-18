class Node:
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, data):
        """
        Node constructor
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Insert new node with data
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        """
        Lookup node containing data
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def children_count(self):
        """
        Returns the number of children
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def delete(self, data):
        """
        Delete node containing data
        """
        # get node containing data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()

        if children_count == 0:
            # if node has no children, just remove it
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            else:
                self.data = None

        elif children_count == 1:
            # if node has 1 child
            # replace node with its child
            if node.left:
                n = node.left
            else:
                n = node.right
            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            else:
                self.left = n.left
                self.right = n.right
                self.data = n.data

        else:
            # if node has 2 children
            # find its successor
            parent = node
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left
            # replace node data by its successor data
            node.data = successor.data
            # fix successor's parent's child
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right

    def inorder(self):
        """
        Print tree content inorder
        """
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def remove_duplicate(self):
        """
        Removes the duplicate elements from the tree
        :return:
        """
        global elements_list
        if self.data not in elements_list:
            elements_list.append(self.data)
        else:
            self.delete(self.data)

        if self.left:
            self.left.remove_duplicate()
        if self.right:
            self.right.remove_duplicate()



if __name__ == '__main__':
    tree = Node(5)
    tree.insert(8)
    tree.insert(7)
    tree.insert(6)
    tree.insert(3)
    tree.insert(2)
    tree.insert(11)
    tree.insert(11)
    tree.insert(11)
    tree.insert(9)
    tree.insert(4)
    tree.insert(4)
    tree.insert(4)
    global elements_list
    elements_list = []
    tree.remove_duplicate()
    tree.inorder()
