import time
import datetime


# time.time()은 epoch time (1970년 1월 1일 0시 0분 0초)부터 현재까지의 시간을 초 단위로 반환
cur_time = time.time()
# datetime.datetime.now()는 datetime 객체를 반환 (추후 가공하여 사용)
cur_date = datetime.datetime.now()

str_1 = f"Seconds since January 1, 1970: {cur_time:,.4f} or {cur_time:.2e} in scientific notation"
str_2 = cur_date.strftime("%b %d %Y") # %b : 월 이름, %m : 월 숫자(2자리)

print(str_1)
print(str_2)
