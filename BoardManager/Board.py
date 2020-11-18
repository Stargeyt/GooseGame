from BoardManager.Case import Case



class Board:

    def __init__(self):
        self.cases = list()

        for i in range(48):
            case = Case()
            if i == 47:
                case.type = "End"
            if i == 6:
                case.type = "times2"
            if i == 26:
                case.type = "to41"
            if i == 9:
                case.type = "playAgain"
            if i == 31:
                case.type = "backTo20"
            if i == 40:
                case.type = "restart"
            if i == 19:
                case.type = "wait"

            self.cases.append(case)

    def getCase(self, case):
        return self.cases[case]
