# 2022. 04. 12.
# 5주차 과제 1
#1.
##first_name = input('이름:')
##last_name = input('성:')
##name = first_name + ' ' + last_name
##print('이름: ',name)

#2.
##address = '경상북도 안동시 경동로 1234 국립안동대학교'
##print('안동대 주소:',address)

#3.
##address = '경상북도 안동시 경동로 1234 국립안동대학교'
##number = address[13:17]
##print('번지:',number)

#4.
##address = '경상북도 안동시 경동로 1234 국립안동대학교'
##result = address.replace('1234','1375')
##print(result)

#5.
##address = '경상북도 안동시 경동로 1234 국립안동대학교'
##print(address.find('안동시'))

## 5주차 과제 2
#1.
##food =['사과', '배', '바나나', '오렌지', '우유', '빵']
##print(food)

#2.
##food =['사과', '배', '바나나', '오렌지', '우유', '빵']
##new_food = input('새로운 음식:')
##food.append(new_food)
##print(food)

##3.
##letters = ['a', 'b', 'c', 'd', 'e', 'f']
##slice_letter = letters[2:5]
##print(slice_letter)

#4.
##a = range(1,11,3)
##print(list(a))

###5.
##a = range(10,2,-1)
##print(list(a))


# 6주차 수업 #

##a=30
##b=20
##if a>b:
##    print('a>b')
##    print('program')
##print('good program')

#1.

##score = int(input('점수 입력:'))
##if score >= 90:
##    print('장학금 대상자...')
##
##print('수고했습니다..')


#2.
##year = int(input('출생년도 입력:'))
##age = 2022 - year
##if age >= 15 and age < 20:
##    print('청소년')

#3.
##k_time = int(input('한국시간:'))
##v_time = k_time - 2
##if v_time <= 0:
##    v_time = v_time + 24
##
##print(v_time)

# if ~ else
#1.
##num = int(input('숫자 입력:'))
##result = num % 2
##if result == 0:
##    print('짝수')
##else:
##    print('홀수')
##num = int(input('숫자 입력:'))
##result = num % 2
##if result == 1:
##    print('홀수')
##else:
##    print('짝수')

##num = int(input('숫자 입력:'))
## 
##if num % 2 == 0:
##    print('짝수')
##else:
##    print('홀수')    
##

#2.
##score = int(input('점수:'))
##if score >= 90:
##    print('장학금 대상자')
##    print('축하합니다')
##else:
##    print('다음 학기...')
##
##print('수고했습니다...')
##

#3
##num = int(input('정수:'))
##cal = num/3
##print(cal)
##cal_10 = cal * 10
##print(cal_10)
##print(int(cal_10))
##if (int(cal_10)%10) >= 5:
##    result = cal + 0.5
##else:
##    result = cal
##print('반올림 결과:',int(result))

##kor = int(input('국어:'))
##eng = int(input('영어:'))
##mat = int(input('수학:'))
##avg = (kor+eng+mat)/3

##if avg >= 90:
##    print('시험을 아주 잘 봤군요...')
##elif avg >= 80 and avg < 90:
##    print('시험을 괜찮게 봤군요...')
##elif avg >= 70 and avg < 80:
##    print('시험을 좀 못 봤군요...')
##else:
##    print('다음 기회는 좀 더 분발...')
    
##if avg >= 90:
##    print('시험을 아주 잘 봤군요...')
##elif avg >= 80:
##    print('시험을 괜찮게 봤군요...')
##elif avg >= 70:
##    print('시험을 좀 못 봤군요...')
##else:
##    print('다음 기회는 좀 더 분발...')
##
##if avg >= 90:
##    print('시험을 아주 잘 봤군요...')
##elif 80 <= avg < 90:
##    print('시험을 괜찮게 봤군요...')
##elif 70 <=  avg < 80:
##    print('시험을 좀 못 봤군요...')
##else:
##    print('다음 기회는 좀 더 분발...')
##


#4.
##absence = int(input('결석횟수:'))
##score = int(input('시험점수:'))
##if absence < 3 and score >= 70:
##    print('PASS')
##elif (absence < 3 and 50 <= score < 70) or absence==0:
##    print('재시험 가능자')
##else:
##    print('FAIL')

#5.
##score = int(input('시험점수:'))
##if score >= 70: print('pass')
##else: print('fail')
#

#...#
# 입력이 양의 정수인 경우 짝수와 홀수를 출력하는 프로그램 작성
# 입력이 음수인 경우는 '음수 입니다' 출력

    









