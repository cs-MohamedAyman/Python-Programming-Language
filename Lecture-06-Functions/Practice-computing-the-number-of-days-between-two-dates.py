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

def compare_dates(year1, month1, day1, year2, month2, day2):
    if year1 != year2:
        return 1 if year1 > year2 else -1
    if month1 != month2:
        return 1 if month1 > month2 else -1
    if day1 != day2:
        return 1 if day1 > day2 else -1
    return 0

def next_date(year, month, day):
    day += 1
    if day > days_in_month(year, month):
        day = 1
        month += 1
    if month == 13:
        month = 1
        year += 1
    return year, month, day

def days_between(y1, m1, d1, y2, m2, d2):
    if not is_valid_date(y1, m1, d1) or \
       not is_valid_date(y2, m2, d2):
       return 0

    cur_y, cur_m, cur_d = y1, m1, d1
    n_days = 0
    while compare_dates(cur_y, cur_m, cur_d, y2, m2, d2) == -1:
        n_days += 1
        cur_y, cur_m, cur_d = next_date(cur_y, cur_m, cur_d)

    return n_days

print(days_between(2010, 1, 1,  2011, 1, 1 ))
print(days_between(2000, 4, 30, 2000, 7, 31))
print(days_between(2010, 1, 1,  2000, 12,31))
print(days_between(2020, 4, 31, 2020, 7, 31))
