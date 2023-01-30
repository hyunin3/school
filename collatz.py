# collatz(6)  # => 8
# collatz(16)  # => 4
# collatz(27)  # => 111
# collatz(626331)  # => -1
num = int(input())
def collatz(num):
    cnt = 0
    while num != 1:
        if num % 2 ==0:
            num = num / 2
            cnt = cnt + 1
        else:
            num = num * 3 + 1    
            cnt = cnt + 1
        if cnt <= 500:
            pass
        else:
            return -1
    return cnt                
print(collatz(num))            