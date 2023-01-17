num = int(input('해를 입력하세요: '))
if num % 4 == 0 and num % 100 != 0:
    print('윤년')
elif num % 400 == 0:
    print('윤년')
else:
    print('윤년이 아닙니다.')    