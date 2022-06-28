"""
Project 3 (Fall 2020) - Red/Black Trees
Name: Shubham Chandna
"""

from __future__ import annotations
from typing import TypeVar, Generic, Callable, Generator
from Project3.RBnode import RBnode as Node
from copy import deepcopy
import queue






T = TypeVar('T')


class RBtree:
    """
    A Red/Black Tree class
    :root: Root Node of the tree
    :size: Number of Nodes
    """

    __slots__ = ['root', 'size']

    def __init__(self, root: Node = None):
        """ Initializer for an RBtree """
        # this alllows us to initialize by copying an existing tree
        self.root = deepcopy(root)
        if self.root:
            self.root.parent = None
        self.size = 0 if not self.root else self.root.subtree_size()

    def __eq__(self, other: RBtree) -> bool:
        """ Equality Comparator for RBtrees """
        comp = lambda n1, n2: n1 == n2 and ((comp(n1.left, n2.left) and comp(n1.right, n2.right)) if (n1 and n2) else True)
        return comp(self.root, other.root) and self.size == other.size

    def __str__(self) -> str:
        """ represents Red/Black tree as string """

        if not self.root:
            return 'Empty RB Tree'

        root, bfs_queue, height= self.root, queue.SimpleQueue(), self.root.subtree_height()
        track = {i:[] for i in range(height+1)}
        bfs_queue.put((root, 0, root.parent))

        while bfs_queue:
            n = bfs_queue.get()
            if n[1] > height:
                break
            track[n[1]].append(n)
            if n[0] is None:
                bfs_queue.put((None, n[1]+1, None))
                bfs_queue.put((None, n[1]+1, None))
                continue
            bfs_queue.put((None, n[1]+1, None) if not n[0].left else (n[0].left, n[1]+1, n[0]))
            bfs_queue.put((None, n[1]+1, None) if not n[0].right else (n[0].right, n[1]+1, n[0]))

        spaces = 12*(2**(height))
        ans = '\n' + '\t\tVisual Level Order Traversal of RBtree'.center(spaces) + '\n\n'
        for i in range(height):
            ans += f"Level {i+1}: "
            for n in track[i]:
                space = int(round(spaces / (2**i)))
                if not n[0]:
                    ans += ' ' * space
                    continue
                ans += "{} ({})".format(n[0], n[2].value if n[2] else None).center(space, " ")
            ans += '\n'
        return ans

    def __repr__(self) -> str:
        return self.__str__()

################################################################
################### Complete Functions Below ###################
################################################################

######################## Static Methods ########################
# These methods are static as they operate only on nodes,
# without explicitly referencing an RBtree instance

    @staticmethod
    def set_child(parent: Node, child: Node, is_left: bool) -> None:
        """
        Sets the child parameter of parent to child.
        :param is_left: Bool value if the child is left or right to the parent
        :param parent: the parent node
        :param child: the child node
        """
        if is_left == True:
            parent.left = child
        else:
            parent.right = child
        if child!=None:
            child.parent = parent



    @staticmethod
    def replace_child(parent: Node, current_child: Node, new_child: Node) -> None:
        """
        Replaces the current child with a new child.
        :param parent: the parent node
        :param current_child: the existing child of the parent to be replaced
        :param new_child: the new child of the parent
        """
        if parent.left == current_child:
            parent.left = new_child
        else:
            parent.right = new_child
        if new_child != None:
            new_child.parent = parent


    @staticmethod
    def get_sibling(node: Node) -> Node:
        """
        Returns the sibling node of the node given
        :param node: the given node
        :return : the sibling node
        """
        if node.parent:
            if node.value > node.parent.value:
                if node.parent.left:
                    return node.parent.left
                return None
            if node.parent.right:
                return node.parent.right
            return None
        return None

    @staticmethod
    def get_grandparent(node: Node) -> Node:
        """
        Returns the grandparent node of the node given
        :param node: the given node
        :return : the parent of the parent of the given node
        """
        if node.parent:
            if node.parent.parent:
                return node.parent.parent
            return None
        return None

    @staticmethod
    def get_uncle(node: Node) -> Node:
        """
        Returns the sibling of the parent node given
        :param node: the given node
        :return : the sibling of the parent node
        """
        if node.parent and node.parent.parent:
            if node.parent.value > node.parent.parent.value:
                if node.parent.parent.left:
                    return node.parent.parent.left
                return None
            if node.parent.parent.right:
                return node.parent.parent.right
            return None
        return None
 ######################## Misc Utilities ##########################

    def min(self, node: Node) -> Node:
        """
        Returns the node with the minimum value in the tree
        :param node: the given node
        :return : the node with the smallest value
        """
        if node:
            if node.left is None:
                return node

            def min_helper(node: Node):
                if node.left is None:
                    return node
                return min_helper(node.left)
            return min_helper(node.left)
        return None

    def max(self, node: Node) -> Node:
        """
        Returns the node with the maximum value in the tree
        :param node: the given node
        :return : the node with the biggest value
        """
        if node:
            if node.right is None:
                return node
            def max_helper(node: Node):
                if node.right is None:
                    return node
                return max_helper(node.right)
            return max_helper(node.right)
        return None


    def search(self, node: Node, val: Generic[T]) -> Node:
        """
        Searches the tree node with the passed value
        :param node: the node at which the tree is rooted
        :param val: the value to search for
        :return : the node with the found value
        """
        if node:
            if node.value == val:
                return node
            elif val < node.value:
                if node.left:
                    return self.search(node.left, val)
                return node
            elif val > node.value:
                if node.right:
                    return self.search(node.right, val)
                return node








 ######################## Tree Traversals #########################

    def inorder(self, node: Node) -> Generator[Node, None, None]:
        """
        Returns a generator object describing an inorder traversal of the subtree rooted at node.
        :param node: the node at which the tree/subtree is rooted
        :return : A generator describing an inorder traversal
        """
        if node:
            yield from self.inorder(node.left)
            yield node
            yield from self.inorder(node.right)


    def preorder(self, node: Node) -> Generator[Node, None, None]:
        """
        Returns a generator object describing a preorder traversal of the subtree rooted at node.
        :param node: the node at which the tree/subtree is rooted
        :return : A generator describing a preorder traversal
        """
        if node:
            yield node
            yield from self.preorder(node.left)
            yield from self.preorder(node.right)



    def postorder(self, node: Node) -> Generator[Node, None, None]:
        """
        Returns a generator object describing a postorder traversal
        :param node: the node at which the tree/subtree is rooted
        :return : A generator describing a postorder traversal
        """
        if node:
            yield from self.postorder(node.left)
            yield from self.postorder(node.right)
            yield node



    def bfs(self, node: Node) -> Generator[Node, None, None]:
        """
        Returns a generator object describing a breadth first traversal
        :param node: the node at which the tree/subtree is rooted
        :return : A generator describing a breadth first traversal
        """
        if node:
            q = queue.deque()
            q.append(node)
            while len(q) > 0:
                node = q.popleft()
                yield node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)



                    ################### Rebalancing Utilities ######################

    def left_rotate(self, node: Node) -> None:
        """
        Performs a left tree rotation on the subtree rooted at node.
        :param node: the node at which the tree is rooted
        """
        right_left = node.right.left
        if node.parent != None:
            RBtree.replace_child(node.parent, node, node.right)
        else:
            self.root = node.right
            self.root.parent = None
        RBtree.set_child(node.right, node, True)
        RBtree.set_child(node, right_left, False)



    def right_rotate(self, node: Node) -> None:
        """
        Performs a right tree rotation on the subtree rooted at node.
        :param node: the node at which the tree is rooted
        """
        right_left = node.left.right
        if node.parent != None:
            RBtree.replace_child(node.parent, node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        RBtree.set_child(node.left, node, False)
        RBtree.set_child(node, right_left, True)

    def insertion_repair(self, node: Node) -> None:
        """
        Re-balances the tree by ensuring that the red-black tree properties are ensured after insertion
        :param node: the node at which the subtree is rooted
        """
        if node:
            if node.parent is None:
                node.is_red = False
                return

            if node.parent.is_red == False:
                node.is_red = True
                return
            parent = node.parent
            grandparent = self.get_grandparent(node)
            uncle = self.get_uncle(node)
            if uncle is not None and uncle.is_red == True:
                parent.is_red = False
                uncle.is_red = False
                grandparent.is_red = True
                self.insertion_repair(grandparent)
                return

            if node is parent.right and parent is grandparent.left:
                self.left_rotate(parent)
                node = parent
                parent = node.parent

            elif node is parent.left and parent is grandparent.right:
                self.right_rotate(parent)
                node = parent
                parent = node.parent
    
            parent.is_red = False
            grandparent.is_red = True
            if (node is parent.left):
                self.right_rotate(grandparent)
            else:
                self.left_rotate(grandparent)

    def prepare_removal(self, node: Node) -> None:
        """
        Re-balances the tree by ensuring that the red-black tree properties are ensured before removal of a node
        :param node: the node at which the subtree is rooted
        """

        def case_1(node):
            if node.is_red is True or node.parent is None:
                return True
            else:
                return False

        def case_2(node, sibling):
            if sibling is not None and sibling.is_red== True:
                node.parent.is_red = True
                sibling.is_red = False
                if node is node.parent.left:
                   self.left_rotate(node.parent)
                else:
                   self.right_rotate(node.parent)
                return True
            return False

        def both_child_black(node):
            if node:
                if node.left is not None and node.left.is_red == True:
                     return False
                if node.right is not None and node.right.is_red == True:
                    return False
                return True
            return True


        def case_3(node, sibling):
            if node.parent.is_red is False and both_child_black(sibling):
                if sibling:
                    sibling.is_red = True
                self.prepare_removal(node.parent)
                return True
            return False

        def case_4(node, sibling):
            if node.parent.is_red is True and both_child_black(sibling):
                node.parent.is_red = False
                if sibling:
                    sibling.is_red = True
                return True
            return False

        def non_none_red(node):
            if node is None:
                return False
            return node.is_red == True

        def none_or_black_tree(node):
            if node is None:
                return True
            return node.is_red == False




        def case_5(node, sibling):

            if non_none_red(sibling.left) and none_or_black_tree(sibling.right) and node is node.parent.left:
                sibling.is_red = True
                sibling.left.is_red = False
                self.right_rotate(sibling)
                return True
            return False

        def case_6(node, sibling):

            if none_or_black_tree(sibling.left) and non_none_red(sibling.right) and node is node.parent.right:
                sibling.is_red = True
                sibling.right.is_red = False
                self.left_rotate(sibling)
                return True
            return False

        if case_1(node):
            return

        sibling = self.get_sibling(node)
        if case_2(node, sibling):
            sibling = self.get_sibling(node)
        if case_3(node, sibling):
            return
        if case_4(node, sibling):
            return
        if case_5(node, sibling):
            sibling = self.get_sibling(node)
        if case_6(node, sibling):
            sibling = self.get_sibling(node)

        sibling.is_red = node.parent.is_red
        node.parent.is_red = False
        if (node is node.parent.left):
            sibling.right.is_red = False
            self.left_rotate(node.parent)

        else:
            if sibling.left:
                sibling.left.is_red = False
            self.right_rotate(node.parent)




##################### Insertion and Removal #########################

    def insert(self, node: Node, val: Generic[T]) -> None:
        """
        Inserts a node to the subtree rooted at node with the given value
        : param node: the node at which the subtree is rooted
        : param val: the value of the node to be inserted
        """
        new = Node(val, False)
        if not self.root:
            self.root = new
            self.root.is_red = False
            self.size += 1

        if node:
            if node.value == val:
                return
            elif val < node.value:
                if node.left is None:
                    new = Node(val)
                    node.left = new
                    node.left.parent = node
                    self.size += 1
                else:
                    self.insert(node.left, val)
            else:
                if node.right is None:
                    new = Node(val)
                    node.right = new
                    node.right.parent = node
                    self.size += 1
                else:
                    self.insert(node.right, val)

        self.insertion_repair(new)


    def remove(self, node: Node, val: Generic[T]) -> None:
        """
        Removes node with the given value from the subtree rooted at node.
        : param node: the node at which the subtree is rooted
        : param val: the value of the node to be removed
        """
        def get_predecessor(node):
            if node:
                node = node.left
                while (node.right is not None):
                    node = node.right
                return node


        def BST_remove(found_node):
            if found_node is None:
                return
            if found_node.right is None and found_node.left is None:
                par = found_node.parent
                if par is None:
                    self.root = None
                elif par.right is not None and par.right.value == found_node.value:
                    par.right = None
                else:
                    par.left = None
                self.size -= 1
                return

            if found_node.right is None or found_node.left is None:
                par = found_node.parent
                if found_node.right is not None:
                    child = found_node.right
                else:
                    child = found_node.left
                if par is None:
                    self.root= child
                elif par.right is not None and par.right.value == found_node.value:
                    par.right = child
                else:
                    par.left = child
                self.size -= 1
                child.parent =par
                return

            min_right = self.min(found_node.right)
            if min_right:
                BST_remove(min_right)
                found_node.value = min_right.value

        node_1 = self.search(node, val)
        if node_1:
            flag = 0
            if node_1.left is not None and node_1.right is not None:
                predecessor_node = get_predecessor(node_1)
                predecessor_val = predecessor_node.value
                self.remove(predecessor_node,predecessor_val)
                node_1.value = predecessor_val
                return
            if (node_1.is_red is False):
                self.prepare_removal(node_1)
            if node_1 is self.root:
                flag = 1
            BST_remove(node_1)
            if flag == 1 and self.root is not None:
                self.root.is_red = False
                self.root.parent = None
            if self.root:
                if self.root.left is None and self.root.right is not None:
                    if self.root.right.left is None and self.root.right.left is None:
                        self.root.right.is_red = True
                if self.root.right is None and self.root.left is not None:
                    if self.root.left.right is None and self.root.left.left is None:
                        self.root.left.is_red = True
