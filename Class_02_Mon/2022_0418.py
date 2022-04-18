# 2022.04.18.
# 과제 1
# 방법1
##num = int(input('양의 정수 입력:'))
##if num > 0 and num%3 == 0:
##    print('정수 %d는(은) 3의 배수이다'%num)
##elif num <=0:
##    print('잘못된 입력입니다')
##else:
##    print('정수 %d는(은) 3의 배수가 아니다'%num)
# 방법 2
##num = int(input('양의 정수 입력:'))
##if num > 0:
##    if num%3 == 0:
##        print('정수 %d는(은) 3의 배수이다'%num)
##    else:
##        print('정수 %d는(은) 3의 배수가 아니다'%num)
##       
##else:
##    print('잘못된 입력입니다')

# 과제 2

##p_time = int(input('주차시간 입력:'))
##if p_time <= 15:
##    pare = 0
##elif 15 < p_time <= 30:
##    pare = 3000
##else:
##    imsi_time = p_time - 30
##    i_time = imsi_time//15
##    o_time = imsi_time%15
##    if o_time > 0:
##        i_time = i_time + 1
##        
##    pare = 3000 + i_time*1000
##    
##print('주차시간:%d분'%p_time)
##print('주차요금:%d원'%pare)

# 과제 3
##
##x = int(input('X좌표:'))
##y = int(input('Y좌표:'))
##d = (x**2 + y**2)**0.5
##print('거리:',d)
##if d < 10:
##    print('입력된 좌표 (%d, %d)은(는) 원의 내부에 있다'%(x,y))
##elif d == 10:
##    print('입력된 좌표 (%d, %d)은(는) 원 위에 있다'%(x,y))
##else:
##    print('입력된 좌표 (%d, %d)은(는) 원의 외부에 있다'%(x,y))
##    

#과제4
##y = input('출생년도 입력:')
##if y.isdecimal() == True:
##    age = 2022-int(y)
##    print('당신의 나이는 %d입니다'%age)
##else:
##    print('잘못된 입력')

#과제5

##주민번호 = input('주민번호입력:')
###주민번호 = '891225-2123411'
##년도 = 주민번호[0:2]
##월 = 주민번호[2:4]
##일 = 주민번호[4:6]
##성별 = 주민번호[7:8]
##if 성별 == '1' or 성별 == '2':
##    y = '19'
##else:
##    y = '20'
##출생년도 = y+년도
##age = 2022 - int(출생년도)
##print('당신은 %s년도에 태어났어요'%출생년도)
##print('당신의 생일은 %s월 %s일 입니다.'%(월,일))
##print('당신은 올해 %d살 입니다.'%age)
##if 성별 == '1' or 성별 == '3':
##    print('당신은 남성입니다.')
##elif 성별 == '2' or 성별 == '4':
##    print('당신은 여성입니다.')    

# 과제 6
# 키와 몸무게를 입력
# 키는 cm 단위로 입력, 몸무게는 kg 단위로 입력
# BMI 수치 계산 후 소수 둘 째 자리까지 표현
# BMI 계산 방법: 몸무게(kg)를 키(m)의 제곱으로 나눈다.
# BMI 지수를 출력(소수 둘 째 자리까지)
# 판단 근거
#  BMI < 20         -> 저체중 범위
# 20 <= BMI < 25    -> 정상체중 범위
# 25 <= BMI < 30    -> 경도비만 범위
# 30 <= BMI < 40    -> 비만 범위
#  BMI >= 40        -> 고도비만 범위

##키 = int(input('키 입력:'))
##몸무게 = int(input('몸무게 입력:'))
##미터키 = 키/100
##BMI = 몸무게 / (미터키*미터키)
##print('당신의 BMI 지수는 %.2f입니다'%BMI)
##if BMI < 20: print('저체중 범위')
##elif 20 <= BMI < 25: print('정상체중 범위')
##elif 25 <= BMI < 30: print('경도비만 범위')
##elif 30 <= BMI < 40: print('비만 범위')
##else: print('고도비만 범위')

##cnt = 0
##합 = 0
##while cnt<10:
##    cnt = cnt + 1
##    합 = 합 + cnt
##    print('cnt:%d'%cnt)
##
##print('합:',합)

##cnt = 0
##짝수합 = 0
##홀수합 = 0
##while cnt<10:
##    cnt = cnt + 1
##    if cnt%2 == 0:
##        짝수합 = 짝수합 + cnt
##    else:
##        홀수합 = 홀수합 + cnt
##        
##    print('cnt:%d'%cnt)
##
##print('짝수합:',짝수합)    
##print('홀수합:',홀수합)
##
##cnt = 10
##while cnt <= 100 :
##    print(cnt)
##    cnt = cnt + 10
##    

cnt = 1
합=0
while cnt <= 10:
    if cnt%3 == 0:
        print(cnt)
        합 = 합 + cnt
    cnt = cnt + 1
print('3의 배수 합:',합)






