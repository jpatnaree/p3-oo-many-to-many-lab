class Author:

    all = []

    def __init__(self, name = ""):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        return [ c for c in Contract.all if c.author == self]
    
    def books(self):
        return [ c.book for c in Contract.all if c.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total = [c.royalties for c in Contract.all if c.author == self]
        return sum(total)

class Book:

    all = []

    def __init__(self, title =""):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [ c for c in Contract.all if c.book == self]

    def authors(self):
        return [c.author for c in Contract.all if c.book == self]

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.date = date
        self.royalties = royalties
        self.author = author
        self.book = book
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise Exception('')
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, new_book):
        if isinstance(new_book, Book):
            self._book = new_book
        else:
            raise Exception('')
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, new_date):
        if isinstance(new_date, str):
            self._date = new_date
        else:
            raise Exception('')
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, new_ro):
        if isinstance(new_ro, int):
            self._royalties = new_ro
        else:
            raise Exception('')
        
    @classmethod    
    def contracts_by_date(cls, date):
        
        c = [c for c in Contract.all if c.date == date]
        
        return sorted(c, key = lambda contract: contract.date)
    