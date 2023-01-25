import random
lst = [
    '고영진','구본웅','김성용','김하늘','김하림',
    '김현아','민경현','배이경','서동훈','송준우',
    '심현재','유창재','윤민영','윤태영','이민호',
    '이성섭','이성우','이영아','이예슬','임수형',
    '임혜진','정선재','정현아','진익근','최태호',
    '최홍준','하정호','허주혁'
  ]
cnt = 0
for i in lst:
    if len(lst) >= 4: 
        team1 = random.sample(lst, 4)
        team1.sort()
        cnt = cnt + 1
        
        print(cnt,'조', *team1)
        lst = [i for i in lst if i not in team1]   
    else:
        print(*lst)  
        break  


# samplelst = random.sample(lst, 4) #
# samplelst.sort() #뽑힌 리스트를 오름차순으로 정렬
# print(*samplelst)