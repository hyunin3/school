''''''
# 3-2어떤 해가 입력되면 윤년인지 아닌지 판별

# 해(year)가 4의 배수이면서 100의 배수가 아닐 때
# 400의 배수
# 두 조건 중 하나만 만족하면 윤년
''''''
# num = int(input('해를 입력하세요: '))
# if num % 4 == 0 and num % 100 != 0:
#     print('윤년')
# elif num % 400 == 0:
#     print('윤년')
# else:
#     print('윤년이 아닙니다.')    

''''''
# 4-2끝말잇기 단어 리스트 주어졌을때 몇번째 사람이 탈락하는지 확인

# 앞서 입력된 단어의 마지막 문자로 시작하는 단어 말해야
# 틀리거나 이전 단어 사용하면 탈락
# done입력할 때까지 시행
''''''
words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
# for idx in range(len(1, words)):
    print(idx)
words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

for idx in range(1, len(words)):
    print(idx)
    # 지금의 나

#     if words[idx-1][-1] != words[idx][0]:
#         print('실패', idx, words[idx])
#         break

#     elif words[idx] in words[:idx]:
#         print('실패', idx, words[idx])
#         break
# else:
#     print('성공')    
    
         


