from typing import Optional


class Node:
    """
    This class represents a node of a linked list.

    :param data: The value to be stored in the node (int).
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional[Node] = None


class LinkedList:
    """
    This class represents a singly linked list.

    Methods:
        append(data): Add a new node with the given data to the end of the linked list.
        print_list(): Print the data of all nodes in the linked list.
    """

    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, data: int) -> None:
        """
        Add new node to the end of the linked list
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
        Print data in the linked list, with each node's data followed by '-->',
        ending with None.
        """
        current_node = self.head
        while current_node:
            print(current_node.data, end="-->")
            current_node = current_node.next
        print("None")


class Solution:
    """
    This class written for add two numbers in from linked list.

    Methods:
        add_two_numbers(l1, l2): adding two reverse linked list and return the sum in reverse

        params:
        :type l1: LinkedList
        :type l2: LinkedList
        :rtype: LinkedList
    """

    def add_two_number_s(
        self, l1: Optional[LinkedList] = None, l2: Optional[LinkedList] = None
    ) -> Optional[LinkedList]:

        l1_current_node = l1.head
        l2_current_node = l2.head
        rest = 0
        result = LinkedList()

        while l1_current_node or l2_current_node:
            data = (
                rest
                + (l1_current_node.data if l1_current_node else 0)
                + (l2_current_node.data if l2_current_node else 0)
            )
            val = data % 10
            rest = data // 10
            result.append(val)
            l1_current_node = l1_current_node.next if l1_current_node else None
            l2_current_node = l2_current_node.next if l2_current_node else None
        if rest:
            result.append(rest)
        return result


def main():
    """
    This is main function
    """
    l1 = input("Enter numbers separated by commas for the first list: ")
    l2 = input("Enter numbers separated by commas for the second list: ")

    list_1 = list(map(int, l1.split(",")))
    list_2 = list(map(int, l2.split(",")))

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    # Append elements to the first linked list
    for num in list_1:
        linked_list_1.append(num)
    for num in list_2:
        linked_list_2.append(num)

    print("First Linked List:")
    linked_list_1.print_list()

    print("Second Linked List:")
    linked_list_2.print_list()

    solution = Solution()
    result_list = solution.add_two_number_s(linked_list_1, linked_list_2)
    print("Result Linked List")
    result_list.print_list()


if __name__ == "__main__":
    main()
