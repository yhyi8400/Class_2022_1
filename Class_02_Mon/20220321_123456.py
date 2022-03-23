# 개발 일자: 2022년 3월 21일
# 개발자: Yeunghak Yi
"""
print(10)
print('안동대학교')
print("안동대학교")
print('10')
print('5+6')
"""
##print('Andong','National','University')
##print('Phi:',3.14)

##print('Andong',end='\n')
##print('University')
##print('Andong',end='')
##print('University')
##print('Andong',end=' ')
##print('University')
##print('Andong',end=',')
##print('University')

##print('Andong','National','University')
##print('Hello','Easy','Python', sep='')
##print('Hello','Easy','Python', sep=', ')
##print('Hello','Easy','Python', sep='\t')

##a=10
##print(a)
##print(a+10)
##
##b=20
##c=a
##a=b
##b=c
##print('A:',a,'B:',b,'C:',c)


##name = '홍길동'
##print(name)
##이름 = '홍길동'
##print(이름)
###circle area = 100
##circle_area = 100
##print(circle_area)
##_4tax = 400
##print(_4tax)

##a=10
##b=20
##c=a+b
##print(a,b,c)
##print('%d'%a)
##print('%d + %d = %d'%(a,b,c))

##a=10
##b=3.414
##c="Andong"
##print(type(a))
##print(type(b))
##print(type(c))
####a=b
####print(type(a))
####a=c
####print(type(a))
##
####d=int("123")
####print(a+d)
##d="123"
##print(a+int(d))
##d="123"
##print(b+float(d))

##점수 = input('점수를 입력:')
##print(점수)
##학번 = input("학번 입력:")
##이름 = input("이름 입력:")
##print('학번: ',학번)
##print('이름: ',이름)

##num1 = int(input("첫번째 수: "))
##num2 = int(input("두번째 수: "))
##print(type(num1))
##result = num1 + num2
##print("%d + %d = %d"%(num1, num2, result))

##num1 = input("첫번째 수: ")
##num2 = input("두번째 수: ")
##print(type(num1))
##result = int(num1) + int(num2)
##print("%s + %s = %d"%(num1, num2, result))

##num1 = int(input("첫번째 수: "))
##num2 = int(input("두번째 수: "))
##print(type(num1))
##result = num1 + num2
##print("{} + {}= {}".format(num1, num2, result))

# 원 넓이를 구하는 프로그램:
# 반지름은 입력을 받는다.
# 계산: 반지름*반지름 * phi

num1 = int(input("반지름: "))
area = num1 * num1 * 3.14
print("%d*%d*3.14 = %d"%(num1, num1,area))


# 사각형의 넓이를 구하는 프로그램:
# 가로길이, 세로 길이 입력을 받는다.
# 계산: 가로 * 세로 

num1 = int(input("가로: "))
num2 = int(input("세로: "))
result = num1 * num2
print("{} * {}= {}".format(num1, num2, result))



