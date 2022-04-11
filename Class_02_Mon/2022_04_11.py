# 2022. 04. 11.
# 5주차 과제1
#1.
#first_name = input('이름을 입력:')
#last_name = input('성을 입력:')
#name = first_name +' '+ last_name
#print(name)
#2.
#address = '경상북도 안동시 경동로 1234 국립안동대학교'
#print(address)

#3.
#number = address[13:17]
#print(number)

#4.
#address=address.replace('1234','1375')
#print(address)
#print(address.find('안동시'))

# 5주차 과제2
#1.
#food = ['사과', '배', '바나나', '오렌지', '우유', '빵']
#print(food)

#2.
#food = ['사과', '배', '바나나', '오렌지', '우유', '빵']
#new_food = input('새로운 음식 입력:')
#food.append(new_food)
#print(food)

#3.
#letters = ['a', 'b', 'c', 'd', 'e', 'f']
#print(letters[2:5])

#4.
#a = range(1,11,3)
#print(list(a))

#5.
#b = range(10,2,-1)
#print(list(b))


#a = 10
##a = 30
##if a < 20 :
##    print('10<20')
##    print('if 조건문')
##print('프로그램 종료')

##a = int(input('숫자 입력:'))
##if a < 20 :
##    print('10<20')
##    print('if 조건문')
##print('프로그램 종료')


##점수 = int(input('점수 입력:'))
##if 점수 >= 90 :
##    print('장학금 대상자')
##print('수고했습니다.')


##year = int(input('출생년도 입력:'))
##age = 2022 - year
##if age >=15 and age < 20 :
##    print('당신은 청소년')


##k_time = int(input('한국시간 입력:'))
##b_time = k_time - 2
##if b_time <= 0:
##    b_time = b_time + 24
##
##print('한국 시간: %d시, 베트남 시간: %d시'%(k_time,b_time))


##num = int(input('숫자 한 개 입력:'))
##if (num % 2) == 0 :
##    print('짝수')
##else:
##    print('홀수')

##num = int(input('숫자 한 개 입력:'))
##if num < 0 :
##    print('음수')
##else:
##    print('양수')
##
##if num > 0 :
##    print('양수')
##else:
##    print('음수')

##print('시험 점수를 입력하시오')
##score = int(input('점수입력:'))
##if score >= 90:
##    print('장학금 대상자')
##    print('축하합니다')
##else:
##    print('다음 학기를 노려봅시다')
##
##print('수고했습니다')

##num = int(input('정수 입력:'))
##red = num/3
##print('num/3 =>',red)
##mult_red = red * 10
##print('mult_red =>',mult_red)
##print(int(mult_red)%10)
##if int(mult_red)%10 >=5:
##    result = red +0.5
##else:
##    result=red
##print('입력값/3 = %.1f의 반올림 값은 %d'%(red,int(result)))
##

##a = [2,'a', 3,'c','b',1]
##a.reverse()
##print(a)
##b = [2,3,1]
###b.sort()
##print(b)
##b.sort(reverse=True)
##print(b)


##kor = int(input('국어 점수:'))
##eng = int(input('영어 점수:'))
##mat = int(input('수학 점수:'))
##
##avg = (kor + eng + mat)/3
##print('평균 점수: %.1f'%avg)

# M1.
##if avg >= 90:
##    print('시험을 잘 봤군요...')
##elif avg < 90 and avg >= 80:
##    print('시험을 괜찮게 봤군요...')
##elif avg < 80 and avg >= 70:
##    print('시험을 좀 못봤군요...')
##else:
##    print('좀 더 분발...')

#M2.
##if avg >= 90:
##    print('시험을 잘 봤군요...')
##elif avg >= 80:
##    print('시험을 괜찮게 봤군요...')
##elif avg >= 70:
##    print('시험을 좀 못봤군요...')
##else:
##    print('좀 더 분발...')

# M3.
##if avg >= 90:
##    print('시험을 잘 봤군요...')
##elif 80 <= avg < 90:
##    print('시험을 괜찮게 봤군요...')
##elif 70 <= avg < 80:
##    print('시험을 좀 못봤군요...')
##else:
##    print('좀 더 분발...')


##결석 = int(input('결석횟수 입력:'))
##점수 = int(input('시험점수 입력:'))
##if 결석<3 and 점수>=70:
##    print('pass')
##elif (결석<3 and (점수>=50 and 점수<70)) or 결석==0:
##    print('재시험 가능자')
##else:
##    print('fail...')


# 입력된 양수에 대해서만 홀수와 짝수를 구분하는 프로그램 작성...
# 음수인 경우는 "판정을 할 수 없습니다"을 출력
# 양수인 경우는 "양수-홀수" 혹은 "양수-짝수" 출력
















