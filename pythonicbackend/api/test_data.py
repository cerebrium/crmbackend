import csv
import pandas as pd
import numpy as np
import math

# always put stuff in functions... it scopes your variables and its cleaner.. making different functions do different things is modular and good code
def importData(schedule, drivers, driverManager, ScheduledDatesManager):

    # create array
    myArray = []

    # create variable for import
    data = pd.read_csv("sunday2.csv")

    # clean data -- good job, this is exactly what jupyter notebooks is for... youll need to do more of this kind of thing... for instances I removed the spaces from the 
    # csv file manually.... cant have spaces in names or will cause errors elsewhere
    data.dropna(subset=['ROUTE'], axis = 'rows', how ='all', inplace = True) 
    data.fillna(0,inplace = True)

    # driver = drivers.objects.create_driver(row[0]) -- example :)
    # loop through data and grab every row that belongs to the 'name' column in the data

    print(data)
    for row in data['NAME']:
        driver = drivers.objects.create_driver(row)

    myNum = 0
    while myNum < 13:
        localArray = []
<<<<<<< HEAD
        for row in data:
            localArray.append(data[row][data[row].index[myNum]])
            myArray.append(localArray)
        scheduledDate = schedule.objects.create_date(
            localArray[0], 
            localArray[1], 
            localArray[2], 
            localArray[3], 
            localArray[4], 
            localArray[5], 
            localArray[6], 
            localArray[7], 
            localArray[8], 
            localArray[9], 
            localArray[10], 
            localArray[11], 
            18.00, 
            localArray[13], 
            localArray[14], 
            localArray[15], 
            localArray[16][0:5] if len(str(localArray[16])) > 1 else 0, 
            localArray[17], 
            localArray[18][0:5] if len(str(localArray[18])) > 1 else 0, 
            localArray[19][0:5] if len(str(localArray[19])) > 1 else 0, 
            localArray[20], 
            myNum+1)
=======
        for num, row in enumerate(data):
            localArray.append(data[row][data[row].index[myNum]])
            myArray.append(localArray)
        scheduledDate = schedule.objects.create_date(localArray[0], localArray[1], localArray[2], localArray[3], localArray[4], localArray[5], localArray[6], localArray[7], localArray[8], localArray[9], localArray[10], localArray[11], 18.00, localArray[13], localArray[14], localArray[15], localArray[16][0:5] if len(str(localArray[16])) > 1 else 0, localArray[17], localArray[18][0:5] if len(str(localArray[18])) > 1 else 0, localArray[19][0:5] if len(str(localArray[19])) > 1 else 0, localArray[20], myNum+1)
>>>>>>> 4dec93fb8779d9fcb65aeac9e66a27ebca794973
        localArray = []    
        myNum = myNum + 1

         
    return myArray



   










