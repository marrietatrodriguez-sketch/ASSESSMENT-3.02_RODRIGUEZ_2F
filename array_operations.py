"""
Assessment 3.2: Linear Data Structure
Student: Rodriguez
Data Structure: Array (Index-based / Direct Access)

Stores each letter of a name at its own index, then removes the
letters from left to right until the array is empty.
"""


def get_letters(default_name="RODRIGUEZ"):
    """Ask for a name (press Enter to use the default) and return its letters."""
    try:
        name = input(f"Enter a name (press Enter for {default_name}): ").strip()
    except EOFError:
        name = ""
    if not name:
        name = default_name
    return [ch.upper() for ch in name if ch.isalpha()]


def add_letters(letters):
    """Create an array of fixed size and store each letter by its index."""
    arr = [None] * len(letters)
    print("ADDING letters (index-based assignment):")
    for index, letter in enumerate(letters):
        arr[index] = letter
        print(f"  Store '{letter}' at index {index} -> {arr}")
    return arr


def remove_letters(arr):
    """Visit each index from 0 to the last index and clear that slot."""
    print("\nREMOVING letters (left to right):")
    for index in range(len(arr)):
        letter = arr[index]
        arr[index] = None
        print(f"  Remove '{letter}' from index {index} -> {arr}")
    return arr


def main():
    letters = get_letters()
    print(f"\nLetters to process: {letters}\n")

    arr = add_letters(letters)
    print(f"\nResulting state: {arr}")

    arr = remove_letters(arr)
    remaining = [item for item in arr if item is not None]
    print(f"\nFinal state: {remaining}")


if __name__ == "__main__":
    main()
