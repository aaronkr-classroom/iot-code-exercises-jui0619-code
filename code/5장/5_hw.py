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