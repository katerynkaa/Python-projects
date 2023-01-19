from abc import ABCMeta, abstractmethod

class Visitor(metaclass=ABCMeta):

    @abstractmethod
    def visitAccounting(self, Building):
        pass

    @abstractmethod
    def visitDirectory(self, Building):
        pass

    @abstractmethod
    def visitCantine(self, Building):
        pass

    @abstractmethod
    def visitParents(self, Building):
        pass

class Building(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

class Accounting(Building):
    def __init__(self, scholar):
        self.scholar = scholar

    def __str__(self):
        res = "Cтуденту було нараховано стипендію в %d грн" % (self.scholar)
        return res

    def accept(self, visitor: Visitor):
        visitor.visitAccounting(self)

class Directory(Building):
    def __init__(self, accomodation):
        self.accomodation = accomodation

    def __str__(self):
        res = "Cтуденту заплатив за проживання %d грн" % (self.accomodation)
        return res

    def accept(self, visitor: Visitor):
        visitor.visitDirectory(self)


class Cantine(Building):
    def __init__(self, meals):
        self.meals = meals

    def __str__(self):
        res = "Cтудент заплатив за їжу %d грн" % (self.meals)
        return res

    def accept(self, visitor: Visitor):
        visitor.visitCantine(self)

class Parents(Building):
    def __init__(self, cash):
        self.cash = cash

    def __str__(self):
        res = "Cтудент отримав кишенькові гроші %d грн" % (self.cash)
        return res

    def accept(self, visitor: Visitor):
        visitor.visitParents(self)

class Student(Visitor):

    def __init__(self):
        self.graduation = ''
        self.money = 0

    def visitAccounting(self, Building: Accounting):
        sh = Building.scholar
        self.money += sh

    def visitParents(self, Building: Parents):
        c = Building.cash
        self.money += c

    def visitDirectory(self, Building: Directory):
        a = Building.accomodation
        self.money -= a

    def visitCantine(self, Building: Cantine):
        m = Building.meals
        self.money -= m

    def __str__(self):
        if self.money >= 0:
            self.graduation = 'На рахунку студента %d грн, він може випуститись із університету' % self.money
        else:
            self.graduation =  'Борг складає %d грн, бракує коштів для продовження навчання, він відрахований' % self.money

        return self.graduation


if __name__ == '__main__':
    print("===============SPENDINGS=================")
    obtainHelp = Parents(300)
    print(obtainHelp)
    obtainScholarschip = Accounting(1500)
    print(obtainScholarschip)
    payHostel = Directory(350)
    print(payHostel)
    payCanteen = Cantine(50)
    print(payCanteen)

    print("===============GRADUATION=================")
    student = Student()

    obtainHelp.accept(student)
    obtainScholarschip.accept(student)
    payCanteen.accept(student)
    payHostel.accept(student)

    print(student)






