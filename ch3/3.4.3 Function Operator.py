# random 모듈
from random import * # random 모듈의 모든 기능을 가져다 쓰겠다는 의미

print(random()) # 0이상 1미만 난수를 뽑는 기능
print(random())
print(random())

print(random() * 10) # 0.0 이상 10.0 미만에서 난수 생성
print(int(random() * 10)) # 0이상 10미만 정수에서 난수 생성 (random()결과를 int()로 감싸서 정수로 변환)
print(int(random() * 10) + 1) # 1이상 11미만 정수에서 난수 생성 (random()결과를 정수로 변환해 1을 더함)

print(int(random() * 45) + 1)

print(randrange(1, 46)) # 1 이상 46 미만에서 난수 생성
print(randint(1, 45)) # 1 이상 45 이하에서 난수 생성

print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))