from domain.book import Book
from infrastructure.library import BookRepository

br = BookRepository([Book(10, 'A'),
                     Book(20, 'B'),
                     Book(30, 'C'),
                     Book(40, 'D'),
                     Book(50, 'E'),
                     Book(60, 'F'),
                     Book(60, 'G')])

br1 = BookRepository([Book(10, 'AA'),
                     Book(20, 'BB'),
                     Book(20, 'C'),
                     Book(40, 'D')])

br2 = BookRepository([Book(10, 'A'),
                     Book(20, 'B'),
                     Book(20, 'C'),])

print(br)
br.updateBook(1, 22, 'BB')
print(br)
try:
    br.updateBook(-3, 99, 'abc')
except ValueError as ve:
    print(ve)
print(br)
print(br.getBooksNumOfPagesMaximum())
assert str(br.getBooksNumOfPagesMaximum()) == "[Book(60, F), Book(60, G)]"
assert str(br1.getBooksNumOfPagesMaximum()) == "[Book(40, D)]"
assert str(br2.getBooksNumOfPagesMaximum()) == "[Book(20, B), Book(20, C)]"

print(br.getAllBooks1(1))
print(br1.getAllBooks2(2))

