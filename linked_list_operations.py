"""
Assessment 3.2: Linear Data Structure
Student: Rodriguez
Data Structure: Singly Linked List (Sequential Chaining, NULL termination)

Appends each letter as a node at the end of the list, then removes
nodes from the head one at a time until the list is empty (NULL).
"""


class Node:
    """A single node holding a value and a link to the next node."""

    def __init__(self, value):
        self.value = value
        self.next = None  # None represents NULL


class SinglyLinkedList:
    """A singly linked list that starts with its head set to NULL."""

    def __init__(self):
        self.head = None

    def append(self, value):
        """Add a new node to the end of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove_head(self):
        """Remove the first node and return its value."""
        if self.head is None:
            raise IndexError("remove from an empty list")
        removed = self.head
        self.head = self.head.next   # move head to the next node
        removed.next = None          # unlink the old head; Python frees it
        return removed.value

    def __str__(self):
        if self.head is None:
            return "NULL"
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        return " -> ".join(parts) + " -> NULL"


def get_letters(default_name="RODRIGUEZ"):
    """Ask for a name (press Enter to use the default) and return its letters."""
    try:
        name = input(f"Enter a name (press Enter for {default_name}): ").strip()
    except EOFError:
        name = ""
    if not name:
        name = default_name
    return [ch.upper() for ch in name if ch.isalpha()]


def main():
    letters = get_letters()
    print(f"\nLetters to process: {letters}\n")

    linked_list = SinglyLinkedList()
    print("ADDING letters (append to the end):")
    for letter in letters:
        linked_list.append(letter)
        print(f"  Append '{letter}' -> {linked_list}")

    print("\nREMOVING letters (from the head):")
    while linked_list.head is not None:
        letter = linked_list.remove_head()
        print(f"  Remove '{letter}' -> {linked_list}")

    print(f"\nFinal state: {linked_list}")


if __name__ == "__main__":
    main()
