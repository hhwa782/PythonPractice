'''
# 별의 개수
s = int(input("원하는 별의 개수를 입력하세요."))
print("*" * s + "홍길동" + "*" * s)
print("\n\n")
'''

# 별 다이아몬드
print("------별 다이아몬드 출력(2)------\n")
print("%10s"%"*")
print("%10s"%"***")
print("%10s"%"*****")
print("%10s"%"*******")
print("%10s"%"*********")

print("\n\n\n")

# 정렬
print("1234567891")
print("%10s" % "PYTHON")

print('-------------------------------')
print('{:>10} 오른쪽 정렬'.format('*')) # 오른쪽 정렬
print('{:<10} 왼쪽 정렬'.format('*')) # 왼쪽 정렬
print('{:^10} 가운데 정렬'.format('*')) # 가운데 정렬

print('-------------------------------')
print('format() 사용')
print('{:^10}'.format('*'))
print('{:^10}'.format('***'))
print('{:^10}'.format('*****'))

print('-------------------------------')
print('center() 사용')
print('*'.center(10))
print('***'.center(10))
print('*****'.center(10))
