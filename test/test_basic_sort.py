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

from basic_sort_olivefoodsolutions397 import int_sort

import numpy as np

import pytest


@pytest.fixture
def int_lists():
    return [[3, 2, 1], [1, 1, 1], list(np.random.randint(-10, 200, 5))]


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
