import collections

Book = collections.namedtuple("Book", ["title", 'author'])
# collections.namedtuple("Book", "title author")

animal_farm = Book("Animal Farm", "George Orwell")
gatsby = Book(title = "The Great Gatsby", author = 'f. Scott Fitzgerald')

class Library():
    def __init__(self, *books):
        self.books = books
        self.librarians = []

    def __len__(self):
        return len(self.books)

l1 = Library(animal_farm)
l2 = Library(animal_farm, gatsby)

print(len(l1))
print(len(l2))
