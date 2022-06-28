"""
Name:
Project 2 - Hybrid Sorting - Starter Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""
from typing import List, Any, Dict


def hybrid_sort(data: List[Any], threshold: int) -> None:
    """
    Sorts the data using a combination of merge sort algorithm
    and insertion sort algorithm
    :param data: list of entries to be sorted
    :param threshold: size of the data at which insertion sort should be called
    """
    merge_sort(data, threshold)


def inversions_count(data: List[Any]) -> int:
    """
    Returns the number of inversions done to sort the given list
    by using the function merge_sort
    :param data: list of entries to be sorted
    :return : the number of inversions done to sort the list
    """
    return merge_sort(data)

def merge_sort(data: List[Any], threshold: int = 0) -> int:
    """
    Sorts the data using merge sort algorithm
    :param data: list of entries to be sorted
    :param threshold: size of the data at which insertion sort should be called
    :return : the value of inversion count if threshold > 0
    """
    if len(data) < 2:
        return 0
    mid = len(data) // 2  # Finding the mid of the array
    left_list = data[:mid]  # Dividing the array elements
    right_list = data[mid:]  # into 2 halves
    inversion_count = 0

    if(len(left_list)) < threshold:
        insertion_sort(data)
        return 0
    inversion_count += merge_sort(left_list)  # Sorting the first half
    inversion_count += merge_sort(right_list)  # Sorting the second half
    inversion_count += merge(left_list, right_list, data)
    return inversion_count

def merge(left_list, right_list, data):
    """
    Merges two sorted lists into one sorted list and counts the number of inversions
    :param left_list: the first list to be merged
    :param right_list: the second list to be merged
    :param data: the main list that needs to be sorted
    :return inversion_count: the number of inversions
    """
    inversion_count = 0
    i = j = 0
    while i + j < len(data):
        if j == len(right_list) or (i < len(left_list) and left_list[i] <= right_list[j]):
            data[i + j] = left_list[i]
            i = i + 1
        else:
            data[i + j] = right_list[j]
            j = j + 1
            inversion_count += (len(left_list) - i)

    return inversion_count


def insertion_sort(data: List[Any]) -> None:
    """
    Sorts the data using insertion sort algorithm
    :param: data list of entries to be sorted
    """
    for i in range(1, len(data)):
        entry = data[i]
        j = i
        while (j > 0 and entry < data[j-1]):
            data[j] = data[j-1]
            j -= 1
        data[j] = entry

def find_match(user_interests: List[str], candidate_interests: Dict[str, List]) -> str:
    """
    Returns the name of the best matching candidate for the user in terms of their interests
    by checking which candidate's interests are closest to being in the same order as the
    user
    :param user_interests: list of interests of the user
    :param candidate_interests: dictionary of the names of the candidates
    as the key and a list of their interests stored as the value to the key
    :return : the name of the best match
    """
    user_dict = {user_interests[i]: i for i in range(0, len(user_interests))}
    for key in candidate_interests:
        new_list = []
        for i in candidate_interests[key]:
            new_list.append(user_dict[i])
        candidate_interests[key] = new_list

    min = 99999999
    for key in candidate_interests:
        inversions = inversions_count(candidate_interests[key])
        if inversions < min:
            min = inversions
            name = key
    return name
