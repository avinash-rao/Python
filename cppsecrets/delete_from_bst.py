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
            elif data > self.data:
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

    def inorder(self):
        """
        Print tree content inorder
        """
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def postorder(self):
        """
        Print tree content postorder
        """
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)

    def print_full_nodes(self):
        """
        To print all full nodes of the tree
        """
        if self.children_count() == 2:
            self.left.print_full_nodes()
            print(self.data)
            self.right.print_full_nodes()

    def deleteTree(self):

        """ first delete both subtrees """
        if self.left:
            self.left.deleteTree()
        if self.right:
            self.right.deleteTree()

        """ then delete the node """
        print(" Deleting node:", self.data)
        del self

    def size(self):
        if self.left is None and self.right is None:
            return 1
        if self.left is None:
            return (1 + self.right.size())
        if self.right is None:
            return (self.left.size() + 1)

        return (self.left.size() + 1 + self.right.size())

    def print_leaf_nodes(self):
        if self.children_count() == 0:
            print(self.data)
            return

        if self.left:
            self.left.print_leaf_nodes()
        if self.right:
            self.right.print_leaf_nodes()

    def print_nonleaf_nodes(self):
        if self.children_count() != 0:
            print(self.data)
            if self.left:
                self.left.print_nonleaf_nodes()
            if self.right:
                self.right.print_nonleaf_nodes()
        else:
            return

    def next_right_node(self, data):
        """
        Prints the data in the right node of the given data
        """
        node,parent = self.lookup(data)
        if node.right:
            print(node.right.data)
        else:
            print("Right node does not exist for the given key")

    # def successor(self):
    #     if self.right:
    #         return self.right.least_value()
    #     else:
    #
    #
    # def least_value(self):
    # """
    # Returns the least value present in the subtree
    # """
    #     if self.left is None:
    #         return self
    #     self.left.least_value()




if __name__ == '__main__':
    tree = Node(5)
    tree.insert(8)
    tree.insert(7)
    tree.insert(6)
    tree.insert(3)
    tree.insert(2)
    tree.insert(11)
    tree.insert(9)
    tree.insert(4)
    tree.next_right_node(7)
    # tree.print_nonleaf_nodes()
    # print(tree.size())



    # tree.print_full_nodes()
    # tree.deleteTree()
    # del tree