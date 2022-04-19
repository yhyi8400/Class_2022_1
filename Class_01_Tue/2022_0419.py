# 2022. 04. 19.
# 과제 1
##num = int(input('양의 정수 입력:'))
##if num > 0 and num%3==0:
##    print('정수 %d은(는) 3의 배수이다.'%num)
##elif num > 0 and num%3!=0:
##    print('정수 %d은(는) 3의 배수가 아니다.'%num)
##elif num <= 0:
##    print('잘못된 입력')
    
##num = int(input('양의 정수 입력:'))
##if num > 0:
##    if num%3==0:
##        print('정수 %d은(는) 3의 배수이다.'%num)
##    else:
##        print('정수 %d은(는) 3의 배수가 아니다.'%num)
##else:
##    print('잘못된 입력')

#과제 2
##주차시간 = int(input('주차시간 입력:'))
##if 주차시간 <= 15:
##    pare = 0
##elif 15 < 주차시간 <= 30:
##    pare = 3000
##else:
##    임시_주차시간 = 주차시간 - 30
##    p_pare = 임시_주차시간//15
##    r_pare = 임시_주차시간%15
##    if r_pare > 0:
##        p_pare = p_pare + 1
##    pare = 3000 + p_pare*1000
##
##print('주차시간:%d'%주차시간)
##print('주차요금:%d원'%pare)

# 과제 3
##x = int(input('x좌표:'))
##y = int(input('y좌표:'))
##d = (x**2 + y**2)**0.5
##print('거리 d:',d)
##if d < 10:
##    print('입려된 좌표 (%d, %d)은(는) 원의 내부에 있다.'%(x,y))
##elif int(d) == 10:
##    print('입려된 좌표 (%d, %d)은(는) 원 위에 있다.'%(x,y))
##else:
##    print('입려된 좌표 (%d, %d)은(는) 원의 외부에 있다.'%(x,y))
##    


#과제 4
##year = input('출생년도입력:')
##if year.isdecimal() == True:
##    age = 2022 - int(year)
##    print('당신의 나이는 {}살 입니다'.format(age))
##else:
##    print('입력 오류')

#과제 5
#주민번호 = '021225-3123411'
##주민번호 = input('주민번호 전체 입력:')
##연도 = 주민번호[0:2]
##월 = 주민번호[2:4]
##일 = 주민번호[4:6]
##성별 = 주민번호[7:8]
###print(연도, 월, 일, 성별)
##
##if 성별=='1' or 성별=='2':
##    year = '19'+ 연도
##elif 성별=='3' or 성별=='4':
##    year = '20'+ 연도
##
##print('당신은 %s년도에 태어났어요'%year)
##print('당신의 생일은 %s월 %s일 입니다.'%(월,일))
##print('당신은 올해 %d살 입니다'%(2022-int(year)))
##if 성별=='1' or 성별=='3':
##    print('당신은 남성입니다')
##elif 성별=='2' or 성별=='4':
##    print('당신은 여성입니다')

#과제 6
##num = int(input('양의 정수 입력:'))
##if num%2 == 0:
##    print('{}는(은) 2의 배수이다'.format(num))
##    if num%3 == 0:
##        print('{}는(은) 3의 배수이다'.format(num))
##    elif num%5 == 0:
##        print('{}는(은) 5의 배수이다'.format(num))
##elif num%3 == 0:
##    print('{}는(은) 3의 배수이다'.format(num))
##    if num%2 == 0:
##        print('{}는(은) 2의 배수이다'.format(num))
##    elif num%5 == 0:
##        print('{}는(은) 5의 배수이다'.format(num))
##elif num%5 == 0:
##    print('{}는(은) 3의 배수이다'.format(num))
##    if num%2 == 0:
##        print('{}는(은) 2의 배수이다'.format(num))
##    elif num%3 == 0:
##        print('{}는(은) 3의 배수이다'.format(num))


# 반복문
# 1.

##cnt = 1
##tot = 0
##while cnt<=10:
##    tot = tot + cnt
##    #print('cnt, tot:',cnt,tot)
##    cnt = cnt + 1
##    
##print('1-10 합:',tot)
##print('프로그램 종료')

cnt = 1
e_tot = 0
o_tot = 0
while cnt<=10:
    if cnt % 2 == 0: e_tot = e_tot + cnt
    else:  o_tot = o_tot + cnt

    cnt = cnt + 1
    
print('짝수합:',e_tot)
print('홀수합:',o_tot)
print('프로그램 종료')
