class MyClass:
    def method(self):
        return 'instance method', self
    
    @classmethod
    def classmethod(cls):
        return 'classmethod'
    
    @staticmethod
    def staticmethod():
        return 'staticmethod'
    
my_class  = MyClass()
print(my_class.method())
print(my_class.classmethod()) 
print(my_class.staticmethod())     