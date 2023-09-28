days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

class Date(object):
    
    def __init__(self, year=1990, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        year = self.year
        month = str(self.month).rjust(2, '0')
        day = str(self.day).rjust(2, '0')
        
        return str(year) + '/' + month + '/' + day

    def same_day_in_year(self, dayT):
        
        if (self.month == dayT.month and self.day == dayT.day):
            return True
        else:
            return False
    
    def is_leap_year(self):
        y = self.year
        
        if (y % 4 == 0):
            if (y % 100 == 0 and y % 400 == 0):
                return True
            elif (y % 100 == 0):
                return False
            else:
                return True
        return False
    
    def __lt__(self, dateT):
        if self.year < dateT.year:
            return True
        elif(self.year == dateT.year):
            if (self.month < dateT.month):
                return True
            elif (self.month > dateT.month):
                return False
            else:
                return (self.day < dateT.day)
        else:
            return False
    
if __name__ == "__main__":
    
    # checkpoint 1
    
    d1 = Date(1900, 3, 27)
    d2 = Date(2000, 4, 13)
    d3 = Date(1996, 4, 13)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print ()
       
    # checkpoint 2
    print("d1 is leap year: {}".format(d1.is_leap_year()))
    print("d2 is leap year: {}".format(d2.is_leap_year()))
    
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1998, 5, 13)
    d4 = Date(1998, 4, 11)
    
    print(d1 < d2)
    print(d2 < d3)
    print(d3 < d4)
    
    