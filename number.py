'''
# 큰 수와 짝수홀수
num1 = int(input("첫 번째 정수를 입력하세요 : "))
num2 = int(input("두 번째 정수를 입력하세요 : "))

if num1 >= num2:
    if num1 % 2 == 0:
        print(num1, "이 큰 수이고, 짝수이다.")
    else:
        print(num1, "이 큰 수이고, 홀수이다.")
else:
    if num2 % 2 == 0:
        print(num2, "이 큰 수이고, 짝수이다.")
    else:
        print(num2, "이 큰 수이고, 홀수이다.")
'''

'''
# 양수, 0, 음수(if-elif-else)
num = int(input('정수를 입력하시오: '))
if num == 0:
    print('0입니다.')
elif num > 0:
    print('양수입니다.')
else:
    print('음수입니다.')
'''

# 10부터 20 사이에 홀수를 출력하는 프로그램(for문)
for i in range(11, 21, 2):
    print(i, end=",")
