# chp4 연습문제

2. 다음 내용을 하나의 조건식으로 만드세요.
- 홀수 달의 15일 또는 짝수 달의 16일이면 "그날"을 출력함.
- 8월 15일이면 "광복절"을 출력함.
- 그 외는 "평일"을 출력함.
- 변수는 month와 day를 사용함.
```
month = 8
day = 15
if month == 8 and day == 15:
    print("광복절")
elif (month % 2 != 0 and day == 15) or (month % 2 == 0 and day == 16):
    print("그날")
else:
    print("평일")
```

3. for 문을 이용해 1~50의 짝수 합을 구하되, 3의 배수는 제외하세요.
```
total_sum = 0
for i in range(1, 51):
    if i % 2 == 0 and i % 3 != 0:
        total_sum += i
print(f"결과: {total_sum}")
```

4. 연습문제 4.3을 while 문으로 해결하세요.(다음 조건을 만족하는 프로그램 작성)
  - 1에서 50까지의 짝수의 합계를 구합니다.
  - 3으로 나누어떨어지는 숫자이면 제외합니다.
  - 합계(sum)를 출력합니다.
```
i = 1
total_sum = 0
while i <= 50:
    if i % 2 == 0 and i % 3 != 0:
        total_sum += i
    i += 1
print(f"결과: {total_sum}")
```
