'''
# 카드 잔액 확인
money = int(input("잔액을 입력하세요: "))
if money > 1200:
    print("탑승하세요.")
else:
    print("잔액이 부족합니다. 충전하세요.")
'''

'''
# 오디오 음량
print("음량은 1부터 10까지 조정할 수 있습니다.")
vol = int(input("원하는 음량을 입력하세요: "))
if vol >= 7:
    print("음량이 너무 높습니다. 권장 음량 제한은 6까지입니다. 줄이세요.")
else:
    print("적당합니다.")
'''

# 3의 배수
num = int(input("양의 정수를 입력하세요: "))
if num%3 == 0:
    print(num, "은 3의 배수 입니다.")
else:
    print(num, "은 3의 배수가 아닙니다.")
