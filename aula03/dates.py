

def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

def monthDays(year, month):
    if isLeapYear(year) == True:
        MONTHDAYS = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    else:
        MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = MONTHDAYS[month]
    return days

def nextDay(year, month, day):
    if day == monthDays(year, month):
        if month == 12:
            day = 1
            month = 1
            year += 1
        else:
            day = 1
            month += 1
    else:
        day += 1
    return year, month, day

def dateIsValid(year, month, day):
    if 0 < month > 12:
        return False
    elif year < 0:
        return False
    elif day <= monthDays(year, month):
        return True
    else:
        return False

def previousDay(year, month, day):
    if month == 1 and day == 1:
        day = 31
        month = 12
        year -= 1
    elif month == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] and day == 1:
        month -= 1
        day = monthDays(year, month)
    else:
        day -= 1 

    return year, month, day

def main():
    print("The date is valid?", dateIsValid(2017, 1, 30))
    print("The date is valid?", dateIsValid(-2, 1, 31))
    print("The date is valid?", dateIsValid(2017, 2, 28))
    print("The date is valid?", dateIsValid(2016, 2, 29))
    print("The date is valid?", dateIsValid(2017, 12, 32))
    print("The date is valid?", dateIsValid(2017, 14, 30))

    
    print("Was", 2017, "a leap year?", isLeapYear(2017))    
    print("Was", 2016, "a leap year?", isLeapYear(2016))    
    print("Was", 2000, "a leap year?", isLeapYear(2000))    
    print("Was", 1900, "a leap year?", isLeapYear(1900))    
    
    print("January 2017 had", monthDays(2017, 1), "days")   
    print("February 2017 had", monthDays(2017, 2), "days")  
    print("February 2016 had", monthDays(2016, 2), "days")  
    print("February 2000 had", monthDays(2000, 2), "days")  
    print("February 1900 had", monthDays(1900, 2), "days")  
    
    y, m, d = nextDay(2017, 1, 30)
    print(y, m, d)
    y, m, d = nextDay(2017, 1, 31)
    print(y, m, d)
    y, m, d = nextDay(2017, 2, 28)
    print(y, m, d)
    y, m, d = nextDay(2016, 2, 29)
    print(y, m, d)
    y, m, d = nextDay(2017, 12, 31)
    print(y, m, d)

main()