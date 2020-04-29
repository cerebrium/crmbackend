import csv
import pandas as pd
import math

# always put stuff in functions... it scopes your variables and its cleaner.. making different functions do different things is modular and good code
def importData(schedule, drivers, driverManager,ScheduledDatesManager):

    # These two comments explain why you cant import scheduleddates.... the name is main. which is fine... but youll notice the package is null... which is not fine. and try as I might
    # I could not get the package name to change... hence my other solutions... which actually i think is better because it makes this process reproducable
    print('hello, my name is: ', __name__)
    print('and i live in package: ', __package__)

    # create array
    myArray = []

    # create variable for import
    data = pd.read_csv("sunday2.csv")

    # clean data -- good job, this is exactly what jupyter notebooks is for... youll need to do more of this kind of thing... for instances I removed the spaces from the 
    # csv file manually.... cant have spaces in names or will cause errors elsewhere
    data.dropna(subset=['ROUTE'], axis = 'rows', how ='all', inplace = True) 

    # loop through data and grab every row that belongs to the 'name' column in the data
    print(data)
    for row in data:
        print(str(data[row]))


#PARCEL, LWP, LVP, CRT, SUP, FUEL, SUPPORT, FDDS
        # print(schedule.objects.create_scheduledDate(row[2]))
        # print(drivers.objects.create_driver(row))
        # This line calls the function on the driver manager class that is attached to the driver class that makes a new driver
        # driver = drivers.objects.create_driver(row[0]),  # comment this after the data appears or it will multiply
        # this line just attaches a name to the array that is returned so the route looks pretty.
        # routeType = schedule.objects.create_scheduledDate(row[2])

    return myArray



   










