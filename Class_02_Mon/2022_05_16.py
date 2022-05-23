# 2022.05.16.
#문제1.
"""
num=[]
for x in range(1,101):
    #print(x, end=', ')
    num.append(x)
#print(num)
e_tot=0
o_tot=0
for n in num:
    if n % 2 == 0: e_tot = e_tot+n
    else: o_tot = o_tot+n

print('짝수합:',e_tot)
print('홀수합:',o_tot)
"""
#문제 2.
"""
myTuple = ('A','B','C','D','E','F')
for x in myTuple:
    print(x, end=' ')
"""
#문제 3.
"""
sports = ('태권도','축구','야구','등산','권투')
for x in range(len(sports)):
    #print(x)
    if x % 2 == 1:
        print(sports[x])
"""
#문제 4.
"""
foods = {'떡볶이':'오뎅',
         '짜장면':'단무지',
         '라면':'김치',
         '피자':'피클',
         '맥주':'땅콩',
         '치킨':'무김치',
         '삼겹살':'상추'}

print(foods)
print(foods.keys())
#print(list(foods.keys()))
print(foods.values())

food_lists = list(foods.keys())
print('food_lists:',food_lists)

while True:
    food_name = input('음식이름 입력:')
    if food_name in food_lists:
        print('%s 궁합 음식은 %s입니다'%(food_name,foods.get(food_name)))
    elif food_name == '끝':
        print('프로그램 종료')
        break
    else:
        print('없는 음식 입니다')
"""
"""

def cal():
    a=10
    b=20
    print('%d + %d = %d'%(a,b,a+b))

def greet():
    print('반갑습니다')
    print('안녕하세요')
    

cal()
cal()
greet()
greet()
greet()
greet()

"""
"""
def cnverUnit():
    print('cm 길이: %.1f - > inch길이: %.1f'%(lenCM, lenCM*0.393701))

lenCM = float(input('cm길이 입력:'))
cnverUnit()
"""
"""
num1=10
def func1():
    print('num1은 함수 내:',num1)

print('num1은 함수 외:',num1)
func1()
"""
"""
# 아래 프로그램은 에러 발생 - 지역변수 num
num1=10
def func1():
    num=30
    print('num은 함수 내:',num)

print('num1은 함수 외:',num)
func1()
"""
"""
def greet(name):
    print(name,'씨 반갑습니다')


#greet('홍길동')
이름 = input('이름 입력:')
greet(이름)
"""    
"""
def add(a,b) :
    c=a+b
    print('%d + %d = %d'%(a,b,c))

def abst(a,b) :
    c=a-b
    print('%d - %d = %d'%(a,b,c))
def mul(a,b) :
    c=a*b
    print('%d * %d = %d'%(a,b,c))
def div(a,b) :
    c=a/b
    print('%d / %d = %.1f'%(a,b,c))
add(10,20)
abst(10,20)
mul(10,20)
div(10,20)
"""
"""
def addFunction(n1,n2):
    tot = n1+n2
    return tot

result = addFunction(10,20)
#print(addFunction(10,20))
print(result)
"""
"""
def cal(v1,v2,op):
    re = 0
    if op == '+':
        re = v1+v2
    elif op == '-':
        re = v1-v2
    elif op == '*':
        re = v1*v2
    elif op == '/':
        re = v1/v2

    return re
    

n1 = int(input('숫자1:'))
n2 = int(input('숫자2:'))
oper = input('연산자:')
result = cal(n1,n2,oper)
print('%d %s %d = %d'%(n1,oper,n2,result))
"""
"""
def multi(n1,n2):
    reList=[]
    re1=n1+n2
    re2=n1-n2
    reList.append(re1)
    reList.append(re2)

    return reList
    

myList=[]
myList = multi(100,200)
print(myList)

"""
# 원의 반지름을 입력받아 원의 넓이를 구하는 프로그램 작성
# 단, 넓이의 계산은 return이 있는 함수를 이용하야 계산한다.

def circle(n1):
    area = n1**2*3.14
    return area

cir = float(input('원의 반지름 입력:'))
result = circle(cir)
print('원의 넓이:%.1f'%result)



