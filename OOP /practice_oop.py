
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def info(self):
        print(f"Name: {self.name}, Grade: {self.grade}")


s1 = Student("Shankar", "A")
s2 = Student("Riya", "B")

s1.info()
s2.info()


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance = {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. Balance left = {self.balance}")


acc = BankAccount("Shankar", 5000)
acc.deposit(1500)
acc.withdraw(3000)
acc.withdraw(5000)


class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog()
cat = Cat()

print("\nDog says:", dog.speak())
print("Cat says:", cat.speak())


def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog())
animal_sound(Cat())
