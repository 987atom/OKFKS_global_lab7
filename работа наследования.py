from лекция import Person

class Empliyee(Person):
    def __init__(self, lastname, firstname, patronimic,job, salary):
        super().__init__(lastname, firstname, patronimic)
        self.__job = job
        self.__salary = salary

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self,job):
        job.__job = job

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def infoEmpliyee(self):
        print(f"фамилия {self.lastname}\nИмя {self.firstname}\n Отчество {self.patronimic}\n Должность {self.job}\n Зарплата {self.salary}")


ivanov = Empliyee("Иванов","Иван","Иванович", "Продовец", 50000)
ivanov.infoEmpliyee()