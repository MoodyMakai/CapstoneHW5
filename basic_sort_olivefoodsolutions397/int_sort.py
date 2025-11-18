# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

"""
This module provide functions to sort a list of integers in many ways.
It implements, bubble, quick, and insertion sort in their respective functions.
Pass a list of integers into any of these functions and it will sort that list.
"""


def bubble(int_list):
    """
    A function that sorts a given list of integers using bubble sort.

    :param int_list: the list of only integers to be sorted.
    """
    length = len(int_list)
    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            if int_list[j] > int_list[j + 1]:
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
                swapped = True
        if swapped is False:
            break
    return int_list


def _quick_recursive(arr_part, low, high):
    """
    A helper function for quick that allows it to be recursive.
    Not part of the api.

    :param arr_part: The partition of the list you are working on.
    :param low: The lower bound for the partition.
    :param high: The upper bound for the partition.
    """
    if low < high:
        pi = arr_part[high]
        i = low - 1
        for j in range(low, high):
            if arr_part[j] < pi:
                i += 1
                arr_part[i], arr_part[j] = arr_part[j], arr_part[i]
        arr_part[i + 1], arr_part[high] = arr_part[high], arr_part[i + 1]
        pivot = i + 1
        _quick_recursive(arr_part, low, pivot - 1)
        _quick_recursive(arr_part, pivot + 1, high)
    


def quick(int_list):
    """
    A function that sorts a given list of integers using quick sort.

    :param int_list: the list of only integers to be sorted.
    """
    low = 0
    high = len(int_list) - 1
    _quick_recursive(int_list, low, high)
    return int_list


def insertion(int_list):
    """
    A function that sorts a given list of integers using quick sort.

    :param int_list: the list of only integers to be sorted.
    """
    for i in range(1, len(int_list)):
        key = int_list[i]
        j = i - 1
        while j >= 0 and key < int_list[j]:
            int_list[j + 1] = int_list[j]
            j -= 1
        int_list[j + 1] = key
    return int_list
