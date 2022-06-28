"""
Name:
Project 2 - Hybrid Sorting - Unit Tests
CSE 331 Fall 2020
Professor Sebnem Onsay
"""

import unittest
from HybridSort import insertion_sort, merge_sort, hybrid_sort, inversions_count, find_match
from random import seed, sample, randint

"""
Here is an example of how you can generate a list of random data for your own tests.
Please write your own tests with random data before asking questions about hidden test cases.
"""
seed(345)  # change the seed to generate a new set of random numbers.
random_data = sample(range(0, 10000), 30)  # creates a list of 30 random ints in the range [0, 10000).


class Project2Tests(unittest.TestCase):

    def test_insertion_sort(self):
        # Test with basic set of integers.
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        result = data
        insertion_sort(result)
        expected = sorted(data)

        assert result == expected

        # Test with basic set of strings.
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        result = data
        insertion_sort(result)
        expected = sorted(data)

        assert result == expected

        # Test with already sorted data.
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = data
        insertion_sort(result)
        expected = data

        assert result == expected

        # Test empty.
        data = []
        result = data
        insertion_sort(result)
        expected = []

        assert result == expected

        # Check that function does not return anything
        data = [5, 6, 3, 2]
        result = insertion_sort(data)
        expected = None

        assert result == expected


    def test_merge_sort(self):
        # Test with basic set of integers.
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        result = data
        merge_sort(result)
        expected = sorted(data)

        assert result == expected

        # Test with basic set of strings.
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        result = data
        merge_sort(result)
        expected = sorted(data)

        assert result == expected

        # Test with already sorted data.
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = data
        merge_sort(result)
        expected = data

        assert result == expected

        # Test empty.
        data = []
        result = data
        merge_sort(result)
        expected = []

        assert result == expected


    def test_hybrid_sort(self):
        # Test with small threshold.
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        threshold = 2
        result = data
        hybrid_sort(result, threshold)
        expected = sorted(data)

        assert result == expected

        # Test with max threshold.
        threshold = 9
        result = data
        hybrid_sort(result, threshold)
        expected = sorted(data)

        assert result == expected

        # Test with threshold out of bounds.
        threshold = 20
        result = data
        hybrid_sort(result, threshold)
        expected = sorted(data)

        assert result == expected

        threshold = -9
        result = data
        hybrid_sort(result, threshold)
        expected = sorted(data)

        assert result == expected

        # Check that function does not return anything
        data = [5, 6, 3, 2]
        threshold = 3
        result = hybrid_sort(data, threshold)
        expected = None

        assert result == expected


    def test_inversion_count(self):
        # Even Length List
        data = [2, 4, 3, 1]
        inversions = inversions_count(data)
        assert (inversions == 4)

        data = [4, 3, 2, 1]
        inversions = inversions_count(data)
        assert (inversions == 6)

        data = [1, 2, 3, 4]
        inversions = inversions_count(data)
        assert (inversions == 0)

        # Odd Length List
        data = [2, 4, 1, 3, 5]
        inversions = inversions_count(data)
        assert (inversions == 3)

        data = [5, 4, 3, 2, 1]
        inversions = inversions_count(data)
        assert (inversions == 10)

        data = [1, 2, 3, 4, 5]
        inversions = inversions_count(data)
        assert (inversions == 0)

        # Random Tests
        seed(1130)
        data = [randint(0, 100) for _ in range(10)]
        inversions = inversions_count(data)
        assert(inversions == 30)

        in_order = sorted(data)
        in_order_inversions = inversions_count(in_order)
        assert (in_order_inversions == 0)

        reverse = sorted(data, reverse=True)
        reverse_inversions = inversions_count(reverse)
        assert (reverse_inversions == 45)

        data = [randint(0, 100) for _ in range(11)]
        inversions = inversions_count(data)
        assert (inversions == 27)

        in_order = sorted(data)
        in_order_inversions = inversions_count(in_order)
        assert (in_order_inversions == 0)

        reverse = sorted(data, reverse=True)
        reverse_inversions = inversions_count(reverse)
        assert (reverse_inversions == 55)


    def test_find_match(self):
        winnie_the_pooh_interests_ = ['Hunny', 'Playing Poohsticks', 'Adventures', 'Poems', 'Mornings']
        candidate_interests = {
            "Eeyore": ['Mornings', 'Poems', 'Adventures', 'Playing Poohsticks', 'Hunny'],
            "Piglet": ['Poems', 'Playing Poohsticks', 'Mornings', 'Adventures', 'Hunny'],
            'Tigger': ['Adventures', 'Mornings', 'Hunny', 'Poems', 'Playing Poohsticks'],
            'Rabbit': ['Playing Poohsticks', 'Hunny', 'Adventures', 'Poems', 'Mornings']
        }

        best_match = find_match(winnie_the_pooh_interests_, candidate_interests)
        assert (best_match == 'Rabbit')

        prince_charming_interests = ['one glass slipper', 'hide and seek', 'gardens', 'magic',
                                     'horseback riding', 'ruling a kingdom', 'clocks']
        candidate_interests = {
            'Drizella': ['ruling a kingdom', 'magic', 'hide and seek', 'one glass slipper',
                         'clocks', 'gardens', 'horseback riding'],
            'Anastasia': ['magic', 'one glass slipper', 'ruling a kingdom', 'gardens',
                          'clocks', 'hide and seek', 'clocks'],
            'Cinderella': ['horseback riding', 'magic', 'one glass slipper', 'clocks',
                           'gardens', 'hide and seek', 'ruling a kingdom'],
            'Princess Chelina of Zaragosa': ['ruling a kingdom', 'gardens', 'horseback riding',
                                             'magic', 'clocks', 'hide and seek', 'one glass slipper'],
            'Captain of the Guard': ['horseback riding', 'one glass slipper', 'hide and seek', 'magic',
                                     'gardens', 'clocks', 'ruling a kingdom']
        }

        best_match = find_match(prince_charming_interests, candidate_interests)
        assert (best_match == 'Captain of the Guard')

        snow_white_interests = ['cleaning after 7 dwarves', 'singing with animals', 'washing hands', 'cooking']

        candidate_interests = {
            "The Prince": ['cleaning after 7 dwarves', 'singing with animals', 'cooking', 'washing hands'],
            "Doc": ['cleaning after 7 dwarves', 'washing hands', 'cooking', 'singing with animals'],
            "Grumpy": ['cleaning after 7 dwarves', 'washing hands', 'singing with animals', 'cooking'],
            "Happy": ['washing hands', 'cleaning after 7 dwarves', 'cooking', 'singing with animals'],
            "Sleepy": ['cooking', 'washing hands', 'cleaning after 7 dwarves', 'singing with animals'],
            "Sneezy": ['cooking', 'cleaning after 7 dwarves', 'singing with animals', 'washing hands'],
            "Bashful": ['singing with animals', 'washing hands', 'cooking', 'cleaning after 7 dwarves'],
            "Dopy": ['singing with animals', 'cleaning after 7 dwarves', 'washing hands', 'cooking']
        }

        best_match = find_match(snow_white_interests, candidate_interests)
        assert (best_match == "The Prince")


if __name__ == '__main__':
    unittest.main()
