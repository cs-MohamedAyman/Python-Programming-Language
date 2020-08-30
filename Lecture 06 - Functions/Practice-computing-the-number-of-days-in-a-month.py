def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return 29
        else:
            return 28

print(days_in_month(2000, 3))
print(days_in_month(2010, 6))
print(days_in_month(2100, 2))
print(days_in_month(2400, 2))
