from test_framework import generic_test
from list_node import ListNode


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    # L is actually the first element of the list
    # We need a dummyhead because we might need to delete the first element in the list
    # p1 and p2 has k gaps, therefore when p2 reaches end of the list p1 points to (k+1)th element from the end
    # delete p1.next will yield the result

    # make tow pointers that point to the first element of the list
    dummy_head = ListNode(0, L)
    p1 = p2 = dummy_head

    # move p2 forward k steps
    for _ in range(0, k):
        p2 = p2.next

    # move p1, p2 together till p2 hits the end of the list
    while p2.next:
        p1, p2 = p1.next, p2.next

    # delete the block after p1 is pointing to
    p1.next = p1.next.next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
