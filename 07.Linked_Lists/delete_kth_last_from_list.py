from test_framework import generic_test
from list_node import ListNode


# fix me: !! need to think more about k!!

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    dummy_head = ListNode(0, L)
    point1 = point2 = dummy_head

    # advance point2 k step first
    count = 0
    while count < k:
        point2 = point2.next
        count += 1

    # advance both point1 and point2 until point2 hit the end of the array
    while point2.next:
        point1, point2 = point1.next, point2.next

    # remove k + 1
    point1.next = point1.next.next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
