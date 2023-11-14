class Human:
    def __init__(self, n, a, h):
        print('Создан объект класса Human')
        self.__name = n
        self.__age = a
        self.height = h 
        
    def print(self):
        print(f'Имя: {self.__name}')
        print(f'Возраст: {self.age}')
        print(f'Рост: {self.height}')
        print('-'*30)
        
    @property
    def name(self):
        return self.__name.upper()
        
    @name.setter
    def name(self, n):
        self.__name = n.capitalize()
        
    @property
    def age(self):
        return self.__age
        
    @age.setter
    def age(self, a):
        if a >= 0 and a <= 100:
            self.__age = a 
        else:
            print('Столько не живут')

class Student(Human):
    def study(self):
        print(f'{self.name} учится')
                    
person1 = Student('Алина', 17, 167)
person1.print()
person1.study()
