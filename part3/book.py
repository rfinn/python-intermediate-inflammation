#!/usr/bin/env python

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + ' by ' + self.author

    def __eq__(self, other):
        if self.title == other.title and self.author == other.author:
            return True
        else:
            return False


class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def __len__(self):
        return len(self.books)

    def __getitem__(self, number):
        return self.books[number]

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def by_author(self, author):
        return_books = []
        for b in self.books:
            if b.author == author:
                    return_books.append(b)
        if not return_books:
            raise KeyError('Author does not exist')

        return return_books

    @property
    def titles(self):
        all_titles = []
        for b in self.books:
            all_titles.append(b.title)

        return all_titles

    @property
    def authors(self):
        all_authors = []
        for b in self.books:
            all_authors.append(b.author)

        return list(set(all_authors))

    def union(self,library):
        """ merge self and input library, removing books

        :returns a new Library containing all the books of the two provided libraries, no duplicates

        """

        allbooks = self.books

        for b in library.books:
            for a in allbooks:
                if b.__eq__(a):
                    break
            allbooks.append(b)

        # create new instance of class of Library
        new_library = Library(allbooks)

        return new_library



if __name__ == '__main__':
    book = Book('A Book', 'Me')

    print(book)

    library = Library()

    library.add_book('My First Book', 'Alice')
    library.add_book('My Second Book', 'Alice')
    library.add_book('A Different Book', 'Bob')

    print(len(library))

    book = library[2]
    print(book)

    books = library.by_author('Alice')
    for book in books:
        print(book)

    #books = library.by_author('Carol')

    print(library.titles)
    print(library.authors)

