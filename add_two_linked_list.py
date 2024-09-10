from typing import Optional


class Node:
    """
    This class represent a Node for a linked list.

    Params:
        :dtype data: int
    """

    def __init__(self, data: int = 0, next=None) -> None:
        self.data: int = data
        self.next: Optional["Node"] = next


class LinkedList:
    """
    This class represent a linked list.

    Methods:
        append(data: int): Appends a value to the linked list.
        print_list(): Prints the linked list.
    """

    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, data: int) -> None:
        """
        This method adds new node in the linked list
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        """
        This method prints the linked lists.
        """
        current_node = self.head
        while current_node:
            print(current_node.data, end="->")
            current_node = current_node.next
        print("None")


class Solution(object):
    """
    This class solves the 'Add Two Numbers' problem.

    Methods:
        addTwoNumbers(l1, l2): Takes two linked lists as input and returns their sum as linked list.
    """

    def addTwoNumbers(
        self, l1: Optional[LinkedList], l2: Optional[LinkedList]
    ) -> LinkedList:
        """
        This method takes two linked lists, adds their node values,
        and returns the sum in reverse order as a linked ist.

        Params:
            :type l1: LinkedList
            :type l2: LinkedList
        """
        reminder = 0
        result_list = LinkedList()

        current_node_l1 = l1.head
        current_node_l2 = l2.head

        while current_node_l1 or current_node_l2:
            total = (
                reminder
                + (current_node_l1.data if current_node_l1 else 0)
                + (current_node_l2.data if current_node_l2 else 0)
            )
            reminder = total // 10
            result_list.append(total % 10)

            current_node_l1 = current_node_l1.next if current_node_l1 else 0
            current_node_l2 = current_node_l2.next if current_node_l2 else 0
        if reminder:
            result_list.append(reminder)
        return result_list


def main():
    list_1 = input("Enter your 1st list here, separated by comma: ")
    list_2 = input("Enter your 2nd list here, separated by comma: ")
    array_list_1 = list(map(int, list_1.split(",")))
    array_list_2 = list(map(int, list_2.split(",")))

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for num in array_list_1:
        linked_list_1.append(num)

    for num in array_list_2:
        linked_list_2.append(num)

    print("First Linked List", end=": ")
    linked_list_1.print_list()
    print("Second Linked List", end=": ")
    linked_list_2.print_list()

    solution = Solution()
    result_linked_list = solution.addTwoNumbers(linked_list_1, linked_list_2)
    print("Result Linked List", end=": ")
    result_linked_list.print_list()


if __name__ == "__main__":
    main()
