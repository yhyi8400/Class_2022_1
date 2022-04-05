"""
#1.
입력금액 = int(input('저축금액 입력:'))
이자 = 입력금액 * 0.0375
세금 = 이자 * 0.15
원리금 = 입력금액 + 이자 - 세금
print('원금:%d원'%입력금액)
print('이자:%d원'%이자)
print('세금:%d원'%세금)
print('최종금액:%d원'%원리금)
"""
"""
#2
높이 = float(input('높이:'))
반지름 = float(input('반지름:'))
원기둥부피 = 반지름**2 * 높이 * 3.141592
print('원기둥의 부피:%.1f'%원기둥부피)
"""
"""
#3
x1 = int(input('x1좌표:'))
y1 = int(input('y1좌표:'))
x2 = int(input('x2좌표:'))
y2 = int(input('y2좌표:'))
d = ((x2-x1)**2 + (y2-y1)**2)**0.5
print('두 점 사이의 거리:%.3f'%d)
"""
"""
#4
사과 = int(input('사과:'))
바나나 = int(input('바나나:'))
망고 = int(input('망고:'))
과자 = int(input('과자:'))
지불금액 = int(input('지불금액:'))
물건가격 = 사과 + 바나나 + 망고 + 과자
거스럼돈 = 지불금액 - 물건가격
천원 = 거스럼돈 // 1000
천원_나머지 = 거스럼돈 % 1000
오백원 = 천원_나머지 // 500
오백원_나머지 = 천원_나머지 % 500
백원 = 오백원_나머지 // 100
백원_나머지 = 오백원_나머지 % 100
십원 = 백원_나머지 // 10
print('받은 돈:%d'%지불금액)
print('물건가격:%d'%물건가격)
print('거스럼돈:%d'%거스럼돈)
print('1000원:%d장'%천원)
print('500원:%d개'%오백원)
print('100원:%d개'%백원)
print('10원:%d개'%십원)
"""
"""
import time
print(1)
print(2)
print(3)
time.sleep(2)
print(4)
print(5)
"""
"""
from sys import getsizeof


str1 = '안동대학교'
print(len(str1))
길이 = len(str1)
print(길이)
print(getsizeof(str1))

str1 = 'Andong'
str2 = 'University'
str3 = str1 + ' ' + str2
print(str3)
주소 = '36729' + ' ' + str3
print(주소)

str1 = 'Andong'
str2 = 'university'
print(str1.lower())
print(str1.upper())
print(str2.capitalize())

a = '1234'
print(a.isdecimal())
str1 = 'Andong'
print(str1.isalpha())
print(str1.isdecimal())
print(str1.islower())
print(str1.isupper())

str1 = 'Andong National University'
print(str1.replace('National','International'))

무지개 = '빨주노초파남보'
순서 = 무지개[0]
print(순서)
순서 = 무지개[1]
print(순서)
순서 = 무지개[4]
print(순서)

str1 = 'Andong National University'
sl = str1[2:5]
print(sl)
print(str1[:10])
print(str1[10:])

str1 = 'Andong National University'
sl = str1[-1]
print(sl)
print(str1[-6:-2])


jumin = input('주민번호입력:')
y = jumin[:2]
m = jumin[2:4]
d = jumin[4:]
year = '19'+y
age = 2022 - int(year)
print('당신은 %s년도에 태어났어요'%year)
print('당신의 생일은 %s월 %s일 입니다.'%(m,d))
print('당신의 나이는 %d살 입니다.'%(age))
"""
"""
str1 = 'Andong National University'
result = 'Nat' in str1
print(result)
result = 'Nato' in str1
print(result)
result = str1.find('Nat')
print(result)
result = str1.find('n')
print(result)
"""
"""
a=[]
print(a)
b=10
print(b)
c = [1,2,3,4,5]
print(c)
print(c[0])
print(c[2])
"""
"""
c = [1,2,3,4,5]
print(len(c))

a=[10,20,30]
b=[100,200,300]
d = a+b
print(d)
print(max(c))
print(min(c))
"""
"""
a=[10,20,30]
a.append(100)
print(a)
#data = int(input('점수:'))
#a.append(data)
#print(a)
a.insert(2,1000)
print(a)
b=[600,700,800] 
a.extend(b)
print(a)
"""
"""
#a = [1,2,'a','c','s','a']
#lo = a.index('a')
#print(lo)
#s = a.remove('a')
#print(s)
a=[30,10,20]
result = a.sort()
print(result)
"""
a = range(5)
print(list(a))

a = range(1,10,2)
print(list(a))

a = range(10,5,-1)
print(list(a))



