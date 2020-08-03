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

def next_date(year, month, day):
    day += 1
    if day > days_in_month(year, month):
        day = 1
        month += 1
    if month == 13:
        month = 1
        year += 1
    return year, month, day

print(next_date(2010, 1, 1))
print(next_date(2010, 1, 31))
print(next_date(2100, 2, 28))
print(next_date(2010, 12, 31))
