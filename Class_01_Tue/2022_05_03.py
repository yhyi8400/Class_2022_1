# 2022. 05. 03

##cnt = 1
##while cnt <= 10:
##    print('cnt:',cnt)
##    cnt = cnt + 1
##print('최종 cnt값:',cnt)
##print('프로그램 종료')

##cnt = 10
##while cnt <= 100:
##    print('cnt:',cnt)
##    cnt = cnt + 10
##print('최종 cnt값:',cnt)
##print('프로그램 종료')


##cnt = 1
##tot = 0 # 전체 합
##e_tot = 0 # 짝수 합
##o_tot = 0 # 홀수 합
##while cnt <= 10:
##    
##    tot = tot + cnt
##    if cnt % 2 == 0:
##        e_tot = e_tot + cnt
##    else:
##        o_tot = o_tot + cnt
##        
##    print('cnt,tot,e_tot,o_tot:',cnt,tot, e_tot,o_tot)
##    
##    cnt = cnt + 1
##    
##print('최종 cnt값:',cnt)
##print('1-10까지 합:',tot)
##print('1-10까지 짝수의 합:',e_tot)
##print('1-10까지 홀수의 합:',o_tot)
##print('프로그램 종료')

##dan = int(input('단 입력:'))
##cnt = 1
##print('===== %d 단====='%dan)
##while cnt<=9:
##    print('%d x %d = %d'%(dan,cnt,dan*cnt))
##
##    cnt = cnt + 1


# 숫자 2개를 입력
# 반드시 첫번째 숫자가 두번째 숫자보다 적을 경우
# 첫번째 숫자부터 두번째 숫자까지의 합을 구하시오.
# 만약 첫번째 숫자가 두번째 숫자보다 클 경우는
# '프로그램 종료' 출력
# 숫자 2개 입력
##n1 = int(input('첫번째 수:'))
##n2 = int(input('두번째 수:'))
##cnt=n1
##if n1 < n2:
##    tot = 0
##    while n1 <= n2:
##        tot = tot + n1
##        n1 = n1 + 1
##    print('%d ~ %d 합: %d'%(cnt,n2,tot))
##else:
##    print('프로그램 종료')
##


##for x in range(1,11):
##    print(x)

# 10 - 20 가지 합
##tot = 0
##for x in range(10,21):
##    tot = tot + x
##
##print('10-20 total:',tot)

##dan = int(input('단 입력:'))
##print('===== %d 단====='%dan)
##for x in range(1,10):
##    print('%d x %d = %d'%(dan,x,dan*x))
    
##score = [75,83,95,99,45,67,55]
##cnt = 1 
##for x in score:
##    #print(x)
##    if x >= 70:
##        print('%d번 학생 %d는 1급'%(cnt,x))
##    elif x >= 60:
##        print('%d번 학생 %d는 2급'%(cnt,x))
##    else:
##        print('%d번 학생 %d는 불합격'%(cnt,x))
##
##    cnt = cnt + 1
        
##score = [75,83,95,99,45,67,55]
##print(len(score))
##for x in range(len(score)):
##    #print(x)
##    if score[x] >= 70:
##        print('%d번 학생 %d는 1급'%(x+1,score[x]))
##    elif score[x] >= 60:
##        print('%d번 학생 %d는 2급'%(x+1,score[x]))
##    else:
##        print('%d번 학생 %d는 불합격'%(x+1,score[x]))

##
##score = [75,83,95,99,45,67,55]
##tot = 0
##for x in score:
##    tot = tot + x
##
##avg = tot/len(score)
##print('점수들의 합:',tot)
##print('점수들의 평균:%.1f'%avg)
    
##flag = True
##while flag:
##    inData = int(input('1, 2:'))
##    if inData ==1:
##        flag = True
##    else:
##        flag = False
##
##print('end')

##while True:
##    inData = int(input('1, 2:'))
##    if inData ==1:
##        print('계속')
##    else:
##        print('end')
##        break


##for x in range(1,11):
##    if x == 5:
##        continue
##    print(x)
##    print(x*x)
##    print(x*x*x)
##    print(x*x*x*x)

##for x in range(2,10):
##    print('===== %d 단====='%x)
##    for y in range(1,10):
##        print('%d x %d = %d'%(x,y,x*y))

