#총 몇 잔의 주문이 들어왔는지 확인
#증복을 제거한 메뉴만을 리스트 형식으로 출력.내림차순으로

orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
order = list(orders.split(','))
#print(order)
print(len(order))

result = []
for menu in order:
    if menu not in result:
        result.append(menu)
result.sort(reverse = True)
print(result)        
