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
    while myNum < len(data):
        localArray = []
        for row in data:
            # this line adds the data to the local array
            localArray.append(data[row][data[row].index[myNum]])

            # this line adds the local array to the returned array
            myArray.append(localArray)    

            # this line uses array indexing to add each item to the date class
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



#get our csv data script, the "data" will repsresents sunday
#any other day will be in a file named after it, expect for saturday

# create variable for import
data = pd.read_csv("monday.csv")

    # csv file manually.... cant have spaces in names or will cause errors elsewhere
data.dropna(subset=['ROUTE'], axis = 'rows', how ='all', inplace = True) 
data.fillna(0,inplace = True)
#print(data)

#count the number of ALL routes
#data['IN'] = data['IN'].astype(float)
numOfRoutes = data['IN'].value_counts()[1]  
numOfMFNRoutes = data['ROUTE'].value_counts()['MFN']
numOfFUllRoutes = numOfRoutes - numOfMFNRoutes


#count number of LVP and LWP respectively
numOfLVP = int(data['LVP'].sum())
numOfLWP = int(data['LWP'].sum())
numOfParcels = int(data['PARCEL'].sum())


#here I just print out the results
names = ['Routes: ',"FULL: ", 'MFN: ', 'LVP: ', 'LWP: ','Parcels: ']
values = [str(numOfRoutes),str(numOfFUllRoutes),str(numOfMFNRoutes),
          str(numOfLVP),str(numOfLWP),str(numOfParcels)]
for i in names:
    n1 = names[0] + f" " + values[0] 
    n2 = names[1] + f" " + values[1]
    n3 = names[2] + f" " + values[2]
    n4 = names[3] + f" " + values[3]
    n5 = names[4] + f" " + values[4]
    n6 = names[5] + f" " + values[5]
    text = f"Statistics for today:"
    datStats = [text,n1,n2,n3,n4,n5,n6]
print("Monday Report:", datStats)
print(text,n1,n2,n3,n4,n5,n6)






# ##------------------------get some statistics for Saturday WEEK 18 --------------------------
# saturday = pd.read_csv("saturday.csv")
# saturday.dropna(subset=['ROUTE'], axis = 'rows', how ='all', inplace = True) 
# saturday.fillna(0,inplace = True)
# saturday.drop(["VANS ", "FDDS", "PHR","POD","CALL","CONS","DAILY DPMO ","week"],axis = 1,inplace = True, errors = 'ignore')
# #RUn just once, the follwoing 2 lines just create the week column in the csv file, we can change it do a specific date if you want
# #saturday["WEEK"] = "18"
# #saturday.to_csv("saturday.csv", index=False)
# #saturday.head(15)
# numOfRoutes_sat = saturday['IN'].value_counts()[1] 
# numOfLVP_sat = int(saturday['LVP'].sum())
# numOfLWP_sat = int(saturday['LWP'].sum())
# numOfParcels_sat = int(saturday['PARCEL'].sum())



# names = ['Routes: ', 'LVP: ', 'LWP: ','Parcels: ']
# #print(names)
# values = [str(numOfRoutes_sat), str(numOfLWP_sat),str(numOfLVP_sat),str(numOfParcels_sat)]
# #print(values)
# #nl = '\n'
# myNum = len(values)

# for i in names:
#     n1 = names[0] + f" " + values[0] 
#     n2 = names[1] + f" " + values[1]
#     n3 = names[2] + f" " + values[2]
#     n4 = names[3] + f" " + values[3]
#     text = f"Statistics for today:"
# #print(text,n1,n2,n3,n4)
# satStats = [text,n1,n2,n3,n4]
# print("Saturday Report:", satStats)


###------------------------------ end ------------------------------