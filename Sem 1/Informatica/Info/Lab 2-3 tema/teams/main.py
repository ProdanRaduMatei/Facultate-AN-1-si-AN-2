from domain.team import Teams
from infrastructure.repository import Repository

tr = Repository([Teams('A', 10, 'AI'),
                 Teams('B', 60, 'classic'),
                 Teams('C', 45, 'classic')
                 ])

print(tr)
tr.addTeam('D', 80, 'classic')
print(tr)
try:
    tr.addTeam('A', 100, 'classic')
except ValueError as e:
    print(e)

try:
    tr.addTeam('E', 101, 'classic')
except ValueError as e:
    print(e)

try:
    tr.addTeam('F', 100, 'Web development')
except ValueError as e:
    print(e)

tr.deleteTeamWithScoreBelow25(25)
print(tr)

tr.UpdateTeamByName('A', 99, 'AI')
print(tr)

try:
    tr.UpdateTeamByName('X', 65, 'classic')
except ValueError as e:
    print(e)
print(tr)
