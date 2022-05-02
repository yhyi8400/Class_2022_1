# 2022. 05. 02(Mon.)

##cnt = 1
##tot = 0
##while cnt<=10:
##    tot = tot + cnt
##    print('cnt, tot:',cnt,tot)
##    cnt = cnt + 1
##
##print('종료 후 cnt 값:',cnt)

##cnt = 1
##tot = 0
##e_tot = 0
##o_tot = 0
##while cnt<=10:
##    tot = tot + cnt
##    if cnt % 2 == 0: e_tot = e_tot + cnt
##    else: o_tot = o_tot + cnt
##    print('cnt, tot, e_tot, o_tot:',cnt,tot,e_tot,o_tot)
##    cnt = cnt + 1
##
##print('종료 후 cnt 값:',cnt)

##dan = int(input('단 입력:'))
##cnt = 1
##while cnt<=9:
##    
##    print('%d X %d =%d'%(dan,cnt,dan*cnt))
##    cnt = cnt + 1
##
##print('종료 후 cnt 값:',cnt)

##for i in range(1,11):
##    print(i)

##e_tot=0
##for i in range(1,11):
##    if i % 2 == 0:
##        e_tot = e_tot + i
##print('e_tot:',e_tot)

##tot = 0
##num = int(input('Num:'))
##for i in range(1,num+1):
##    tot = tot + i
##
##print(tot)

##for i in range(30,51):
##    print(i)    

##s_num = int(input('Start Num:'))
##e_num = int(input('End Num:'))
##tot = 0
##for i in range(s_num,e_num+1):
##    tot = tot + i
##
##print(tot)

##dan = int(input('단 입력:'))
##
##for cnt in range(1,10):
##    print('%d X %d =%d'%(dan,cnt,dan*cnt))


##score = [75,83,95,99,45,67,55]
##for i in score:
##    if i >= 70: print('%d는 1급'%i)
##    elif i >= 60: print('%d는 2급'%i)
##    else: print('%d는 불합격'%i)
##    

##이름 = '안동대학교'
##for x in 이름:
##    print(x)

##이름 = '안동대학교'
##
###print(len(이름))
##for x in range(len(이름)):
##    #print(x)
##    print('[%d] -> %s'%(x,이름[x]))


##flag =True
##while flag:
##    inputData = int(input('1: 진행, 2:종료'))
##    if inputData == 1:
##        flag =True
##        print('게임 계속 진행')
##    else:
##        flag =False
##        print('게임 종료')
##        

##while True:
##    inputData = int(input('1: 진행, 2:종료'))
##    if inputData == 1:
##        print('게임 계속 진행')
##    else:
##        print('게임 종료')
##        break
        
##for i in range(1,51):
##    if (i%5==0) and (i%7==0):
##        continue
##    print('number:',i)
##

##for i in range(2,10):
##    print('======= %d단 ========='%i)
##    for j in range(1,10):
##        print('%d x %d = %d'%(i,j,i*j))

# 369게임
##n = 1
##while n<=50:
##    #if n%3 == 0 or n%10==3:
##    if n%3 == 0 or '3' in str(n):
##        print('박수')
##    else:
##        print(n)
##
##    n=n+1
##print('프로그램 종료')

##for i in range(5):
##    for j in range(5):
##        print('*',end='')
##    print('')



##
##for i in range(1,6):
##    for j in range(1,i+1):
##        print('*',end='')
##    print('')


