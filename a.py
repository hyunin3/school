# collatz(6)  # => 8
# collatz(16)  # => 4
# collatz(27)  # => 111
# collatz(626331)  # => -1
num = int(input())
def collatz(num):
    for i in range(501):
        if num % 2 == 0:
            num / 2
        elif num % 2 != 0:
            num *3 + 1    
        if num == 1    
            