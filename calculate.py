op1=int(input("계산할 첫번째 숫자를 입력하세요: "))
oper=input("연산자를 입력하세요: ")
op2=int(input("계산할 두번째 숫자를 입력하세요: "))
if oper == "+":
    result = op1 + op2
if oper == "-":
    result = op1 - op2
if oper == "*":
    result = op1 * op2
if oper == "/":
    result = op1 / op2
print(op1, oper, op2, "=", result)
