class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Scores(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def getAvgGrade(scores):
        lenScores = len(scores)
        avgScore = float(sum(scores)/lenScores)
        if avgScore >= 90.0:
            return 'O'
        if avgScore >= 80.0 and avgScore < 90.0:
            return 'E'
        if avgScore >= 70.0 and avgScore < 80.0:
            return 'A'
        if avgScore >= 55.0 and avgScore < 70.0:
            return 'P'
        if avgScore >= 40.0 and avgScore < 55.0:
            return 'D'
        if avgScore <40.0:
            return 'T'


class Student(Person):
    def __init__(self, firstName, lastName, idNumber,scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
        
    
    def calculate(self):
        return str(Scores.getAvgGrade(self.scores))

s = Student('her','her',1111,[100,90,70])
print(s.calculate())