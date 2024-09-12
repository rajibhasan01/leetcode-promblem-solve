# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If one of the lists is not empty, append it to the result
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next


# Creating the linked lists
list_1 = ListNode(1)
list_1.next = ListNode(2)
list_1.next.next = ListNode(4)

list_2 = ListNode(1)
list_2.next = ListNode(3)
list_2.next.next = ListNode(4)

# Merging the lists
solution = Solution()
merged_list = solution.mergeTwoLists(list_1, list_2)

print(merged_list.val, merged_list.next.val, merged_list.next.next.val)
