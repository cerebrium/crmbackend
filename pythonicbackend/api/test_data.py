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
        localArray = []    
        myNum = myNum + 1
    
    return myArray


#below os the code that works for Monday
#you first have to run 

    # create variable for import
data = pd.read_csv("monday.csv")

    # csv file manually.... cant have spaces in names or will cause errors elsewhere
data.dropna(subset=['ROUTE'], axis = 'rows', how ='all', inplace = True) 
data.fillna(0,inplace = True)
#print(data)





#----- Below are the statistics we will need



#count the number of ALL routes
#data['IN'] = data['IN'].astype(float)
numOfRoutes = data['IN'].value_counts()['1']   #pay attention to this  "['1']",  I am using it only for monday, 
#for the other days of the week i just use [1] have on clue way but it works, i will figure it out 

#count number of LVP and LWP respectively
numOfLVP = int(data['LVP'].sum())
numOfLWP = int(data['LWP'].sum())


#here I just print out the results
names = ['Routes: ', 'LVP: ', 'LWP: ']
#print(names)
values = [str(numOfRoutes), str(numOfLWP),str(numOfLVP)]
#print(values)
nl = '\n'
myNum = len(values)

for i in names:
    n1 = names[0] + f" " + values[0] + f"{nl}"
    n2 = names[1] + f" " + values[1]+ f"{nl}"
    n3 = names[2] + f" " + values[2]+ f"{nl}"
    text = f"Statistics for t2oday:{nl}{nl}"
print(text,n1,n2,n3)
















#----below is will just keep some commands i have used don't need it if you are not
#using jyouter maybe

#data.shape
#data.columns
#data.head(25)


   










