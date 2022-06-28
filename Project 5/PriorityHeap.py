from typing import List, Tuple, Any


class Node:
    """
    Node definition should not be changed in any way
    """
    __slots__ = ['key', 'value']

    def __init__(self, k: Any, v: Any):
        """
        Initializes node
        :param k: key to be stored in the node
        :param v: value to be stored in the node
        """
        self.key = k
        self.value = v

    def __lt__(self, other):
        """
        Less than comparator
        :param other: second node to be compared to
        :return: True if the node is less than other, False if otherwise
        """
        return self.key < other.key or (self.key == other.key and self.value < other.value)

    def __gt__(self, other):
        """
        Greater than comparator
        :param other: second node to be compared to
        :return: True if the node is greater than other, False if otherwise
        """
        return self.key > other.key or (self.key == other.key and self.value > other.value)

    def __eq__(self, other):
        """
        Equality comparator
        :param other: second node to be compared to
        :return: True if the nodes are equal, False if otherwise
        """
        return self.key == other.key and self.value == other.value

    def __str__(self):
        """
        Converts node to a string
        :return: string representation of node
        """
        return '({0}, {1})'.format(self.key, self.value)

    __repr__ = __str__


class PriorityQueue:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = []

    def __str__(self) -> str:
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data)

    __repr__ = __str__

    def to_tree_format_string(self) -> str:
        """
        Prints heap in Breadth First Ordering Format
        :return: String to print
        """
        string = ""
        # level spacing - init
        nodes_on_level = 0
        level_limit = 1
        spaces = 10 * int(1 + len(self))

        for i in range(len(self)):
            space = spaces // level_limit
            # determine spacing

            # add node to str and add spacing
            string += str(self.data[i]).center(space, ' ')

            # check if moving to next level
            nodes_on_level += 1
            if nodes_on_level == level_limit:
                string += '\n'
                level_limit *= 2
                nodes_on_level = 0
            i += 1

        return string

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def __len__(self) -> int:
        """
        Returns the length of the PriorityQueue
        """
        return len(self.data)

    def empty(self) -> bool:
        """
        Checks if the priority queue is empty.
        """
        if self.data == []:
            return True
        return False

    def top(self) -> Node:
        """
        Gets the root node
        : return : Node
        """
        if self.empty() is False:
            return self.data[0]
        return None

    def get_left_child_index(self, index: int) -> int:
        """
        Returns the index of the left child
        :param index: index of the node
        :return : index of the left child
        """
        left_index = 2*index + 1
        if left_index < len(self.data):
            return left_index

    def get_right_child_index(self, index: int) -> int:
        """
        Returns the index of the right child
        :param index: index of the node
        :return : index of the right child
        """
        right_index = 2 * index + 2
        if right_index < len(self.data):
            return right_index

    def get_parent_index(self, index: int) -> int:
        """
        Returns the index of the parent
        :param index: index of the node
        :return : index of the parent
        """
        if self.empty() or self.__len__() == 1:
            return None
        return int((index - 1) / 2)

    def push(self, key: Any, val: Any) -> None:
        """
        Adds a Node to the Heap
        """
        if self.empty():
            self.data.append(Node(key, val))
        else:
            self.data.append(Node(key, val))
            self.percolate_up(len(self.data) - 1)

    def pop(self) -> Node:
        """
        Removes the smallest element from the queue
        :return : Node
        """
        if self.empty() is False:
            self.data[0], self.data[-1] = self.data[-1], self.data[0]
            item = self.data.pop()  # and remove it from the list;
            self.percolate_down(0)  # then fix new root
            return item

    def get_min_child_index(self, index: int) -> int:
        """
        Returns the index of the smallest child
        :param index: index of the node
        :return : index of the smallest child
        """
        left = self.get_left_child_index(index)
        right = self.get_right_child_index(index)
        if left is not None and right is None:
            return left
        if left is None and right is not None:
            return right
        if left is not None and right is not None:
            if self.data[left] < self.data[right]:
                return left
            return right
        return None

    def percolate_up(self, index: int) -> None:
        """
        Moves the node up to its valid spot in the heap
        """
        parent_index = self.get_parent_index(index)
        if index > 0 and self.data[index] < self.data[parent_index]:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            self.percolate_up(parent_index)

    def percolate_down(self, index: int) -> None:
        """
        Moves the node down to its valid spot in the heap
        """
        if (2*index + 1) < len(self.data):
            left = self.get_left_child_index(index)
            small_child = left
            if (2 * index + 2) < len(self.data):
                right = self.get_right_child_index(index)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self.data[small_child] < self.data[index]:
                self.data[index], self.data[small_child] = self.data[small_child], self.data[index]
                self.percolate_down(small_child)


class MaxHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = PriorityQueue()

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data.data)

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self.data)

    def print_tree_format(self):
        """
        Prints heap in bfs format
        """
        self.data.tree_format()

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def empty(self) -> bool:
        """
        Checks if the max heap is empty or not
        :return: True or False
        """
        if self.data.empty() is True:
            return True
        return False

    def top(self) -> int:
        """
        Returns the root value
        :return: root value
        """
        if self.data.empty() is False:
            return self.data.top().value
        return None

    def push(self, key: int) -> None:
        """
        Adds the value to the heap
        """
        self.data.push(key * -1, key)

    def pop(self) -> int:
        """
        Removes the largest element from the heap
        """
        return self.data.pop().value


def heap_sort(array):
    """
    Sorts the given array in ascending order
    :param array: Unsorted array
    :return : Sorted array
    """
    max_heap = MaxHeap()
    length_array = len(array)
    for item in array:
        max_heap.push(item)
    item = length_array - 1
    while item >= 0:
        array[item] = max_heap.pop()
        item -= 1
    return array


def find_ranking(rank, results: List[Tuple[int, str]]) -> str:
    rank_queue = PriorityQueue()
    for i in results:
        rank_queue.push(i[0], i[1])
    for j in range(rank-1):
        rank_queue.pop()
    node = rank_queue.pop()
    if node:
        return node.value
    return None
