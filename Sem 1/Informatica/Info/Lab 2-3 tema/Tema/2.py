year = int(input("year= "))
day_num = int(input("days= "))
ok = 0
if year % 4 == 0 and year % 100 != 0:
    ok = 1
elif year % 400 == 0:
    ok = 1
if day_num <= 31:
    print(day_num, 1, year)
if ok == 1:
    if day_num <= 60:
        print(day_num - 31, 2, year)
    elif day_num <= 91:
        print(day_num -60, 3, year)
    elif day_num <= 121:
        print(day_num - 91, 4, year)
    elif day_num <= 152:
        print(day_num - 121, 5, year)
    elif day_num <= 182:
        print(day_num - 152, 6, year)
    elif day_num <= 213:
        print(day_num - 182, 7, year)
    elif day_num <= 244:
        print(day_num - 213, 8, year)
    elif day_num <= 274:
        print(day_num - 244, 9, year)
    elif day_num <= 305:
        print(day_num - 274, 10, year)
    elif day_num <= 335:
        print(day_num - 305, 11, year)
    elif day_num <= 366:
        print(day_num - 335, 12, year)
else:
    if day_num <= 59:
        print(day_num - 31, 2, year)
    elif day_num <= 90:
        print(day_num -59, 3, year)
    elif day_num <= 120:
        print(day_num - 90, 4, year)
    elif day_num <= 151:
        print(day_num - 120, 5, year)
    elif day_num <= 181:
        print(day_num - 151, 6, year)
    elif day_num <= 212:
        print(day_num - 181, 7, year)
    elif day_num <= 243:
        print(day_num - 212, 8, year)
    elif day_num <= 273:
        print(day_num - 243, 9, year)
    elif day_num <= 304:
        print(day_num - 273, 10, year)
    elif day_num <= 334:
        print(day_num - 304, 11, year)
    elif day_num <= 365:
        print(day_num - 334, 12, year)