def main():
    #make a list of the months as strings
    monthlist = ['January', 'February', 'March', 'April', 'May', \
                 'June', 'July', 'August', 'September', \
                 'October', 'November', 'December']
    date = input("Enter the date in the form(mm/dd/yyyy): ")

    date_split(date)
    monthnumber, datenumber, year = date_split(date)

    month = monthlist[monthnumber - 1]
    print(month,' ', datenumber, ",", year, sep= '')

def date_split(date):
    dateSplit = date.split("/")
    #dateSplit would be ['02','28','1997']
    monthnumber = int(dateSplit[0])
    datenumber = int(dateSplit[1])
    year = int(dateSplit[2])
    return monthnumber, datenumber, year

main()