def compare_dates(year1, month1, day1, year2, month2, day2):
    if year1 != year2:
        return 1 if year1 > year2 else -1
    if month1 != month2:
        return 1 if month1 > month2 else -1
    if day1 != day2:
        return 1 if day1 > day2 else -1
    return 0

print(compare_dates(2010, 1, 1,  2011, 1, 1 ))
print(compare_dates(2000, 7, 31, 2000, 4, 30))
print(compare_dates(2010, 1, 1,  2010, 1, 1 ))
