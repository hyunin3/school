# 초기화 메서드는 인자로 개의 이름과 견종을 받아서 인스턴스 변수에 할당한다.
# bark() 메서드를 호출하면 개는 짖을 수 있다.
# 클래스 변수는 태어난 개의 숫자와 현재 있는 개의 숫자를 기록하는 변수로 구성한다.
# 개가 태어나면 num_of_dogs와 birth_of_dogs의 값이 각 1씩 증가한다.
# 개가 죽으면 num_of_dogs의 값이 1 감소한다.
# get_status() 메서드를 호출하면 birth_of_dogs와 num_of_dogs의 수를 출력할 수 있다

class Doggy:
    num_of_dogs = 10
    birth_of_dogs = 5
    
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def bark(self):
        print(f'{self.name}:bowwow')
        
    def birth(self):
        self.num_of_dogs += 1
        self.birth_of_dogs += 1
  
    def death(self):
        self.num_of_dogs -= 1

    def get_status(self):
        print(self.num_of_dogs)
        print(self.birth_of_dogs)            
a = Doggy('merry', 'yorkie')
b = Doggy('happy', 'husky')

a.bark() 
b.bark()       
a.birth()
b.birth()
print(a.num_of_dogs)
a.death()
b.death()
print(a.num_of_dogs)