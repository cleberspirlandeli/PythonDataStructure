# https://docs.python.org/3/library/datetime.html
# https://docs.python.org/3/library/time.html
# DATE TIME
print('=== DATETIME ===')
import datetime
print(dir(datetime))
# ['MAXYEAR', 'MINYEAR', 'UTC',
# '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',
# 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']

print(datetime.date.today()) # 2024-03-01
print(datetime.datetime.now()) # 2024-03-01 11:23:11.435442

data = datetime.date(2024, 7, 10)
print(data) # 2024-07-10
print(data.day) # 10
print(data.month) # 7
print(data.year) # 2024

horario = datetime.datetime(2024, 7, 10, 7, 30, 0)
print(horario) # 2024-07-10 07:30:00
print(horario.hour) # 07
print(horario.minute) # 30
print(horario.second) # 00
print('\n================\n')


# TIME
print('===== TIME =====')
import time as tm
antes = tm.time()
tm.sleep(2)
depois = tm.time()
intervalo = depois - antes
print(f'Tempo: {intervalo} segundos')


print('\nFinalizando...')
tm.sleep(2)
print('...')
tm.sleep(2)
print('Até a próxima')

print('\n================\n')