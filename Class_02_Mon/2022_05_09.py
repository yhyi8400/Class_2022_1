# 2022. 05. 09.
# 문제 1.
"""
for문을 사용하여 50부터 100까지의 정수 중에서
3으로 나누어 떨어지거나 5로 나누어 떨어지는 수들의 합계를
구하는 프로그램을 작성하시오.
"""
"""
tot=0
for x in range(50,101):
    #print(x,end=' ')
    if x%3==0 or x%5==0: # 3,6,9,5,10
        print(x,end=' ')
        tot = tot + x

print('50-100까지 합: %d'%tot)
"""

#문제 2.
"""
양의 정수를 입력 받아 구구단 n단을 작성하는 프로그램을 작성하시오.
범위(2 <= n <= 9)를 벗어나는 정수가 입력되면
잘못된 값이 입력되었다고 안내를 하고 프로그램을 종료한다.
그렇지 않을 경우는 계속해서 입력을 받아 구구단을 출력한다.
"""
"""
while True:
    dan = int(input('구구단 입력:'))
    if 2<= dan <=9:
        for x in range(1,10):
            print(dan, 'x',x, '=',dan*x)
    else:
        print('잘못된 입력입니다')
        break
"""

#문제 3.
"""
'곱셈의 제왕' 프로그램을 만들려고 한다.
이 게임은 두 개의 숫자를 입력 받은 후
사용자가 올바른 곱셈 값을 입력할 때까지 반복하는 게임이다.
'곱셈의 제왕' 게임 프로그램을 만들어보세요.
"""
"""
num1 = int(input('숫자 1:'))
num2 = int(input('숫자 2:'))
곱셈 = num1*num2
while True:
    결과값 = int(input('곱셈 결과 값 입력:'))
    if 곱셈 == 결과값:
        print('잘 했습니다')
        break
    else:
        print('새로 입력하세요..')
        
        
print('프로그램 종료')
"""

##a = [10,20,30]
##b = [40,50,60]
##c = a+b
##print(c)
##tot = a[0] + a[1] + a[2]
##avg = tot/3
##print('avg:',avg)

##tot=0
##for x in a:
##    tot = tot + x
##    print(x,tot)

##a[1:2]=[200,201]
##print(a)
##b[1] = [200, 201]
##print(b)


##a = [1,2,'a','b','c','a']
##print(a.index('a'))
##
##a.remove('b')
##print(a)
##del(a[1])
##print(a)

##a.reverse()
##print(a)

##a = [6,3,7,9,2,5]
###a.sort()
##a.sort(reverse=True)
##print(a)

##a = ['kim','lee','hong','park','song']
##print(len(a))
##for x in a:
##    print(x)
##for x in range(len(a)):
##    print(a[x])

##list1 = []
##list2 = []
##val=1
##for x in range(3):
##    for y in range(4):
##        list1.append(val)
##        val = val + 1
##    list2.append(list1)
##    list1=[]
##for x in range(3):
##    for y in range(4):
##        print('%3d'%list2[x][y], end='')
##    print('')
###print(list2)
##a=[]
##for x in range(1,51):
##    #print(x, end=' ')
##    if x % 3 == 0:
##        a.append(x)
##
##print(a)

##myTuple = (10,20,30,40,50)
##result = 30 in myTuple
##print(myTuple)
##print(len(myTuple))
##print(result)
##for x in myTuple:
##    print(x)
#myTuple.append(60)
#myTuple.insert(2,60)
#myTuple.remove(30)
#del myTuple(2)


##myTuple = (10,20,30,40,50)
##myList = list(myTuple)
##print(myList)
##myList.append(60)
##print(myList)
##myTuple = tuple(myList)
##print(myTuple)
##tp1 = (1,2,3)
##tp2 = (4,5,6)
##tp = tp1+tp2
##print(tp)
##sports = ('태권도','축구','수영','야구','등산','권투','농구','양궁')
##for x in range(len(sports)):
##    if x % 2 ==1:
##        print(sports[x])

##dict = {'강아지':'dog','고양이':'cat','새':'bird'}
##print(dict)
##print(dict.keys())
##print(dict.values())
##print(dict['강아지'])
##print(dict.get('고양이'))
##dict['고래']='whale'
##print(dict)
##del dict['고양이']
##print(dict)
##dict.clear()
##print(dict)

##dict = {'이름':'홍길동', '나이':'25','주소':'안동','취미':['축구','수영','야구','등산'], '혈액형':'A'}
##for x in dict.keys():
##    print(x,'\t:',dict[x])
##

# Membership
"""
Membership = {}
ID = input('멤버 ID:')
PW = input('멤버 PW:')
member = input('1. 회원가입, 2. 프로그램종료')
if member == '1': #회원가입
else: #종료
    break
"""
Membership = {}
while True:
    member = input('1. 회원가입(1), 2. 프로그램종료(2)')
    if member == '1': #회원가입
        ID = input('멤버 ID:')
        PW = input('멤버 PW:')
        Membership[ID]=PW
        #print(Membership)
    else: #종료
        print('프로그램 종료')
        break

print(Membership)
    
