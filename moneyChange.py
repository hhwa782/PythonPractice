# 물건 값을 입력 받고 잔돈을 계산하는 프로그램
money, price, change = 0, 0, 0
money = int(input("투입한 돈: "))
price = int(input("물건값: "))

change = money - price
print("거스름돈: ", change)

coin1000s = change // 1000
change = change % 1000
coin500s = change // 500
change = change % 500
coin100s = change // 100
change = change % 100
coin10s = change // 10

print("1000원 지폐의 개수: ", coin1000s)
print("500원 동전의 개수: ", coin500s)
print("100원 동전의 개수: ", coin100s)
print("10원 동전의 개수: ", coin10s)
