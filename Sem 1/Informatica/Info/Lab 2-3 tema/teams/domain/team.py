# Manage teams of hackathon => Team Repository/Hackathon
#                 -> name (unique)
#                 -> score (between 0 and 100)
#                 -> category ('AI', 'classic')
# 1. Add a new team.
# 2. Delete all teams with score below 25
# 3. Update a team by name
# 4. Find teams with score above 25
# 5. Sort teams by score

class Teams:
    def __init__(self, name, score, category):
        self.__name = name
        if 100 >= score >= 0:
            self.__score = score
        else:
            raise ValueError("Score is not correct!")
        categories = ['AI', 'classic']
        if category in categories:
            self.__category = category

    @property
    def name(self):
        return self.__name
    @property
    def score(self):
        return self.__score
    @property
    def category(self):
        return self.__category

    @name.setter
    def name(self, other_name):
        self.__name = other_name
    @score.setter
    def score(self, other_score):
        self.__score = other_score
    @category.setter
    def category(self, other_category):
        self.__category = other_category

    def __repr__(self):
        return f"Team({self.__name}, {self.__score}, {self.__category})"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.__name == other.__score or self.__score == other.__score or self.__category == other.__category
