class Person:
    def __init__(self):
        self._age = 0
        
    def get_age(self):  #getter
        print('getter 호출!')
        return self._age
    
    
    def set_age(self, age):    #setter
        print('setter 호출!')
        self._age = age
        
    age = property(get_age, set_age)  #이거해주면 p1.age = 25해도 됨   
        
p1 = Person() 
#p1._age = 25  하면 안됨
#print(p1._age)  하면 안됨
p1.set_age(25)
print(p1.get_age())          

@property
def age(self):  #getter
    print('getter 호출!')
    return self._age
    
@age.setter   
def age(self, age):    #setter
    print('setter 호출!')
    self._age = age