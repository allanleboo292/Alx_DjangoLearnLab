from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(book.title)

def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)

def librarian_for_library(library_name):
    try:
        
        librarian = Librarian.objects.get(library=Library.objects.get(name=library_name))
        print(f"Librarian for {library_name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}")

if __name__ == "__main__":
    books_by_author('J.K. Rowling')
    books_in_library('City Library')
    librarian_for_library('City Library')
