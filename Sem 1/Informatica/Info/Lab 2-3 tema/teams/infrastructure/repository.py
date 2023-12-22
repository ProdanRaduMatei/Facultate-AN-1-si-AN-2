import domain.team as tm


class Repository:
    def __init__(self, TeamList=None):
        self.__TeamList = []
        if TeamList is not None:
            for team in TeamList:
                if isinstance(team, tm.Teams) and self.__isunique(team.name):
                    self.__TeamList.append(team)
                else:
                    raise ValueError("Not a Team!")

    def __isunique(self, name):
        for team in self.__TeamList:
            if team.name == name:
                return False
        return True

    def addTeam(self, name, score, category):
        """
        Add a new team.
        :param name: name
        :param score: score
        :param category: category
        :return: Team
        """
        if not self.__isunique(name):
            self.__TeamList.append(tm.Teams(name, score, category))
        else:
            raise ValueError("Name is not a name.")

    def deleteTeamWithScoreBelow25(self, scor):
        for index, teams in enumerate(self.__TeamList):
            if teams.score < scor < 25:
                del self.__TeamList[index]

    def UpdateTeamByName(self, name, score, category):
        if not self.__isunique(name):
            for index, team in enumerate(self.__TeamList):
                if team.name == name:
                    self.__TeamList[index].score = score
                    self.__TeamList[index].category = category
        else:
            raise ValueError("Not a name.")

    def FilterTeam(self, scor):
        return Repository(filter(lambda team: team.score > scor > 25, self.__TeamList))

    def SortTeamScore(self):
        return Repository(sorted(self.__TeamList, key = lambda team: team.score))

    def __repr__(self):
        return str(self.__TeamList)

