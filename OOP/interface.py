from OOP.my_interface import implements, Interface


class InterfaceClass(Interface):
    def method1(self, x):
        pass

    def method2(self, x, y):
        pass


class MyClass(implements(InterfaceClass)):
    def method1(self, x):
        return x * 2

    def method2(self, x, y):
        return x + y


myCls = MyClass()

print(myCls.method1(5))
