# 2022. 05.10.(화)

#과제 문제 1.
"""
for문을 사용하여 50부터 100까지의 정수 중에서
3으로 나누어 떨어지거나 5로 나누어 떨어지는 수들의
합계를 구하는 프로그램을 작성하시오.
"""
"""
tot = 0
for x in range(50,101):
    if x % 3 == 0 or x % 5 == 0:
        print(x, end=' ')
        tot = tot + x
    #print('for문 영향',x, end=' ')
print('')
print('50~100까지 합: ',tot)
"""

#과제 문제 2.
"""
양의 정수를 입력 받아 구구단 n단을 작성하는 프로그램을 작성하시오.
범위(2 <= n <= 9)를 벗어나는 정수가 입력되면 잘못된 값이 입력되었다고
안내를 하고 프로그램을 종료한다.
그렇지 않을 경우는 계속해서 입력을 받아 구구단을 출력한다.
"""
#구구단 입력
#2 <= n <= 9 인 경우 구구단 출력
#2 <= n <= 9 이외의 경우는 '잘못된 값이 입력' 출력 그리고 프로그램을 종료
#계속해서 입력


##dan = int(input('구구단 입력:'))
##print('====== %d단 ======'%dan)
##for x in range(1, 10):
##    print(dan,'x',x,'=',(dan*x))
##

##dan = int(input('구구단 입력:'))
##if 2<=dan<=9:
##    print('====== %d단 ======'%dan)
##    for x in range(1, 10):
##        print(dan,'x',x,'=',(dan*x))
##else:
##    print('잘못된 값이 입력')

"""
while True:
    dan = int(input('구구단 입력:'))
    if 2<=dan<=9:
        print('====== %d단 ======'%dan)
        for x in range(1, 10):
            print(dan,'x',x,'=',(dan*x))
    else:
        print('잘못된 값이 입력')
        break
"""

#과제 문제 3.
"""
'곱셈의 제왕' 프로그램을 만들려고 한다.
이 게임은 두 개의 숫자를 입력 받은 후 사용자가 올바른 곱셈 값을 입력할 때까지
반복하는 게임이다.
'곱셈의 제왕' 게임 프로그램을 만들어보세요.
"""

#두 개의 숫자 입력
#두 개의 숫자 곱셈
#곱셈의 결과를 입력
#곱셈의 결과와 두 개의 숫자 곱셈의 비교
#맞을 때 까지 입력

##num1 = int(input('수 1 입력:'))
##num2 = int(input('수 2 입력:'))
##계산곱셈 = num1*num2
##입력곱셈 = int(input('곱셈 값 입력:'))
##print(계산곱셈,입력곱셈)
##if 계산곱셈 == 입력곱셈:
##    print('Equal')
##else:
##    print('Different')
"""
num1 = int(input('수 1 입력:'))
num2 = int(input('수 2 입력:'))
계산곱셈 = num1*num2

while True:
    입력곱셈 = int(input('곱셈 값 입력:'))
    print(계산곱셈,입력곱셈)
    if 계산곱셈 == 입력곱셈:
        print('Equal')
        break
    else:
        print('Different')
"""

##a=[10,20,30]
##print(len(a))
##b=[40,50,60]
##c=a+b
##print(c)
##
##a[1]=200
##a[2]=201
##print(a)

##a=[10,20,30]
####a[1:2]=[200,201]
####print(a)
##a[1]=[200,201]
##print(a)

##a=[10,20,30]
##a.append(100)
##print(a)
##a.insert(3,300)
##print(a)
##b=[6,7,8]
##a.extend(b)
##print(a)

##a=[1,2,3,'a','b','c','a']
##print(a.index('a'))
##a.remove('a')
##print(a)
##del(a[1])
##print(a)
##a=[1,2,3,'b','c','a']
##a.reverse()
##print(a)
##a=[5,3,9,4,7,2]
###a.sort()
##a.sort(reverse=True)
##print(a)
##a = ['kim','lee','hong','park','song']
##for x in a:
##    print(x,end=' ')
##
##print('')
##for x in range(len(a)): # 0,1,2,3,4
##    print(a[x], end=' ')
##
##list1 =[]
##list2 =[]
##val = 1
##
##for x in range(3):
##    for y in range(4):
##        list1.append(val)
##        val = val +1
##    list2.append(list1)
##    list1=[]
##
##for x in range(3):
##    for y in range(4):
##        print('%3d'%list2[x][y], end =' ')
##    print('')

##a=[]
##for x in range(1,51):
##    if x % 3 == 0:
##        a.append(x)
##
##for x in a:
##    print(x, end=' ')

##myTuple = (1,2,3,4,5)
###print(myTuple)
###print(len(myTuple))
##for x in myTuple:
##    print(x)
##r = 3 in myTuple
###print(r)
##r = 30 in myTuple
###print(r)
###myTuple.append(7)
###myTuple.insert(2,7)
###myTuple.remove(2)
##del(myTuple[1])
##print(myTuple)

##myTuple = (1,2,3,4,5)
##myList = list(myTuple)
##print(myTuple)
##print(myList)
##myList.append(600)
##print(myList)
##myTuple = tuple(myList)
##print(myTuple)
##tp1 = (10,20,30)
##tp2 = (40,40,60)
##ttpp = tp1 + tp2
##print(ttpp)

#dic = {'강아지':'dog','고양이':'cat','새':'bird'}
##print(dic)
##print(dic.keys())
##print(dic.values())
##print(dic['강아지'])
##print(dic.get('고양이'))
##dic['고래']='whale'
##print(dic)
##del dic['고양이']
##print(dic)
##dic.clear()
##print(dic)

##dict = {'이름':'홍길동','나이':'25', '주소':'안동','취미':['축구','야구','등산']}
##for x in dict.keys():
##    print(x,'\t:',dict[x])

dic = {}
while True:
    mem = input('1. 회원가입:‘, ‘2.프로그램 종료:')
    if mem == '1':
        ID = input('ID 입력:')
        PW = input('PW 입력:')
        dic[ID]=PW
        #print(ID,PW)
    else:
        #print('종료')
        break

print('-'*20)
print(' 아이디:비밀번호')
print('-'*20)
for x in dic.keys():
    print(x,':',dic[x])
