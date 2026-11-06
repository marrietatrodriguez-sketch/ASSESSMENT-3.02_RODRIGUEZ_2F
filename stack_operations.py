"""
Assessment 3.2: Linear Data Structure
Student: Rodriguez
Data Structure: Stack (LIFO - Last In, First Out)

Pushes each letter onto the stack, then pops them off one by one
until the stack is empty.
"""


class Stack:
    """A stack where the end of the list is the top of the stack."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        """Place an item on the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item on the top of the stack."""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it (None if empty)."""
        if self.is_empty():
            return None
        return self.items[-1]

    def __str__(self):
        return str(self.items)


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

    stack = Stack()
    print("ADDING letters (push operations):")
    for letter in letters:
        stack.push(letter)
        print(f"  push('{letter}') -> Stack state: {stack}")
    if not stack.is_empty():
        print(f"  Top element: '{stack.peek()}'")

    print("\nREMOVING letters (pop operations):")
    while not stack.is_empty():
        letter = stack.pop()
        print(f"  pop() -> '{letter}' -> Stack state: {stack}")

    print(f"\nFinal state: {stack}")


if __name__ == "__main__":
    main()
