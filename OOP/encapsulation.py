class Student:
    def __init__(self, name, age):
        self.name = name  # Public Attribute
        self.__age = age  # Private Attribute

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

        else:
            print("Age must be positive number")


student = Student('Zihad', 26)

student.set_age(20)

print(student.get_age())
