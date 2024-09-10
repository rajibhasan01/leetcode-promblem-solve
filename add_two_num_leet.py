class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()  # A dummy node to simplify result creation
    current = dummy
    carry = 0  # To handle sums >= 10

    while l1 or l2 or carry:
        # Get the values of the current nodes (if they exist) or 0
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate the sum and update carry
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)  # Store only the last digit
        current = current.next  # Move to the next node

        # Move to the next nodes in the input lists, if available
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next  # Return the next node of the dummy (the real result)


print(addTwoNumbers([2, 4, 3], [5, 6, 4]))
