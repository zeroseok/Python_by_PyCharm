print(int("3"))
# print(int("3") + "입니다.") # TypeError 발생
print(int(3.5))
# print(int("삼")) # ValueError 발생

print(float("3.5"))
print(float(3))

# print(float("오")) # ValueError 발생
print(str(3) + "입니다.")
print(str(3.5) + "입니다.")


print(type(3)) # 정수(int)
print(type("3")) # 문자열(str)
print(type(3.5)) # 실수(float)
print(type(str(3))) # 정수(int)를 문자열(str)로 형변환