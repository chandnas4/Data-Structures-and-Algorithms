"""
Your Name
Project 4 - Tries
CSE 331 Fall 2020
Professor Sebnem Onsay
"""

from __future__ import annotations
from typing import Tuple, Dict, List


class TrieNode:
    """
    Implementation of a trie node.
    """

    # DO NOT MODIFY

    __slots__ = "children", "is_end"

    def __init__(self, arr_size: int = 26) -> None:
        """
        Constructs a TrieNode with arr_size slots for child nodes.
        :param arr_size: Number of slots to allocate for child nodes.
        :return: None
        """
        self.children = [None] * arr_size
        self.is_end = 0

    def __str__(self) -> str:
        """
        Represents a TrieNode as a string.
        :return: String representation of a TrieNode.
        """
        if self.empty():
            return "..."
        children = self.children  # to shorten proceeding line
        return str({chr(i + ord("a")) + "*"*min(children[i].is_end, 1): children[i] for i in range(26) if children[i]})

    def __repr__(self) -> str:
        """
        Represents a TrieNode as a string.
        :return: String representation of a TrieNode.
        """
        return self.__str__()

    def __eq__(self, other: TrieNode) -> bool:
        """
        Compares two TrieNodes for equality.
        :return: True if two TrieNodes are equal, else False
        """
        if not other or self.is_end != other.is_end:
            return False
        return self.children == other.children

    # Implement Below

    def empty(self) -> bool:
        """
        Returns True if the node has no children
        :return: Returns True or False
        """
        for i in self.children:
            if i is not None:
                return False
        return True

    @staticmethod
    def _get_index(char: str) -> int:
        """
         Returns the integer index of a character in a-z or A-Z
        :param char: Character to get the index
        :return: The integer index of the character
        """
        if char >= "a" and char <= 'z':
            return ord(char)-97
        return ord(char)-65

    def get_child(self, char: str) -> TrieNode:
        """
        Retrieves and returns the child node at the integer index of the character passed
        :param char: character to get the index
        :return: The child node
        """
        if self.children[self._get_index(char)] is not None:
            return self.children[self._get_index(char)]
        return None

    def set_child(self, char: str) -> None:
        """
        Creates a new and stores it in children at the index using charcer passed
        :param char: Character to get the index
        :return: Returns None
        """
        self.children[self._get_index(char)] = TrieNode()

    def delete_child(self, char: str) -> None:
        """
        Deletes the child node at the index of the character passed
        :param char: Character to get the index
        :return: Returns None
        """
        self.children[self._get_index(char)] = None


class Trie:
    """
    Implementation of a trie.
    """

    # DO NOT MODIFY

    __slots__ = "root", "unique", "size"

    def __init__(self) -> None:
        """
        Constructs an empty Trie.
        :return: None.
        """
        self.root = TrieNode()
        self.unique = 0
        self.size = 0

    def __str__(self) -> str:
        """
        Represents a Trie as a string.
        :return: String representation of a Trie.
        """
        return "Trie Visual:\n" + str(self.root)

    def __repr__(self) -> str:
        """
        Represents a Trie as a string.
        :return: String representation of a Trie.
        """
        return self.__str__()

    def __eq__(self, other: Trie) -> bool:
        """
        Compares two Tries for equality.
        :return: True if two Tries are equal, else False
        """
        return self.root == other.root

    # Implement Below

    def add(self, word: str) -> int:
        """
        Adds word to the trie data structure
        :param word: word to be inserted
        :return: Returns the frequency of the word in the trie
        """
        for_is_end = 0

        def add_inner(node: TrieNode, index: int) -> int:
            nonlocal for_is_end
            if index < len(word):
                if node.get_child(word[index]) is None:
                    node.set_child(word[index])
                add_inner(node.get_child(word[index]), index + 1)
            else:
                node.is_end += 1
                for_is_end = node

        add_inner(self.root, 0)
        self.size += 1
        if for_is_end.is_end == 1:
            self.unique += 1
        return for_is_end.is_end

    def search(self, word: str) -> int:
        """
        Searches for the word in the trie
        :param word: Word to be found
        :return: The number of times a word exists in the trie
        """
        def search_inner(node: TrieNode, index: int) -> int:
            if index < len(word):
                if node.get_child(word[index]):
                    return search_inner(node.get_child(word[index]), index + 1)
                return 0
            return node.is_end
        return search_inner(self.root, 0)

    def delete(self, word: str) -> int:
        """
        Deletes the the word to be deleted from the trie data structure
        :param word: The word to be deleted
        :return: The number of times the word existed in the trie
        """

        def delete_inner(node: TrieNode, index: int) -> Tuple[int, bool]:
            if node:
                if index == len(word):
                    deletion_times = node.is_end
                    node.is_end = 0
                    self.unique -= 1
                    if node.empty():
                        return deletion_times, True
                    return deletion_times, False
                if index < len(word):
                    child_tracker = delete_inner(node.get_child(word[index]), index + 1)
                    if child_tracker[1]:
                        node.delete_child(word[index])
                        if node.empty() and node.is_end == 0:
                            return child_tracker[0], True
                    return child_tracker[0], False
        if word == "":
            return 0
        if self.search(word) == 0:
            return 0
        count = delete_inner(self.root, 0)[0]
        self.size -= count
        return count

    def __len__(self) -> int:
        """
        Returns the total number of words  in the vocabulary
        :return: Return total words
        """
        return self.size

    def __contains__(self, word: str) -> bool:
        """
        Checks if the word exists in the trie
        :param word: Word to check
        :return: Returns True if word is stored in Trie, else False.
        """
        if self.search(word) == 0:
            return False
        return True

    def empty(self) -> bool:
        """
        Checks if the vocabulary is empty or not
        :return: Returns True if vocabulary of Trie is empty, else False..
        """
        if self.size == 0:
            return True
        return False

    def get_vocabulary(self, prefix: str = "") -> Dict[str, int]:
        """
        Returns a dictionary of (word, count) pairs with words beginning with prefix.
        :param prefix: The prefix from which the words need to start from
        :return: A dictionary of (word, count) pairs
        """

        def get_vocabulary_inner(node, suffix):
            if node is not None:
                for index in range(len(node.children)):
                    new_suffix = suffix + chr(index+97)
                    get_vocabulary_inner(node.children[index], new_suffix)

                if node.is_end > 0:
                    key = prefix+suffix
                    dictionary_vocab[key] = node.is_end

        dictionary_vocab = {}
        if prefix == "":
            get_vocabulary_inner(self.root, "")
            return dictionary_vocab
        node = self.root
        for index in range(len(prefix)):
            if node.get_child(prefix[index]) is None:
                return {}
            node = node.children[node._get_index(prefix[index])]
        get_vocabulary_inner(node, "")
        return dictionary_vocab

    def autocomplete(self, word: str) -> Dict[str, int]:
        """
        Completes the template of word in the Trie
        :param word: Param description here.
        :return: Returns a dictionary of (word, count) pairs
        """
        def assign_dictionary(node, prefix, index):
            if length == len(prefix):
                autocomplete_dictionary[prefix] = node.is_end
            elif prefix[len(prefix) - 1] == word[length - 1]:
                autocomplete_dictionary[prefix] = node.is_end
            elif word[index - 1] == '.':
                autocomplete_dictionary[prefix] = node.is_end
            else:
                return

        def autocomplete_inner(node, prefix, index):
            length_pre = len(prefix)
            if node is not None:
                if index < len(word):
                    if word[index] != '.':
                        if node.is_end > 0 and length_pre == length:
                            if word[index] == prefix[length_pre - 1]:
                                autocomplete_dictionary[prefix] = node.is_end
                        prefix = prefix + word[index]
                        autocomplete_inner(node.get_child(word[index]), prefix, index + 1)
                        return
                    for i in range(len(node.children)):
                        autocomplete_inner(node.children[i], prefix + chr(i+97), index + 1)
                    return
                if node.is_end:
                    assign_dictionary(node, prefix, index)
                return

        autocomplete_dictionary = {}
        length = len(word)
        autocomplete_inner(self.root, "", 0)
        return autocomplete_dictionary


class TrieClassifier:
    """
    Implementation of a trie-based text classifier.
    """

    # DO NOT MODIFY

    __slots__ = "tries"

    def __init__(self, classes: List[str]) -> None:
        """
        Constructs a TrieClassifier with specified classes.
        :param classes: List of possible class labels of training and testing data.
        :return: None.
        """
        self.tries = {}
        for cls in classes:
            self.tries[cls] = Trie()

    @staticmethod
    def accuracy(labels: List[str], predictions: List[str]) -> float:
        """
        Computes the proportion of predictions that match labels.
        :param labels: List of strings corresponding to correct class labels.
        :param predictions: List of strings corresponding to predicted class labels.
        :return: Float proportion of correct labels.
        """
        correct = sum([1 if label == prediction else 0 for label, prediction in zip(labels, predictions)])
        return correct / len(labels)

    # Implement Below

    def fit(self, class_strings: Dict[str, List[str]]) -> None:
        """
        Adds every individual word in the list of strings associated with each class to the Trie
        :param class_strings: A dictionary of (class, List[str]) pairs
        :return: Returns None
        """
        for key in class_strings:
            for i in class_strings[key]:
                words = i.split()
                for word in words:
                    self.tries[key].add(word)

    def predict(self, strings: List[str]) -> List[str]:
        """
        Predicts the class of a string retrieved from the tweets in the list
        :param strings:  A list of strings (tweets) to be classified.
        :return: Returns a list of predicted classes corresponding to the input strings
        """
        list_predict = list()
        for tweet_string in strings:
            count = {}
            words = tweet_string.split()
            for word in words:
                for trie_class in self.tries:
                    if self.tries[trie_class].search(word) > 0:
                        count_val = self.tries[trie_class].search(word)/len(self.tries[trie_class])
                        if trie_class in count:
                            count[trie_class] += count_val
                        else:
                            count[trie_class] = count_val
            max_item = 0
            max_string = ""
            for key, val in count.items():
                if val > max_item:
                    max_item = val
                    max_string = key
            list_predict.append(max_string)
        return list_predict
