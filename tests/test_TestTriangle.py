# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import pytest
from hypothesis import given, strategies as st, assume, example

from src.Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(
            classifyTriangle(3, 4, 5), "Right", "3,4,5 is a Right triangle"
        )

    def testRightTriangleB(self):
        self.assertEqual(
            classifyTriangle(5, 3, 4), "Right", "5,3,4 is a Right triangle"
        )

    def testEquilateralTriangles(self):
        self.assertEqual(
            classifyTriangle(1, 1, 1), "Equilateral", "1,1,1 should be equilateral"
        )


@pytest.mark.parametrize(
    "a,b,c",
    [
        (201, 1, 1),
        (1, 201, 1),
        (1, 1, 201),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
        (1.5, 1, 1),
        (1, 1.5, 1),
        (1, 1, 1.5),
        (None, 1, 1),
        (1, None, 1),
        (1, 1, None),
        ("a", 1, 1),
        (1, "a", 1),
        (1, 1, "a"),
    ],
)
def test_invalid_input(a, b, c):
    assert classifyTriangle(a, b, c) == "InvalidInput"


@given(
    a=st.integers(min_value=1, max_value=200),
    b=st.integers(min_value=1, max_value=200),
    c=st.integers(min_value=1, max_value=200),
)
def test_valid_input(a, b, c):
    assert classifyTriangle(a, b, c) != "InvalidInput"


@given(
    a=st.integers(min_value=1, max_value=200),
    b=st.integers(min_value=1, max_value=200),
    c=st.integers(min_value=1, max_value=200),
)
@example(a=1, b=1, c=2)
def test_not_a_triangle(a, b, c):
    assume(a + b <= c or a + c <= b or b + c <= a)
    assert classifyTriangle(a, b, c) == "NotATriangle"


@given(
    a=st.integers(min_value=1, max_value=200),
    b=st.integers(min_value=1, max_value=200),
    c=st.integers(min_value=1, max_value=200),
)
@example(a=1, b=1, c=1)
def test_valid_triangle(a, b, c):
    assume(a + b > c and a + c > b and b + c > a)
    assert classifyTriangle(a, b, c) != "NotATriangle"


@given(
    a=st.integers(min_value=1, max_value=200),
)
def test_equilateral(a):
    assert classifyTriangle(a, a, a) == "Equilateral"


@given(
    args=st.one_of(
        st.permutations((3, 4, 5)),
        st.permutations((5, 12, 13)),
        st.permutations((8, 15, 17)),
        st.permutations((7, 24, 25)),
        st.permutations((20, 21, 29)),
        st.permutations((12, 35, 37)),
        st.permutations((9, 40, 41)),
        st.permutations((28, 45, 53)),
        st.permutations((11, 60, 61)),
        st.permutations((16, 63, 65)),
        st.permutations((33, 56, 65)),
        st.permutations((48, 55, 73)),
        st.permutations((13, 84, 85)),
        st.permutations((36, 77, 85)),
        st.permutations((39, 80, 89)),
        st.permutations((65, 72, 97)),
    )
)
def test_right(args):
    assert classifyTriangle(*args) == "Right"


@given(
    a=st.integers(min_value=1, max_value=200),
    b=st.integers(min_value=1, max_value=200),
)
def test_isoceles(a, b):
    assume(a != b)
    assume(a * 2 > b)
    assert classifyTriangle(a, a, b) == "Isoceles", f"{a}, {a}, {b}"
    assert classifyTriangle(a, b, a) == "Isoceles", f"{a}, {b}, {a}"
    assert classifyTriangle(b, a, a) == "Isoceles", f"{b}, {a}, {a}"


@given(
    a=st.integers(min_value=1, max_value=200),
    b=st.integers(min_value=1, max_value=200),
    c=st.integers(min_value=1, max_value=200),
)
@example(a=2, b=4, c=3)
def test_scalene(a, b, c):
    assume(a + b > c and a + c > b and b + c > a)
    assume(a != b and b != c and a != c)
    assert classifyTriangle(a, b, c) == "Scalene"


if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()
