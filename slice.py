#문자열 슬라이스 연습



s='abcdefghi'
#  012345678
#(-)987654321         
print(s[:3])#0에서부터 3칸 0,1,2->a,b,c
print(s[5:])#5부터 끝까지 쭉 5,6,7,8->f,g,h,i
print(s[1:4])#4-1=3. 1부터 3칸 1,2,3->b,c,d
print(s[-2])#뒤에서 2칸 -2->h
print(s[::])#그대로
print(s[::-1])#거꾸로