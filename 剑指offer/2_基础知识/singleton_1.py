"""

使用Python实现单例模式

https://www.cnblogs.com/qiaojushuang/p/7805973.html

https://howto.lintel.in/python-__new__-magic-method-explained/

https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

Python is Object oriented language, every thing is an object in python. 
Python is having special type of  methods called magic methods named with preceded 
and trailing double underscores.

When we talk about magic method __new__ we also need to talk about __init__

These methods will be called when you instantiate 
(The process of creating instance from class is called instantiation). 
That is when you create instance. 
The magic method __new__ will be called when instance is being created. 
Using this method you can customize the instance creation. 
This is only the method which will be called first then __init__ will 
be called to initialize instance when you are creating instance.

Method __new__ will take class reference as the first argument 
followed by arguments which are passed to constructor(Arguments passed to call 
of class to create instance). 
Method __new__ is responsible to create instance, so you can use 
this method to customize object creation. 
Typically method __new__ will return the created instance object reference. 
Method __init__ will be called once __new__ method completed execution.

You can create new instance of the class by invoking the superclass’s __new__ method using super. 
Something like super(currentclass, cls).__new__(cls, [,….])

"""


class SingleTone(object):
    __instance = None

    def __new__(cls, val):
        if SingleTone.__instance is None:
            SingleTone.__instance = object.__new__(cls)
        SingleTone.__instance.val = val
        return SingleTone.__instance


class MyClass(SingleTone):
    class_val = 22

    def __init__(self, val):
        self.val = val

    def obj_fun(self):
        print(self.val, 'obj_fun')

    @staticmethod
    def static_fun():
        print('staticmedhot')

    @classmethod
    def class_func(cls):
        print(cls.class_val, 'classmethod')


if __name__ == '__main__':
    a = MyClass(1)
    b = MyClass(2)
    print(a is b)
    print(id(a))
    print(id(b))
    print(type(a))
    print(type(b))
