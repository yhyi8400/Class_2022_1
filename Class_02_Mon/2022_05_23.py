# 2022. 05. 23
# 문제1.
def name(이름):
    print('나의 이름은 %s입니다'%이름)
##
##for x in range(5):
##    name('yeung')

# 문제2.
##본인이름 = input('본인 이름 입력:')
##count = int(input('횟 수 입력:'))
##for x in range(count):
##    name(본인이름)


# 문제 3.
##def cir_area(r):
##    area = r*r*3.14
##    return area
##
##def square_area(x,y):
##    area = x*y
##    return area
##
##def tri_area(x,h):
##    area = (x*h)/2
##    return area
##
##while True:
##    cir_r = int(input('반지름 입력:'))
##    sq_x =int(input('사각형의 가로 길이:'))
##    sq_y =int(input('사각형의 세로 길이:'))
##    tr_x = int(input('삼각형의 밑변 길이:'))
##    tr_h = int(input('삼각형의 높이 길이:'))
##
##    c_area = cir_area(cir_r)
##    sq_area = square_area(sq_x, sq_y)
##    tr_area = tri_area(tr_x,tr_h)
##    if c_area == 0 or sq_area == 0 or tr_area == 0:
##        print('면적이 0 이므로 프로그램 종료')
##        break
##    else:
##        print('원의 넓이: %.1f'%c_area)
##        print('사각형의 넓이: %.1f'%sq_area)
##        print('삼각형의 넓이: %.1f'%tr_area)
##        

import math

#print('%.1f'%math.pi)

#print('%.1f'%math.e)
#print('3.6의 소수점 절삭:%.1f'%math.floor(3.6))
#print('5.1의 무조건 올림:%.1f'%math.ceil(5.1))
#print('3.6의 무조건절삭:%.1f'%math.trunc(3.6))
#print('6.3의 반올림:%.1f'%round(6.3))
#print('6.6의 반올림:%.1f'%round(6.6))

##angle = int(input('각도:'))
##dist = int(input('거리:'))
##h= dist*math.tan(math.radians(angle))
##print('건물의 높이는 %.2fM 입니다'%h)



##for x in range(10):
##    #print('random number:%.3f'%(random.random()))
##    #print('random number:%d'%(random.randint(0,9)))
##    #print('random number:%d'%(random.randrange(0,9)))
##    print('random sample number:',random.sample(range(0,10),3))

##listVar = [1,2,3,4,5]
##print('choice:',random.choice(listVar))
##random.shuffle(listVar)
##print(listVar)

import random
cnt = 1
while True:
    print('주사위 던지기: %d번째'%cnt)
    me = random.randint(1,6)
    com = random.randint(1,6)
    if me > com:
        print('나:',me)
        print('컴퓨터',com)
        print('나의 승리')
    elif me < com:
        print('나:',me)
        print('컴퓨터',com)        
        print('컴퓨터의 승리')
    else: print('비겼음')
        
    answer = input('게임 계속 여부(Y:게임 계속), (N:게임 종료):')
    if answer == 'y':
        print('게임 계속')
    else:
        print('게임 종료')
        break

    cnt =  cnt + 1












    
