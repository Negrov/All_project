import datetime


time = '13:12:13-15:13:12'
print(*[datetime.time(*[int(j) for j in i.split(':')]) for i in time.split('-')])