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

import time
import tracemalloc

from basic_sort_olivefoodsolutions397 import int_sort

import numpy as np

import psutil

import pytest


@pytest.fixture
def int_lists():
    return [
        [0, -9000, 11, -3],
        [3, 2, 1],
        [1, 1, 1],
        list(np.random.randint(-10, 200, 5)),
        list(np.random.randint(-10000, 10000, 150)),
        list(np.random.randint(0, 100, 10000)),
        list(np.random.randint(0, 25, 10000)),
    ]


def test_bubble(int_lists):
    for lst in int_lists:
        sorted_list = int_sort.bubble(lst.copy())
        assert sorted_list == sorted(lst)


def test_quick(int_lists):
    for lst in int_lists:
        sorted_list = int_sort.quick(lst.copy())
        assert sorted_list == sorted(lst)


def test_insertion(int_lists):
    for lst in int_lists:
        sorted_list = int_sort.insertion(lst.copy())
        assert sorted_list == sorted(lst)


def test_bubble_cpu(int_lists):
    proc = psutil.Process()
    proc.cpu_percent()

    for lst in int_lists:
        proc.cpu_percent()
        sorted_list = int_sort.bubble(lst.copy())
        cpu = proc.cpu_percent()
        print(
            "Bubble sort on list of size",
            len(lst),
            "used",
            (cpu),
            "% of the cpu",
        )
        assert sorted_list == sorted(lst)


def test_quick_runtime(int_lists):
    for lst in int_lists:
        start_time = time.perf_counter()
        sorted_list = int_sort.quick(lst.copy())
        end_time = time.perf_counter()
        print(
            "Quick sort on list of size",
            len(lst),
            "took",
            "{:.4}".format(end_time - start_time),
            "seconds",
        )
        assert sorted_list == sorted(lst)


def test_insertion_memory(
    int_lists,
):  # had to use tracemalloc since psutil was not giving any results
    for lst in int_lists:
        tracemalloc.start()
        data = lst.copy()
        sorted_list = int_sort.insertion(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(
            "Insertion sort on list of size",
            len(lst),
            "had peak memory usage of",
            "{:.4}".format(peak / (1024)),
            "KB",
        )
        assert sorted_list == sorted(lst)
