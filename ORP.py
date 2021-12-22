#object oriented programming in python

def hello():
    print('hello')

x =1
print(type(hello))   
print(type(x)) 

class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #print(name)
        
#    def add_one(self,x):
#        return x+1
        
#    def bark(self):
#        print('bark')

d = Dog('Tim',2)
print(d.name)
print(d.age)
#d = Dog()
#d.bark()

#print(d.add_one(5))            
#print(type(d))

class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade   #0-100
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False   
    
    def get_average_grade(self):
        value = 0
        for stuedent in self.students:
            value += stuedent.get_grade() 

        return value /len (self.students)           
        
s1 =student('Tim',19,95)
s1.get_grade()
s2 =student('Bill',19,75)        
s3 =student('jill',19,65)

course = Course('science',3)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.get_average_grade())


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')
    
    def speak(self):
        print('I do not know what I say')

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print('Meow')

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')    

class Dog(Pet):
    def speak(self):
        print('Bark')

#class Fish(Pet):
#    pass

p = Pet('Tim', 19)
p.show()
c = Cat('Bill', 34, 'red')
c.show()
c.speak()
d = Dog('Jill' ,25)
d.show()
d.speak()
#f = Fish('Bubbles', 10)
#f.speak()

