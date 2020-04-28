import csv
import pandas as pd

def importData(schedule, drivers, driverManager):
    print(__name__)
    print(__package__)

    # create array
    myArray = []


    # create variable for import
    data = pd.read_csv("sunday2.csv")

    # clean data -- good job, this is exactly what jupyter notebooks is for
    data.dropna(subset=['ROUTE'], axis = 'rows', how ='all', inplace = True) 

    # loop through data and write data to database
    for row in data['NAME']:
        driver = drivers.objects.create_driver(row)
        myArray.append(row)

    return(myArray)    






