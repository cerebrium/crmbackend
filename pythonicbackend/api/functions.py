##### functions file #####
## make sure to import anything you plan to use
import datetime
import math
import pandas as pd
import numpy as np
import math
import csv

## declare a function - this one is going to return an array containing the difference between log in and log out times
def timeDifference(logIn, logOut):
    date = datetime.date(1, 1, 1)  # null time value to compare our log in and log out times to

    dateTimeLogIn = datetime.datetime.strptime(str(logIn), '%H:%M:%S') # lots here... but combining null time and our elements log in time
    dateTimeLogOut = datetime.datetime.strptime(str(logOut), '%H:%M:%S')  # same but log out, and now we can actually subrat them

    differenceValue = dateTimeLogIn - dateTimeLogOut

    differenceValue = str(abs(differenceValue))  # if you look at the console it says 8:00:00.... which is fine, but comment this out then look what postman gives you
    myString = differenceValue.split()

    return myString


def statistics(datesList):
        #----- Below are the statistics we will need
    myDatesArray = []

    for ele in datesList:
        myTransientObjectDates = {}

        myTransientObjectDates['driver_id'] = str(ele.driver_id)
        myTransientObjectDates['date_id'] = ele.date_id
        myTransientObjectDates['name'] = ele.name
        myTransientObjectDates['inOff'] = ele.inOff
        myTransientObjectDates['route'] = ele.route
        myTransientObjectDates['logIn_time'] = ele.logIn_time
        myTransientObjectDates['logOut_time'] = ele.logOut_time
        myTransientObjectDates['timeDifference'] = timeDifference(ele.logIn_time, ele.logOut_time)
        myTransientObjectDates['location'] = ele.location
        myTransientObjectDates['date'] = ele.date
        myTransientObjectDates['parcel'] = ele.parcel
        myTransientObjectDates['LWP'] = ele.LWP
        myTransientObjectDates['LVP'] = ele.LVP
        myTransientObjectDates['CRT'] = ele.CRT
        myTransientObjectDates['RL'] = ele.RL
        myTransientObjectDates['SUP'] = str(ele.SUP)
        myTransientObjectDates['fuel'] = str(ele.fuel)
        myTransientObjectDates['support'] = str(ele.support)
        myTransientObjectDates['vans'] = str(ele.vans)
        myTransientObjectDates['deductions'] = str(ele.SUP + ele.fuel + ele.support + ele.vans) # here
        myTransientObjectDates['training'] = ele.CRT + ele.RL # and here

        myDatesArray.append(myTransientObjectDates)

    # data = pd.read_csv("monday.csv")
    df = pd.DataFrame(data=myDatesArray)
    data = df

    print(df)

    # csv file manually.... cant have spaces in names or will cause errors elsewhere
    data.dropna(subset=['route'], axis = 'rows', how ='all', inplace = True) 
    data.fillna(0,inplace = True)
    #print(data)

    #count the number of ALL routes
    #data['IN'] = data['IN'].astype(float)
    numOfRoutes = data['inOff'].value_counts()[1]   #pay attention to this  "['1']",  I am using it only for monday, 
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
    return [text,n1,n2,n3]


def returnOrderdData(driversList, datesList, imagesList):
    ############## this function just copies everything and puts it into one array that can be returned...  ###########
    print(__package__)

    myImagesArray = []
    myDriverArray = []
    myDatesArray = []

    for ele in imagesList:
        myTransientImage = {}

        myTransientImage['image_id'] = ele.image_id
        myTransientImage['ImagesLink'] = ele.ImagesLink
        myTransientImage['Verified'] = ele.Verified
        myTransientImage['ImageName'] = ele.ImageName
        myTransientImage['driver_id'] = str(ele.driver_id)
        myTransientImage['ManagerSigned'] = ele.ManagerSigned
        myTransientImage['DriverSigned'] = ele.DriverSigned
        myTransientImage['ExpiryDate'] = ele.ExpiryDate
        myTransientImage['SignitureToken'] = ele.SignitureToken
        myTransientImage['SignitureManagerEmail'] = ele.SignitureManagerEmail

        myImagesArray.append(myTransientImage)

    for ele in datesList:
        myTransientObjectDates = {}

        myTransientObjectDates['driver_id'] = str(ele.driver_id)
        myTransientObjectDates['date_id'] = ele.date_id
        myTransientObjectDates['name'] = ele.name
        myTransientObjectDates['inOff'] = ele.inOff
        myTransientObjectDates['route'] = ele.route
        myTransientObjectDates['logIn_time'] = ele.logIn_time
        myTransientObjectDates['logOut_time'] = ele.logOut_time
        myTransientObjectDates['timeDifference'] = timeDifference(ele.logIn_time, ele.logOut_time)
        myTransientObjectDates['location'] = ele.location
        myTransientObjectDates['date'] = ele.date
        myTransientObjectDates['parcel'] = ele.parcel
        myTransientObjectDates['LWP'] = ele.LWP
        myTransientObjectDates['LVP'] = ele.LVP
        myTransientObjectDates['CRT'] = ele.CRT
        myTransientObjectDates['RL'] = ele.RL
        myTransientObjectDates['SUP'] = str(ele.SUP)
        myTransientObjectDates['fuel'] = str(ele.fuel)
        myTransientObjectDates['support'] = str(ele.support)
        myTransientObjectDates['vans'] = str(ele.vans)
        myTransientObjectDates['deductions'] = str(ele.SUP + ele.fuel + ele.support + ele.vans) # here
        myTransientObjectDates['training'] = ele.CRT + ele.RL # and here
    
        myDatesArray.append(myTransientObjectDates)

    ## recreate the driver dataset
    for ele in driversList:
        myTransientObjectDriver = {}
        datesArray = []
        myTransientObjectDriver['driver_id'] = ele.driver_id
        myTransientObjectDriver['name'] = ele.name
        myTransientObjectDriver['location'] = ele.location

        ## iterate through each date in datesList
        if len(ele.datesList) > 0:
            for item in ele.datesList:
                datesArray.append(item)
            myTransientObjectDriver['datesList'] = datesArray
        else:
            myTransientObjectDriver['datesList'] = [] 

        ################################## important part to look at ..... here i am going to add a 'field' that is not being saved, but will be returned to the front end... very 
        #### useful because this is going to put all the matching appointments into an array attached to the driver object they belong to ... something ive been doing on the front end

        ### step one .... I have mapped all the date data into an array now... which I will be formatting from now on, dont want to touch the actual data class
        # # if it can be avoided.
        datesObjectArray = []
        for dateObject in myDatesArray:

            if dateObject['driver_id'] == ele.name:
                datesObjectArray.append(dateObject)

        myTransientObjectDriver['datesArray'] = datesObjectArray    

        # images version
        imagesArray = []
        for imgObject in myImagesArray:

            if imgObject['driver_id'] == ele.name:
                imagesArray.append(imgObject)

        myTransientObjectDriver['imgArray'] = imagesArray  

        ## append object to array
        myDriverArray.append(myTransientObjectDriver)   

    myFinalObject = {
        'drivers': myDriverArray,
        'dates': myDatesArray,
        'images': myImagesArray
    }   
    

    return myFinalObject
            