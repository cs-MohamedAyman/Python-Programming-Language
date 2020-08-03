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

def is_valid_date(year, month, day):
    return 1 <= year <= 9999 and \
           1 <= month <= 12 and \
           1 <= day <= days_in_month(year, month)

print(is_valid_date(2000, 2, 29))
print(is_valid_date(2010, 4, 31))
print(is_valid_date(2020, 8, 32))
print(is_valid_date(2100, 2, 29))
