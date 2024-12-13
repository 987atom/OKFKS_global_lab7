# class Car:
#     def __init__(self, colr, price):
#         self.__price = price
#         self.__colr = colr
#
#     def infoClass(self):
#         print("этот клас является шаблоном для всех машин")
#
#     def infoCar(self, name_car):
#         print(f"Марка: {name_car}")
#
#     @property
#     def Color(self):
#         return self.__colr
#
#     @property
#     def Price(self):
#         return self.__price
#
#     @Color.setter
#     def Color(self, color):
#         self.__price = color
#
#     @Price.setter
#     def Price(self, price):
#         self.__price = price
#
#
# toyota = Car("Черный", 3000000)
# bmw = Car("Красный", 5000000)
# toyota.colr = "Коричневый"
# toyota.price = 6000000
# print(toyota.colr)
# print(toyota.price)
# # toyota.infoCar("toyota")
# # toyota.infoCar("bmw")
#
# # toyota.infoClass()
# # bmw.infoClass()
# #
# # print(type(toyota))
# # print(type(bmw))






class Person:
    def __init__(self, lastname, firstname, patronimic):
        self.__lastname = lastname
        self.__firstname = firstname
        self.__patronimic = patronimic


    @property
    def lastname(self):
        return  self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    @property
    def firstname(self):
        return  self.__firstname

    @firstname.setter
    def firstname(self, firstname):
        self.__firstname = firstname

    @property
    def patronimic(self):
        return self.__patronimic

    @patronimic.setter
    def patronimic(self, patronimic):
        self.__patronimic = patronimic