import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# this problem is list overlapping with possible cycle
# for better understanding need to check "is_list_cyclic" first
def overlapping_lists(l0, l1):
    # There is a brutal force solution with O(n) time and space complexity.
    # Use hash table to store the nodes and check whether newly newly traversed nodes are in the hash table already.

    # brutal force implementation
    p0 = l0
    p1 = l1

    traversed0 = {}  # use object id as an identifier to make sure key is unique
    traversed1 = {}  # need a second hash table to avoid p1 stuck in infinite loop

    # traverse list 0
    while p0:
        if id(p0) in traversed0:
            break
        else:
            traversed0[id(p0)] = True
            p0 = p0.next

    # traverse list 1 to check whether there is overlapping
    while p1:

        if id(p1) in traversed0:
            return p1
        elif id(p1) in traversed1:
            break
        else:
            traversed1[id(p1)] = True
            p1 = p1.next

    return None


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_lists_overlap.py",
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
