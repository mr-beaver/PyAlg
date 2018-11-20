import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
    # function returns the length of a list
    def length(l):
        count = 0
        p = l
        while p:
            count += 1
            p = p.next
        return count

    # get length of both list
    len0, len1 = length(l0), length(l1)

    # make sure l0 is always the longer list
    if len1 > len0:
        l0, l1 = l1, l0

    # advance the pointer of longer list by difference of length
    for _ in range(abs(len0 - len1)):
        l0 = l0.next

    # advance both pointers to check if there is overlap
    while l0 and l1 and l0 is not l1:
        l0, l1 = l0.next, l1.next

    return l0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
