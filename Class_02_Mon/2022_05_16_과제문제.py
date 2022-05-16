#문제1.
##listNumber=[]
##for x in range(1,101):
##    listNumber.append(x)
##
##e_tot=0
##o_tot=0
##for x in listNumber:
##    if x % 2 == 0: e_tot = e_tot+x
##    else: o_tot = o_tot+x
##        
##print('짝수 합:',e_tot)
##print('홀수 합:',o_tot)

#문제2.
##myTuple = ('A','B','C','D','E')
##for x in myTuple:
##    print(x, end=', ')

#문제3.
##myTuple = ('태권도',' 축구', '수영', '야구', '등산', '권투', '농구', '양궁')
##for x in range(len(myTuple)):
##    if x % 2 == 1:
##        print('%d 번째 종목: %s'%(x, myTuple[x]))

#문제4.
foods = {'떢볶이':'오뎅',
         '짜장면':'단무지',
         '라면':'김치',
         '피자':'피클',
         '맥주':'땅콩',
         '치킨':'무김치',
         '감겹살':'상추'}

print(foods.keys())
print(foods.values())
print(list(foods.keys()))
myList = list(foods.keys())
print('라면' in myList)

"""
while True:
    food_name = input('음식 이름을 입력하시오.:')
    myfoodList = list(foods.keys())
    if food_name in myfoodList:
        print('%s 궁합 음식은 %s입니다.'%(food_name,foods.get(food_name)))
    elif food_name == '끝':
        print('프로그램 종료')
        break
    else:
        print('목록에 없는 음식입니다')
        
"""

