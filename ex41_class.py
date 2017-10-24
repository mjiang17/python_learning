## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## 继承父类Animal, Dog has-a Animal
class Dog(Animal):

	def __init__(self, name):

		self.name = name
		print(self.name)

## 继承父类Animal. Cat has-a Animal
class Cat(Animal):

	def __init__(self, name):

		self.name = name
		print(self.name)

## 定义一个新的类Person, Persion is-a object
class Person(object):

	def __init__(self, name):

		self.name = name
		print(self.name)

		## Person has-a pet of some kind
		self.pet = None
## 继承父类Person, Emploee has-a Person 
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		sef.salary = salary

## 定义一个新的类Fish, Fish is-a object
class Fish:
	pass

## 继承父类Fish, Salmon has-a Fish
class Salmon(Fish):
	pass

## 继承父类Fish, Halibut has-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person 
mary = Person("Mary")
