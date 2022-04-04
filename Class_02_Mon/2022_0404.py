##1.
##원금 = int(input('저축금액 입력:'))
##이자 = 원금*3.75/100
##세금 = 이자*15/100
##최종금액 = 원금 + 이자 - 세금
##print('원금:%d원'%원금)
##print('이자:%d원'%이자)
##print('세금:%d원'%세금)
##print('최종금액:%d원'%최종금액)

##2.
##높이 = float(input('높이:'))
##반지름 = float(input('반지름:'))
##부피 = 반지름**2*높이*3.141592
##print('원기둥의 부피:%.1f'%부피)

###3.
##x1 = int(input('X1:'))
##y1 = int(input('Y1:'))
##x2 = int(input('X2:'))
##y2 = int(input('Y2:'))
##d = ((x2-x1)**2 + (y2-y1)**2)**0.5
##print('두 점 사이의 거리: %.3f'%d)
##
"""
#4.
가격1 = int(input('사과:'))
가격2 = int(input('바나나:'))
가격3 = int(input('망고:'))
가격4 = int(input('과자:'))
지불금액 = int(input('지불금액:'))
물건가격 = 가격1+가격2+가격3+가격4
거스럼돈 = 지불금액-물건가격
print('받은돈:%d원'%지불금액)
print('물건가격:%d원'%물건가격)
print('거스럼돈:%d원'%거스럼돈)
천원 = 거스럼돈 // 1000
천원_나머지 = 거스럼돈 % 1000
오백원 = 천원_나머지 // 500
오백원_나머지 = 천원_나머지 % 500
백원 = 오백원_나머지 // 100
백원_나머지 = 오백원_나머지 % 100
십원 = 백원_나머지 // 10
print('1000원:%d장'%천원)
print('오백원:%d장'%오백원)
print('백원:%d장'%백원)
print('십원:%d장'%십원)

import time
print(1)
print(2)
time.sleep(2)
print(3)


str1 = 'Andong national Univesity'
print(len(str1))
print(getsizeof(str1))

str1 = 'Andong'
str2 = 'National Univesity'
number = '35567'
#address = str1+' '+str2
address = str1+' '+str2 + ' '+ number
print(address)

str1 = 'aNDONG'
print(str1.upper())
print(str1.lower())
print(str1.capitalize())

a='2022'
print(a.isdecimal())
b='abc'
print(b.isalpha())
print(b.isdecimal())
print(b.islower())

str1 = 'Andong National Univesity'
str2 = str1.replace('National','International')
print(str1)
print(str2)

rainbow ='빨주노초파남보'
print(rainbow)
print(rainbow[0])
print(rainbow[3])

str1 = 'Andong National Univesity'
print(str1[1:5])
print(str1[:5])
print(str1[10:])

jumin = input('주민번호:')
y = '19'+jumin[0:2]
m = jumin[2:4]
d = jumin[4:6]
age = 2022-int(y)
print(y,' ',m,' ',d,' ',age)

str1 = 'Andong'
print(str1[-1])
print(str1[-4:-2])
print('i' in str1)
print('n' in str1)
print(str1.find('n'))

a = 10
print(a)

b = []
print(b)
c = list()
print(c)
d = [10,20,30]
print(d)
e = ['홍길동',90,80,85.5]
print(e)
f = [[1,2,3], [4,5,6]]
print(f)
print(len(e))
print(len(f))
g = [1,2,3,4,5,6,7]
print(g[0])
print(g[-1])
print(g[2])
print(max(g))
print(min(g))
h = [10,20,30]
i = g+h
print(i)
"""
#a = [10,20,30]
#b = int(input('점수:'))
#a.append(b)
#print(a)
#b=100
#a.insert(2,b)
#print(a)
#b = [100,200,300]
#a.extend(b)
#print(a)
#a = ['a',1,2,3,'b','c','a']
#print(a.index('a'))
#b = a.remove('a')
#print(a.reverse())
#a=[2,3,1,4,5]
#print(a.sort(reverse=True))
a=range(5)
print(list(a))
b= range(1,10,2)
print(list(b))