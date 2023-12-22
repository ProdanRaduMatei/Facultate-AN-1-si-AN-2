curday = int(input("current day = "))
curmonth = int(input("current month = "))
curyear = int(input("current year = "))
birthday = int(input("birth day = "))
birthmonth = int(input("birth month = "))
birthyear = int(input("birth month = "))
age = curyear - birthyear
if curmonth < birthmonth:
    age -= 1
elif curmonth == birthmonth:
    if curday < birthday:
        age =- 1
print(age)