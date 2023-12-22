from domain.book import Books
from infrastructure.library import Repository

br = Repository([Books('DARKNESS AT NOON', 358),
                 Books('UNDER THE VOLCANO', 302),
                 Books('NATIVE SON', 411),
                 Books('SONS AND LOVERS', 239),
                 Books('LOLITA', 241),
                 ])

print(br)
br.addBook('HARRY POTTER', 500)
print(br)
try:
    br.addBook('TOM SAWYER', 100)
except ValueError as e:
    print(e)

try:
    br.addBook('EMILLY IN PARIS', 250)
except ValueError as e:
    print(e)

try:
    br.addBook('F', 100, 'Web development')
except ValueError as e:
    print(e)

br.deleteBookWithScoreBelow25(25)
print(br)

br.UpdateBookByName('A', 99, 'AI')
print(br)

try:
    br.UpdateBookByName('X', 65, 'classic')
except ValueError as e:
    print(e)
print(br)