**Project 5 - Priority Queues, Min/Max Heaps**
==============================================

**Due: Thursday, November 19th 8:00 pm**

*This is not a team project. Do not copy someone else's work.*

### **Assignment Overview**

![Introduction to Priority Queues using Binary Heaps - Techie Delight](https://www.techiedelight.com/wp-content/uploads/2016/11/Min-Heap.png)

*Binary Min-Heap representation as an array.  The root of the heap is the 0th-index in the array representation.  In a zero-indexed heap, the parent of a node at index i is located at floor((i - 1) / 2).  The left child and right child are located at 2 * i + 1 and 2 * i + 2, respectively.*

In this project, you will be implementing a binary max heap and priority queue using a binary min heap.  Heaps are data structures that are complete trees, with the parent of each node being smaller than its children in a min heap, and larger than its children in a max heap.  A min heap always has the element with the smallest value as its root, while a max heap always has the element with the largest value as its root. 

Because of heaps' quick access to the largest or smallest element, they are generally the best choice to use as a priority queue.  A priority queue is a data structure that has the element with the most significant priority in its top index.  You can think of it as a regular queue, but instead of simply removing the first element that was stored, it removes the most important element.

You will be using your PriorityQueue class to store Nodes, a class that is provided for you.

### **Assignment Specifications**

Node class is completed in the skeleton file. **Do not modify this class.**

Its definition includes a key and a value. The key denotes the entity determining the ordering within the heap. The value represents the content of interest **and acts as the tie breaker if the comparator keys are the same**.

The class has been provided with less than, greater than, equal to, and string representation methods. 

PriorityQueue class is partially completed in the skeleton file.

#### **PriorityQueue Class**

Method signatures and the following provided methods may **not be modified in any way.**

-   **__init__**(self)

    -   self.data - built in list that stores nodes

-   **__str__**(self)
-   **__repr__**(self)

Complete and implement the following methods. **Do not modify the method signatures.**

-   **__len__**(self)
    -   Returns the length of the PriorityQueue
    -   Time Complexity: O(1)
    -   Space Complexity: O(1)
-   **empty**(self)
    -   Checks if the priority queue is empty.
    -   Return: type Bool
    -   Time Complexity: O(1)
    -   Space Complexity: O(1)
-   **top**(self)
    -   Gets the root node
    -   Return: type Node
    -   Time Complexity: O(1)
    -   Space Complexity: O(1)
-   **get_left_child_index**(self, index)
    -   Given an index of a node, return the index of the left child. 
    -   In the event that the index has no left child, return None.
    -   Return: type int
    -   Time Complexity: O(1)
    -   Space Complexity: O(1)
-   **get_right_child_index**(self, index)
    -   Given an index of a node, return the index of the right child. 
    -   In the event that the index has no left child, return None.
    -   Return: type int
    -   Time Complexity: O(1)
    -   Space Complexity: O(1)
-   **get_parent_index**(self, index)
    -   Given an index of a node, return the index of its parent. 
    -   In the event that the index is the top of the PriorityQueue, return None.
    -   Return: type int
    -   Time Complexity: O(1)
    -   Space Complexity: O(1)
-   **push**(self, key, value)
    -   Use the key and value parameters to add a Node to the heap.
    -   Return: type None
    -   Time Complexity: O(log(N))
    -   Space Complexity: O(1)
-   **pop**(self)
    -   Removes the smallest element from the priority queue. 
    -   Reminder: **you cannot use self.data.pop(0).  **This has a runtime complexity of O(N), since after deletion, the function will shift all of the other elements down by one spot.  You must write your own PriorityQueue pop function that runs in O(log(N)).
    -   If no elements exist, return None
    -   Return: type Node
    -   Time Complexity: O(log(N))
    -   Space Complexity: O(1)
-   **get_min_child_index**(self, index)
    -   Given an index of a node, return the index of the smaller child.
    -   In the event that the index is a leaf, return None.
    -   Return: type int
    -   Time Complexity: O(1)
    -   Space Complexity: O(1)
-   **percolate_up**(self, index)
    -   Given the index of a node, move the node up to its valid spot in the heap.
    -   Return: type None
    -   Time Complexity: O(log(N))
    -   Space Complexity: O(1)
-   **percolate_down**(self, index)
    -   Given the index of a node, move the node down to its valid spot in the heap.
    -   Return: type None
    -   Time Complexity: O(log(N))
    -   Space Complexity: O(1)

**MaxHeap Class**

Method signatures and the following provided methods may **not be modified in any way.**

-   **__init__**(self)

    -   self.data -- PriorityQueue that contains the data in our MaxHeap

-   **__str__**(self)
-   **__repr__**(self)
-   **__len__**(self) - returns the length of the data inside the heap

Complete and implement the following methods. **Do not modify the method signatures.**

-   **empty**(self)

    -   Checks if the MaxHeap is empty.
    -   Return: type Bool
    -   Time Complexity: O(1)
    -   Space Complexity: O(1)

-   **top**(self)

    -   If no root value, return None.
    -   Gives the root value.
    -   Return: type same as node.value
    -   Time Complexity: O(1)
    -   Space Complexity: O(1)

-   **push**(self, value)

    -   Adds the value to the heap
    -   Return: type None
    -   Time Complexity: O(log(N))
    -   Space Complexity: O(1)

-   **pop**(self)

    -   If no elements exist, return None
    -   Removes the largest element from the heap
    -   Return: type Node
    -   Time Complexity: O(log(N))
    -   Space Complexity: O(1)

### **Application Problems**

**heap_sort**(array)

-   Sorts the given list **in-place**, in ascending order, using a MaxHeap
    -   This means that you are not allowed to create a new list and append values onto it.  You must modify the original array.
-   Return: type None; list should be sorted
-   Time Complexity: O(Nlog(N))
-   Space Complexity: O(N) **for MaxHeap, not allowed to create other list.**
-   **CREATING A NEW LIST WILL RESULT IN ZERO POINTS ON THIS FUNCTION**

**find_ranking**(rank, results)

Unfortunately, the NCAA has lost the information regarding the rankings of the teams at the end of the season.  They could figure it out, but knowing you have created a PriorityQueue class, they have hired you to do it more quickly and efficiently.  Given "results", a list of tuples -- with each tuple containing the amount of losses that team suffered and the team name - find the team that finished in the position "rank". 

You may assume that each team played the same amount of games in the given season.\
No two teams will have the same amount of losses in a season.

Example:\
rank = 3, results = [(1, "Spartans"), (11, "Hoosiers"), (3, "Buckeyes"), (6, "Wolverines"), (5, "Golden Gophers"), (15, "Nittany Lions"), (7, "Badgers"), (12, "Scarlet Knights")]

Return: "Golden Gophers"

Explanation: The Golden Gophers finished in 3^rd^ place, because they had the 3^rd^ least amount of losses (the Spartans (1) and the Buckeyes (3) had less). 

You **must use the PriorityQueue** class to solve this problem.

Time Complexity: O(Nlog(N))\
Space Complexity: O(N)

### **Assignment Notes**

-   **No use of the module heapq allowed.**
-   **The Node class has built-in comparator functions, meaning you can check if one Node is less than or greater than another.**
-   You must write docstrings for every completed function.
-   The only containers allowed are the built-in priority queue containers and lists to be used in the heap_sort function.
-   Guaranteed that no duplicate nodes will be pushed into the heap, meaning same key and value.
-   Keys and values **for the PriorityQueue class** can be ints, strings, or floats.
-   Values will only be ints **for the MaxHeap class**
-   String and print methods are provided for debugging purposes.
-   Some heaps start at an index at one. However, for this assignment, **indexing will start at index zero**, just like normal lists.

**Submission**
--------------

#### **Deliverables**

Be sure to upload the following deliverables in a .zip folder to Mimir by 8:00p Eastern Time on Thursday, 11/19/20.

Project5.zip\
    |--- Project5/\
        |--- README.md       (for project feedback)\
        |--- __init__.py        (for proper Mimir testcase loading)\
        |--- PriorityHeap.py (contains your solution source code)

**Grading**

-   **Mimir Tests (76]**
-   **Manual (24)**
    -   ReadMe **(2)** 
    -   Time and Space Complexity
        -   length, top, empty, get_left_child_index, get_right_child_index, get_parent_index **__ / 3** *(0.5 pts each)*
        -   get_min_child_index **__ / 1**
        -   push, pop, percolate_up, percolate_down **__ / 8** *(2 pts each)*
        -   heap_sort **__ / 5**
        -   find_ranking **__ / 5**

Project designed by Max Huang and Angelo Savich