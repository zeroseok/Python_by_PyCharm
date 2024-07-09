name = "연탄이"
animal = "개"
age = 4
hobby = "산책"

print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 개인데, 이름이 연탄이예요.")
# print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요.")
print("연탄이는 4살이고, 산책을 아주 좋아해요.")
# print(name + "는 " + age + "살이고, " + hobby + "을 아주 좋아해요.") # 오류 발생
# print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")


name = "해피"
animal = "고양이"
age = 4
hobby = "낮잠"

print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요.")
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")


name = "연탄이"
animal = "개"
age = 4
hobby = "산책"

print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.") # + 연산자 사용 시
print(name, "는", age, "살이고,", hobby, "을 아주 좋아해요.") # 쉼표 사용 시