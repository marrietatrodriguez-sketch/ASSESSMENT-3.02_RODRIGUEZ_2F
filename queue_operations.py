"""
Assessment 3.2: Linear Data Structure
Student: Rodriguez
Data Structure: Queue (FIFO - First In, First Out)

Enqueues each letter at the rear of the queue, then dequeues them
from the front one by one until the queue is empty.
"""

from collections import deque


class Queue:
    """A queue that adds at the rear and removes from the front."""

    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self.items.popleft()

    def front(self):
        """Return the front item without removing it (None if empty)."""
        if self.is_empty():
            return None
        return self.items[0]

    def rear(self):
        """Return the rear item without removing it (None if empty)."""
        if self.is_empty():
            return None
        return self.items[-1]

    def __str__(self):
        return str(list(self.items))


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

    queue = Queue()
    print("ADDING letters (enqueue operations):")
    for letter in letters:
        queue.enqueue(letter)
        print(f"  enqueue('{letter}') -> Queue state: {queue}")
    if not queue.is_empty():
        print(f"  Front: '{queue.front()}', Rear: '{queue.rear()}'")

    print("\nREMOVING letters (dequeue operations):")
    while not queue.is_empty():
        letter = queue.dequeue()
        print(f"  dequeue() -> '{letter}' -> Queue state: {queue}")

    print(f"\nFinal state: {queue}")


if __name__ == "__main__":
    main()
