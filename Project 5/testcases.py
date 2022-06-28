import unittest
from PriorityHeap import Node, PriorityQueue, heap_sort, MaxHeap, find_ranking
from string import ascii_lowercase
from random import seed
from random import randint

seed(5)


class TestProject5(unittest.TestCase):
    def test_accessors(self):
        '''
        Tests the accessors (length, empty, top, get_left_child_index, 
        get_right_child_index, get_parent_index).  The other functions rely 
        on this one for testing.  Make sure you pass this test before attempting
        to move on to the other tests.
        '''

        # Heap with one element is empty, has no top element, and has a length of 0
        heap = PriorityQueue()
        self.assertEqual(True, heap.empty())
        self.assertEqual(None, heap.top())
        self.assertEqual(0, len(heap))

        # Heap with one element is not empty, has a top, which has no right, left, or parent.
        heap.data = [Node(4, '331')]
        self.assertEqual(False, heap.empty())
        self.assertEqual(heap.data[0], heap.top())
        self.assertEqual(None, heap.get_left_child_index(0))
        self.assertEqual(None, heap.get_right_child_index(0))
        self.assertEqual(None, heap.get_parent_index(0))
        self.assertEqual(1, len(heap))

        heap.data = [Node(1, '231'), Node(4, '331')]
        self.assertEqual(1, heap.get_left_child_index(0))  # Root's left child is at index 1
        self.assertEqual(None, heap.get_right_child_index(0))  # Root has no right child
        self.assertEqual(0, heap.get_parent_index(1))  # Node at index 1 has its parent at index 0
        self.assertEqual(2, len(heap))  # Length of heap is 2

        heap.data = [Node(1, '231'), Node(2, '232'), Node(3, '260'), Node(4, '331'), Node(5, '431')]
        self.assertEqual(3, heap.get_left_child_index(1))
        self.assertEqual(4, heap.get_right_child_index(1))  # Nodes at 3 and 4 have parent at index 1
        self.assertEqual(1, heap.get_parent_index(3))
        self.assertEqual(1, heap.get_parent_index(4))  # Node at 1 has children at 3 and 4
        self.assertEqual(5, len(heap))  # Length of heap is 5


    def test_push_priority_queue_basic(self):
        """
        simple push cases, requires functioning acccessors and percolates
        """
        heap = PriorityQueue()
        heap.push(5, 'o')
        heap.push(4, 'n')
        heap.push(3, 's')
        heap.push(2, 'a')
        heap.push(5, 'y')


        self.assertEqual(5, len(heap.data))  # Length of heap is 5
        self.assertEqual(heap.data[0], min(heap.data[:5]))  # The element at the top of the heap is the minimum element
        self.assertLess(heap.data[1], heap.data[3])
        self.assertLess(heap.data[1], heap.data[4])  # Node at index 1 is less than its children

        heap.push(6, 'y')
        self.assertLess(heap.data[2], heap.data[5])  # Node at index 2 is less than Node at index 5

    def test_push_priority_queue_advanced(self):
        """
        more complicated push cases, requires functioning accessors and percolates
        """
        # Large input
        heap = PriorityQueue()
        for i in range(100000):
            heap.push(i, i)

        for i in range(49999):
            # Assert that for each Node in the heap, the children of the node are greater than itself
            self.assertLess(heap.data[i], heap.data[heap.get_left_child_index(i)])
            self.assertLess(heap.data[i], heap.data[heap.get_right_child_index(i)])

        # All values have same key; nodes should be sorted by value
        heap = PriorityQueue()
        for i in range(100):
            heap.push(5, i)

        for i in range(49):
            self.assertLess(heap.data[i], heap.data[heap.get_left_child_index(i)])
            self.assertLess(heap.data[i], heap.data[heap.get_right_child_index(i)])

        # String values should operate the same way
        heap = PriorityQueue()
        for letter in ascii_lowercase:
            heap.push(letter, letter)

        for i in range(12):
            self.assertLess(heap.data[i], heap.data[heap.get_left_child_index(i)])
            self.assertLess(heap.data[i], heap.data[heap.get_right_child_index(i)])

    def test_pop_basic(self):
        """
        simple pop cases, requires accessors, push, and percolates
        """
        # test 1: tests pop returns the root
        heap = PriorityQueue()
        heap.push(5, 'a')
        heap.push(4, 'p')
        heap.push(3, 'p')
        heap.push(2, 'l')
        heap.push(5, 'e')

        print(heap.data)


        # Node that should be popped is Node(2, 'l')
        self.assertEqual(Node(2, 'l'), heap.pop())

        # test 2: checks for length and not empty
        heap = PriorityQueue()
        heap.push(4, 'y')
        heap.push(3, 'n')
        print(heap.data)

        self.assertEqual(2, len(heap.data))
        self.assertEqual(Node(3, 'n'), heap.pop())  # Popped element is min

        self.assertEqual(1, len(heap.data))
        self.assertEqual(Node(4, 'y'), heap.pop())

        self.assertEqual(0, len(heap.data))
        self.assertEqual(None, heap.pop())  # Popping an empty heap does nothing
        self.assertEqual(0, len(heap.data))

    def test_pop_advanced(self):
        """
        Advanced pop cases, requires accessors, push, and percolates
        """
        # Large dataset
        heap = PriorityQueue()
        correct = [i for i in range(1, 100000)]
        student = list()
        for i in range(100000, 0, -1):
            heap.push(i, i)
        for _ in range(99999):
            student.append(heap.pop().key)
        self.assertEqual(correct, student)  # Minimum element is always popped first

        # Non-numeric values, same key should sort by value
        heap = PriorityQueue()
        correct = list()
        student = list()
        for key in ascii_lowercase:
            for val in ascii_lowercase:
                correct.append(Node(key, val))
                heap.push(key, val)
        correct.sort()
        for _ in range(26 * 26):
            student.append(heap.pop())
        self.assertEqual(correct, student)  # Minimum element is always popped first

    def test_min_child(self):
        """
        simple min child test, requires working get_left_child_index and get_right_child_index
        """
        heap = PriorityQueue()
        # Function can find min-child even if node has only one or no child(ren)
        heap.data.append(Node(1, 1))
        self.assertEqual(None, heap.get_min_child_index(0))

        heap.data.append(Node(2, 2))
        self.assertEqual(heap.get_left_child_index(0), heap.get_min_child_index(0))
        self.assertEqual(1, heap.get_min_child_index(0))
        self.assertEqual(None, heap.get_min_child_index(1))  # Heap only has a left child

        # Min child is left index
        heap = PriorityQueue()
        for i in range(25):
            heap.data.append(Node(i, i ** 2))
        for i in range(12):
            self.assertIsNot(None, heap.get_min_child_index(i))
            self.assertEqual(heap.get_left_child_index(i), heap.get_min_child_index(i))

        # Min child is right index
        for i in range(1, 25, 2):
            heap.data[i], heap.data[i + 1] = heap.data[i + 1], heap.data[i]
        for i in range(12):
            self.assertIsNot(None, heap.get_min_child_index(i))
            self.assertEqual(heap.get_right_child_index(i), heap.get_min_child_index(i))

    def test_push_and_pop_max_heap(self):
        """
        Testing push and pop for the max heap implementation
        """
        heap = MaxHeap()
        heap.push(5)
        heap.push(4)
        heap.push(8)
        heap.push(2)
        heap.push(6)

        expected = [8, 6, 5, 4, 2]
        for num in expected:
            self.assertEqual(num, heap.pop())

        correct = list()
        for _ in range(100000):
            random_value = randint(0, 1000000)
            heap.push(random_value)
            correct.append(random_value)

        self.assertEqual(len(correct), len(heap))
        student = list()
        for _ in range(100000):
            student.append(heap.pop())
        self.assertEqual(sorted(correct, reverse=True), student)  # Each time, the largest element is popped

    def test_top_max_heap(self):
        """
        Testing top method on max heap implementation. Requires push and pop.
        """
        heap = MaxHeap()
        self.assertEqual(None, heap.top()) # Empty heap has no top

        heap.push(3)
        heap.push(2)
        heap.push(4)
        heap.push(5)
        self.assertEqual(5, heap.top())  # Top is largest

        heap.push(6)
        self.assertEqual(6, heap.top())  # New largest is added

        heap.push(1)
        self.assertEqual(6, heap.top())

    def test_comprehensive(self):
        """
        Testing all of the heap functionality in a comprehensive test case
        """
        # test both heap basic functions and set up initial testing
        student_pqueue = PriorityQueue()
        student_max_heap = MaxHeap()

        # test top and empty
        # tests inits correctly
        self.assertEqual(True, student_pqueue.empty())
        self.assertEqual(None, student_pqueue.top())

        self.assertEqual(True, student_max_heap.empty())
        self.assertEqual(None, student_max_heap.top())

        # test top and empty, and push
        student_pqueue.push(5, 5)
        student_max_heap.push(5)
        # PQueue
        self.assertEqual(False, student_pqueue.empty())
        self.assertEqual(student_pqueue.data[0], student_pqueue.top())
        # Max
        self.assertEqual(False, student_max_heap.empty())
        self.assertEqual(5, student_max_heap.top())

        # test top and empty, and push
        student_pqueue.push(2, 2)
        student_max_heap.push(2)
        # PQueue
        self.assertEqual(student_pqueue.data[0], student_pqueue.top())
        self.assertEqual(Node(2, 2), student_pqueue.top())
        self.assertEqual(False, student_pqueue.empty())
        # Max
        self.assertEqual(5, student_max_heap.top())
        self.assertEqual(False, student_max_heap.empty())

        # Make new list equal the same as the PQueue, test
        correct = [Node(2, 2), Node(5, 5)]
        self.assertEqual(correct, student_pqueue.data)

        # Make new list equal the same as the max heap, test
        correct_max = [5, 2]
        # below also tests popping
        student_max = [student_max_heap.pop() for i in range(len(student_max_heap))]
        self.assertEqual(correct_max, student_max)

        # re-add values after popping max heap
        student_max_heap.push(5)
        student_max_heap.push(2)

        # add in alphabet with priority being letter of alphabet
        # and adding that same priority 26 times,
        # with the value being another letter in the alphabet
        for key in ascii_lowercase:
            # add key, val combos to PQueue
            for val in ascii_lowercase:
                correct.append(Node(ord(key), ord(val)))
                student_pqueue.push(ord(key), ord(val))
            # add only keys to max heap
            correct_max.append(ord(key))
            student_max_heap.push(ord(key))

        # sorting to make sure same as PQueue
        correct.sort()
        # test student
        self.assertEqual(correct, student_pqueue.data)

        # reversing for max so same as max heap
        correct_max.sort(reverse=True)
        # get max heap values and test popping
        student_max = [student_max_heap.pop() for i in range(len(student_max_heap))]
        # test student max
        self.assertEqual(correct_max, student_max)

        correct_popped = correct[:-2]  # contains all nodes popped from pQueue
        # test popping for PQueue (tested max heap above)
        correct.sort(reverse=True)  # contains nodes left on PQueue after popping
        student_popped = list()
        for _ in range(26 * 26):
            student_popped.append(student_pqueue.pop())
            correct.pop()

        # testing heap sort
        correct_popped_sorted = [ans.key for ans in correct_popped]
        temp = [ans.key for ans in student_popped]
        student_popped_sorted = heap_sort(temp)
        self.assertEqual(correct_popped_sorted, student_popped_sorted)

        # sorting so in same order as Pqueue
        correct.sort()
        # test PQueue
        self.assertEqual(correct, student_pqueue.data)
        self.assertEqual(correct_popped, student_popped)

        # clear pqueue so both queues are empty
        for i in range(len(student_pqueue)):
            student_pqueue.pop()

        test_list = [(7, 4), (5, 3), (4, 8), (3, 5), (17, 93), (14, 55), (1, 1), (2, 2), (1, 2), (55, 55)]
        for node in test_list:
            student_pqueue.push(node[0], node[1])
            student_max_heap.push(node[0])

        correct_popped = [Node(1, 1), Node(1, 2), Node(2, 2), Node(3, 5),
                          Node(4, 8), Node(5, 3), Node(7, 4), Node(14, 55),
                          Node(17, 93), Node(55, 55)]
        correct_max_popped = [55, 17, 14, 7, 5, 4, 3, 2, 1, 1]

        student_popped = list()
        student_max_popped = list()
        # pop from PQueue
        for i in range(len(student_pqueue)):
            student_popped.append(student_pqueue.pop())

        # pop from max heap and use it to create student popped list
        student_max_popped = \
            [student_max_heap.pop() for i in range(len(student_max_heap))]

        self.assertEqual(correct_popped, student_popped)
        self.assertEqual(True, student_pqueue.empty())
        self.assertEqual(correct_max_popped, student_max_popped)
        self.assertEqual(True, student_max_heap.empty())

        # heap sort test


    def test_heap_sort(self):
        """
        heap sort test
        """
        # SORTS ARRAY IN-PLACE - NOTHING TO BE RETURNED FROM FUNCTION
        array = [5, 4, 3, 2, 1]
        heap_sort(array)
        self.assertEqual([1, 2, 3, 4, 5], array)

        array = [325, 450, 231, 331, 335, 422, 260, 431, 440, 404, 480, 482, 471, 476, 232]
        correct = array[:] # Make copy of array
        heap_sort(array)
        self.assertEqual(sorted(correct), array)

        array = []
        heap_sort(array)
        self.assertEqual([], array)

        array = [1]
        heap_sort(array)
        self.assertEqual([1], array)

        correct = list()
        student = list()
        for _ in range(10000):
            random_value = randint(0, 1000000)
            correct.append(random_value)
            student.append(random_value)
        heap_sort(student)
        self.assertEqual(sorted(correct), student)


    def test_find_ranking(self):
        results = [(1, "Spartans"), (11, "Hoosiers"), (3, "Buckeyes"), (6, "Wolverines"), (5, "Golden Gophers"),
                   (15, "Nittany Lions"), (7, "Badgers"), (12, "Scarlet Knights")]

        rank = 3
        self.assertEqual("Golden Gophers", find_ranking(rank, results))

        rank = 1
        self.assertEqual("Spartans", find_ranking(rank, results))

        rank = 100
        self.assertEqual(None, find_ranking(rank, results))  # Out of bounds returns None

        teams = ["Badgers", "Spartans", "Wildcats", "Fighting Illini", "Terrapins", "Hawkeyes",
                 "Buckeyes", "Nittany Lions", "Scarlet Knights", "Michigan Wolverines", "Boilermakers",
                 "Hoosiers", "Golden Gophers", "Wildcats", "Cornhuskers"]
        used = set()
        results = list()
        current_team = 0
        while len(used) < len(teams):
            random_value = randint(0, 32) # Randomly generates values between 0 and 32
            if random_value in used: # No duplicates allowed
                continue
            used.add(random_value)
            results.append((random_value, teams[current_team]))
            current_team += 1
        correct = sorted(results, key=lambda x: x[0])

        for rank in range(1, len(teams) + 5):
            if rank <= len(teams):
                self.assertEqual(correct[rank - 1][1], find_ranking(rank, results))
            else:
                self.assertEqual(None, find_ranking(rank, results))

if __name__ == "__main__":
    unittest.main()
