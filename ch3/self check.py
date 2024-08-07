"""
연산자를 이용해 온도 단위를 변환하는 프로그램 만들기
조건:
1. 섭씨 온도를 저장하기 위한 변수를 만든다.
2. 다음 공식을 이용해 섭씨온도를 화씨온도로 변환하고 새로운 변수에 저장한다.
화씨온도 = (섭씨온도 * 9 / 5) + 32
"""

# 섭씨 온도가 30도일 때
celsius = 30
fahrenheit = (celsius * 9 / 5) + 32
print("섭씨 온도 : " + str(celsius))
print("화씨 온도 : " + str(fahrenheit))