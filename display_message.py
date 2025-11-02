"""Module to display a message."""

def display_message(message: str) -> None:
    """Print the provided message to stdout."""
    print(message)

from typing import List
import sys

def select_books_category(category: str) -> List[str]:
    """Return a list of books for the given category using match/case (Python 3.10+)."""
    category_key = category.strip().lower()
    match category_key:
        case "fiction":
            return ["The Great Gatsby", "To Kill a Mockingbird", "1984"]
        case "nonfiction" | "non-fiction" | "non fiction":
            return ["Sapiens", "Educated", "The Wright Brothers"]
        case "science":
            return ["A Brief History of Time", "The Selfish Gene", "The Gene"]
        case "history":
            return ["Guns, Germs, and Steel", "The Silk Roads", "The Diary of a Young Girl"]
        case "children" | "kids":
            return ["Charlotte's Web", "Where the Wild Things Are", "Matilda"]
        case "poetry":
            return ["Leaves of Grass", "The Collected Poems of W.B. Yeats", "The Waste Land"]
        case _:
            return []

def show_books(category: str) -> None:
    """Display books for a category using display_message."""
    books = select_books_category(category)
    if books:
        display_message(f"Books in '{category}':")
        for b in books:
            display_message(f" - {b}")
    else:
        display_message(f"No books found for category: {category}")

if __name__ == "__main__":
    # If a category is passed as the first CLI argument, show that; otherwise demo a few.
    if len(sys.argv) > 1:
        show_books(sys.argv[1])
    else:
        for cat in ["Fiction", "Science", "Poetry", "Unknown"]:
            show_books(cat)