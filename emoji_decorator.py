def ko_hello(name):
    print(f'안녕하세요, {name}님!')
    print('^~^//')

def en_hello(name):
    print(f'hello, {name}!')
    print('^~^//')   #같은거 하니까 함수로 하려면 

def add_emoji(name, func): #함수를 인자로 넘길 수 있음
    func(name)
    print('^~^//')

ko_hello('hyun')  
en_hello('hyun')  


#add_emoji(name, func)
add_emoji('hyun', ko_hello)

def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print('^~^//')
    return wrapper    #wrapper함수를 리턴

#emoji_decorator(func) #꾸며주고 싶은 함수를 인자로 받음
new_func = emoji_decorator(ko_hello)
new_func('hyun') #매개변수 name필요
#또는 
(emoji_decorator(ko_hello))('hyun')    
(emoji_decorator(en_hello))('hyun')

@emoji_decorator
def ko_hello(name):
    print(f'안녕하세요, {name}님!')
#데코레이팅된 ko_hello가 나옴. 2개의 데코레이터로 꾸미는 것도 가능   