# Вопрос №7

# Полиморфизм позволяет одинаково обращаться с объектами, имеющими однотипный интерфейс, 
# независимо от внутренней реализации объекта. 
# Например, с объектом класса “грузовой автомобиль” можно производить те же операции, 
# что и с объектом класса “автомобиль”, т.к. первый является наследником второго,
# при этом обратное утверждение неверно (во всяком случае не всегда).
# Другими словами полиморфизм предполагает разную реализацию методов с одинаковыми именами.
# Это очень полезно при наследовании, когда в классе наследнике можно переопределить методы класса родителя.


# Пример:

class T1:
    def __init__(self):
        self.n = 10
 
    def total(self, a):
        return self.n + int(a)
 
 
class T2:
    def __init__(self):
        self.string = 'Hi'
 
    def total(self, a):
        return len(self.string + str(a))
 
 
t1 = T1()
t2 = T2()
 
print(t1.total(35))  # Вывод: 45
print(t2.total(35))  # Вывод: 4