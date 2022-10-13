class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        # Overwriting the built-in __str__ method allows us to 
        # determine what will print out when you print a book object e.g.:
        #   book = Book('Vampire Academy', 'Richelle Mead')
        #   print(book)
        # ---> 'Vampire Academy - Richelle Mead'
        return f'{self.title} - {self.author}'


if __name__ == '__main__':
    # The above check allows us to write code that tests the code above,
    # that will only run if we run this file directly

    book = Book('Vampire Academy', 'Richelle Mead')
    print(book.title)
    print(book)
