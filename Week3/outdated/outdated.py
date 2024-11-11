def main():

    months = {

        "January" : "01",
        "February" : "02",
        "March" : "03",
        "April" : "04",
        "May" : "05",
        "June" : "06",
        "July" : "07",
        "August" : "08",
        "September" : "09",
        "October" : "10",
        "November" : "11",
        "December" : "12"
    }

    day, month, year = date(months)
    print(year, month, day, sep = "-")

def date(j):
    while True:
        date = input("Date: ")

        #checks to see which formt the date was input as
        if "/" in date:

            date = date.split("/")

            month = date[0]
            day = date[1]
            year = date[2]

            try:
                month = int(month)
                pass
            except ValueError:
                continue

            try:
                if ckday(day) == True:
                    pass
                else:
                    raise KeyError

            except KeyError:
                continue

            try:
                if ckmonth(month) == True:
                    pass
                else:
                    raise KeyError

            except KeyError:
                continue

            day = chday(day)
            month = chmonth(month)

            return str(day), str(month), int(year)

        #checks to see if the input is not valid, repromts
        elif  "/" not in date and "," not in date:
            continue

        #checks to see which format the date was input as
        else:

            date = date.split(" ")

            month = date[0]
            day = date[1]
            year = date[2]

            #checks to make sure the month is before the day in the input
            try:
                month = change_month(month, j)

            except KeyError:
                continue

            day = day[:-1]

            try:
                if ckday(day) == True:
                    pass
                else:
                    raise KeyError

            except KeyError:
                continue

            day = chday(day)
            month = chmonth(month)

            return str(day), str(month), int(year)


#take in a month as a str and output the int version
def change_month(i,j):
    if not isinstance(i, int):
        return(j[i])

#checks to make sure the day value is valid
def ckday(day):
    if 1 <= int(day) <= 31:
        return True
    else:
        return False

#checks to make sure the month value is valid
def ckmonth(month):
    if 1 <= int(month) <= 12:
        return True
    else:
        return False

#Adds a 0 to the front of the day if there isn't already one there
def chday(day):
    if len(day) == 1:
        day = "0" + str(day)
        return day
    else:
        return day
        
#Adds a 0 to the front of the month if there isn't already one there
def chmonth(month):
    if len(str(month)) == 1:
        month = "0" + str(month)
        return month
    else:
        return month

main()
