# This file is where I construct a simple unit tester that will be used to determine whether a permutation of 8 positions for the 8 queen chess pieces satisfies the 8 Queens Algorithm.

import sys


def unit_test(test_case):
    """ Pass in a boolean test called test_case. Then, print the result of the test and the line number in the file where this function was called for testing test_case."""
    line_number = sys._getframe(1).f_lineno # Get the caller's line number.
    if test_case:
        result_msg = "Test at line {0} PASSED.".format(line_number)
    else:
        result_msg = "Test at line {0} FAILED".format(line_number)
    print(result_msg)


def absolute_value(n):
    """Compute the absolute value of n. The edge case of n = 0
    deliberately returns a wrong value so we can test this test case
    to see if our unit testing function test works"""
    if n < 0:
        return -n
    elif n > 0:
        return n
    return 1


def initial_test():
    """Run a suite of tests for the absolute_value function in this module to ensure that our unit testing function test works as expected."""
    unit_test(absolute_value(6) == 6)
    unit_test(absolute_value(-23) == 23)
    unit_test(absolute_value(0) == 0)
    unit_test(absolute_value(5.23) == 3.12)
    unit_test(absolute_value(-3.12) == 3.12)

# initial_test() The third test of absolute_value(0) == 0 should return false. So should the fourth test of absolute_value(5.23) == 3.12.