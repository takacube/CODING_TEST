from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def __init__(self, id):
        self.id = id
    #Animalクラスを継承したクラスはこのgreetメソッドをオーバーライドしないとエラーが出るようになる！
    @abstractmethod
    def greet(self):
        pass

    def eat(self):
        print("旨旨旨")

class Dog(Animal):
    def greet(self):
        print("ワンワン")

class Cat(Animal):
    def greet(self):
        print("ニャーニャー")

class Pig(Animal):
    def fly(self):
        return True
