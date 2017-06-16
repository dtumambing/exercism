def is_leap_year(year):
    if year % 100 == 0 and year % 4 == 0:
        return true
    elif year % 4 == 0:
        return true
    else:
        return  false
