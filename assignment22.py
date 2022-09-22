# 10 questions about classes, objects, inheritance, polymorphism, queues, stacks, and more

#1. create a credit card class with the following attributes: card number, expiration date, and security code. Create a method that will print out the card number, expiration date, 
#and security code. Create an instance of the class and call the method.

class Credit_card:
    def __init__(self,card_number, expiration_date,security_code):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.security_code = security_code
    def printout(self):
        print("The card number is ", self.card_number, self.expiration_date, "and", self.security_code)


x = Credit_card("2451667", "12/89/8",6738)
x.printout()
        

#2. create Animal class and Dog class. Make the Dog class inherit from the Animal class. Add a bark method to the Dog class. Create an instance of the Dog class and call the bark 
# method.

class Animal:
    def __init__(self):
        print("am an animal")
    
    def bark(self):
        print("am bark")


class Dog(Animal):
    def __init__(self):
        super().__init__(self)
        print("am A dog")
    def bark(self):
        print("am barking dog")

dogg = Dog()
dogg.bark()



#3. create a class called Queue. The class should have the following methods: enqueue, dequeue, and size. The enqueue method should add an item to the queue. The dequeue method 
# should remove an item from the queue. The size method should return the size of the queue.


class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, data):
            self.queue.insert(0, data)
            return True

    
    def dequeue(self):
            return self.queue.pop()

   
    def size(self):
        return len(self.queue)

    def display(self):
            return self.queue

q = Queue()

q.enqueue('city')
q.enqueue('does')
q.enqueue('Assignment')

print(q.display())

print(q.dequeue())

print(q.display())

print(q.size())




#4. create a class called Stack. The class should have the following methods: push, pop, and size. The push method should add an item to the stack. The pop method should remove 
# an item from the stack. The size method should return the size of the stack.

class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack

s = Stack()
s.push('Benard')
s.push('prosper')
s.push('collin')
s.push('james')
print(s.show())
print(s.pop())
print(s.show())
print(s.size())




#5. create a class called Person. The class should have the following attributes: name, age, and address. The class should have the following methods: eat, sleep, and work. 
# The eat method should print out the name of the person and the word "is eating". The sleep method should print out the name of the person and the word "is sleeping". 
# The work method should print out the name of the person and the word "is working".

class Person:
    def __init__(self,name, age,address):
        self.name = name
        self.age = age
        self.address = address
    def __repr__(self):
        return f"<Person {self.name} {self.age} {self.address}>"
    def eat(self):
        print( self.name + " is eating")
    def sleep(self):
        print(self.name + " is sleeping")
    def work(self):
        print(self.name + " is sleeping")
personn = Person("Benard", 26,"Mutungo")
personn.eat()
personn.sleep() 
personn.work()



#6. create a class called Employee. The class should have the following attributes: name, age, and salary. The class should have the following methods: eat, sleep, and work. 
# The eat method should print out the name of the person and the word "is eating". The sleep method should print out the name of the person and the word "is sleeping". 
# The work method should print out the name of the person and the word "is working". Create a subclass of Employee called Programmer. 
# The Programmer class should have the following attributes: name, age, salary, and programming language. The Programmer class should have the following methods: eat, 
# sleep, work, and code. The code method should print out the name of the person and the word "is coding in" and the programming language. Create an instance of the Programmer 
# class and call all the methods.

class Employee:
    def __init__(self,name, age,salary):
        self.name = name
        self.age = age
        self.address = salary
    
    def __repr__(self):
        return f"<Person {self.name} {self.age} {self.salary}>"
    def eat(self):
        print(self.name + " is eating")
    def sleep(self):
        print(self.name + " is sleeping")
    def work(self):
        print(self.name + " is sleeping")
class Programmer(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
    def eat(self):
        print(self.name + " is coding in and the programming language")
    def sleep(self):
        print(self.name + "is coding in and the programming language")
    def work(self):
        print(self.name + " is coding in and the programming language")
prog = Programmer("benard", 26, "shs 10000000")
prog.eat()
prog.sleep() 
prog.work()






#7. create a class called Vehicle. The class should have the following attributes: make, model, and year. The class should have the following methods: start, stop, and drive. 
# The start method should print out the make, model, and year of the vehicle and the word "is starting". The stop method should print out the make, model, and year of the vehicle 
# and the word "is stopping". The drive method should print out the make, model, and year of the vehicle and the word "is driving". Create a subclass of Vehicle called Car. 
# The Car class should have the following attributes: make, model, year, and color. The Car class should have the following methods: start, stop, drive, and park. 
# The park method should print out the make, model, year, and color of the car and the word "is parking". Create an instance of the Car class and call all the methods.

class Vehicle:
    def __init__(self,make, model,year):
        self.make = make
        self.model = model
        self.year = year
    def __repr__(self):
        return f"<Vehicle {self.make} {self.model} {self.year}>"
    def start(self):
        print(self.make + self.model + self.year + "is starting")
    def stop(self):
        print(self.make + self.model + self.year + "is stopping")
    def drive(self):
        print(self.make + self.model + self.year + "is driving")
class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    def start(self):
        print(self.make + self.model + self.year + "is starting")
    def stop(self):
        print(self.make + self.model + self.year + "is stopping")
    def park(self):
        print(self.make + self.model + self.year + "is parking")

ca = Car("ford","EXPLORER", 2019)
ca.start()
ca.stop() 
ca.drive()
ca.park()

    




#8. create a class called Animal. The class should have the following attributes: name, color, and age. The class should have the following methods: eat, sleep, and make_sound. 
# The eat method should print out the name of the animal and the word "is eating". The sleep method should print out the name of the animal and the word "is sleeping". 
# The make_sound method should print out the name of the animal and the word "is making a sound". Create a subclass of Animal called Dog. 
# The Dog class should have the following attributes: name, color, age, and breed. The Dog class should have the following methods: eat, sleep, make_sound, and bark. 
# The bark method should print out the name of the dog and the word "is barking". Create an instance of the Dog class and call all the methods.

class Animal:
    def __init__(self,name, color,age):
        self.name = name
        self.age = color
        self.address = age
    
    def __repr__(self):
        return f"<Animal {self.name} {self.color} {self.age}>"
    def eat(self):
        print(self.name + " is eating")
    def sleep(self):
        print(self.name + "  is sleeping")
    def make_sound(self):
        print(self.name + " is making a sound")
    
class Dog(Animal):
    def __init__(self, name, color, age):
        super().__init__(name, color, age)
    def eat(self):
        print(self.name + " is eating")
    def sleep(self):
        print(self.name + "  is sleeping")
    def make_sound(self):
        print(self.name + " is making a sound")
    def bark(self):
        print(self.name + " is barking")

do = Dog("BENTLEY", "black", 58)
do.eat()
do.sleep() 
do.make_sound()
do.bark()





#9. create a class of your choice. It should have at least 3 attributes and 3 methods where one of the methods is a static method. Implement polymorphism, encapsulation, and 
# inheritance.
class Manchester_United():

	def Location(self):
        
		print("The location of machester united is manchester North West England.")

	def  Get_Best_Player(self):
		print("The best player in manchester is Jose Diogo Dalot Teixeira.")

	def type(self):
		print("Jose Diogo Dalot Teixeira is a left back defender.")

class Arsenal():
	def Location(self):
		print("The location of Arsenal is London Borough of Islington, London, United Kingdom.")

	def Get_Best_Player(self):
		print("The best player in Arsenal is  Bukayo Saka.")

	def type(self):
		print(" Bukayo Saka is a Forward.")

obj_manu = Manchester_United()
obj_Arsenal = Arsenal()
for Club in (obj_manu, obj_Arsenal):
	Club.Location()
	Club.Get_Best_Player()
	Club.type()


class Manchester_United:
	def __init__(self):

		
		self._a = 2

class Derived(Manchester_United):
	def __init__(self):

		Manchester_United.__init__(self)
		print("Calling protected member of base class: ",
			self._a)

		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)


obj1 = Derived()

obj2 = Manchester_United()

print("Accessing protected member of obj1: ", obj1._a)

print("Accessing protected member of obj2: ", obj2._a)


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("Benard", "Byakatonda")
x.printname()


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Byaka", "Bena",2019)
x.welcome()

