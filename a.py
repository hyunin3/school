# 4-2끝말잇기 단어 리스트 주어졌을때 몇번째 사람이 탈락하는지 확인

# 앞서 입력된 단어의 마지막 문자로 시작하는 단어 말해야
# 틀리거나 이전 단어 사용하면 탈락


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