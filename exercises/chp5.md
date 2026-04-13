# chp5 연습문제

3. 다음 조건으로 클래스와 그 클래스를 사용하는 프로그램을 만드세요.
* [조건1] 클래스 만들기
- 클래스 이름 : SayDays
- 오브젝트 만들 때 전달할 매개변수 : year, month, day
- 입력된 year를 기준으로 윤년(2월이 29일까지 있는 해)을 찾아야 함
- 메소드 days( ) : 당해년도 1월 1일 기준으로 몇째 날인지 알려줌
- 메소드 days_left( ) : 당해년도 12월 31일 기준으로 남은 일수를 알려줌
- 메소드 weekday( ) : 숫자로 요일을 알려줌( 0 : 토요일)
- 메소드 weekday_name( ) : 요일을 한글로 알려줌( 0 : 토요일)
- 요일 계산은 Zeller 계산법에 따름
- import 문은 사용하지 말 것
* [조건2] 앞에서 만든 클래스를 사용해 다음과 같이 프로그램 만들기
- SayDays 오브젝트 생성
- while True :
- input 문으로 임의의 날짜 입력받음
- days( ), days_left( ), week( ), week_name( )을 출력


```
class SayDays:
    def __init__(self, year, month, day):
        self.y = year
        self.m = month
        self.d = day

    def is_leap(self, y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    def days(self):
        month_days = [31, 28 + self.is_leap(self.y), 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]
        return sum(month_days[:self.m - 1]) + self.d

    def days_left(self):
        total = 366 if self.is_leap(self.y) else 365
        return total - self.days()

    def weekday(self):
        y = self.y
        m = self.m
        d = self.d

        if m < 3:
            m += 12
            y -= 1

        K = y % 100
        J = y // 100

        h = (d + (13*(m+1))//5 + K + K//4 + J//4 + 5*J) % 7
        return (h + 6) % 7

    def weekday_name(self):
        names = ["일", "월", "화", "수", "목", "금", "토"]
        return names[self.weekday()]


while True:
    y = int(input("년 입력: "))
    m = int(input("월 입력: "))
    d = int(input("일 입력: "))

    date = SayDays(y, m, d)

    print("경과 일수 :", date.days())
    print("남은 일수 :", date.days_left())
    print("요일 이름 :", date.weekday_name())
    print("-" * 20)
```
