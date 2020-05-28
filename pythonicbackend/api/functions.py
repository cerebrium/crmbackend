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
        myTransientObjectDates['fuel'] = str(ele.fuel)
        myTransientObjectDates['support'] = str(ele.support)
        myTransientObjectDates['vans'] = str(ele.vans)
        myTransientObjectDates['deductions'] = str(ele.fuel + ele.support + ele.vans) # here
        myTransientObjectDates['training'] = ele.CRT + ele.RL # and here

        myDatesArray.append(myTransientObjectDates)




    # get data
    df = pd.DataFrame(data=myDatesArray)    #turns the current data in the backend into panda dataframe 
    data = df
    # print('dataframe: ', data)

    # csv file manually.... cant have spaces in names or will cause errors elsewhere
    data.dropna(subset=['route'], axis = 'rows', how ='all', inplace = True) 
    data.fillna(0,inplace = True)
    #add week column
    #data["week"] = "18"
    #data.to_csv("data.csv", index=False)
    #print(data)

    #count the number of ALL routes
    #data['IN'] = data['IN'].astype(float)
    # numOfRoutes = data['inOff'].value_counts()[1]
    # #count number of LVP and LWP respectively
    # numOfLVP = int(data['LVP'].sum())
    # numOfLWP = int(data['LWP'].sum())
    # numOfParcels = int(data['parcel'].sum())


    # #here I just print out the results
    # names = ['Routes: ', 'LVP: ', 'LWP: ', 'Parcels:']

    

    numOfRoutes = data['inOff'].value_counts()[1]  
    # print('routes: ', numOfRoutes)

    # this is how I would do this.... I am sure pandas has a way, but i dont know it
    numOfMFNRoutesOne = data['route'].value_counts()
    
    # set a counter variable
    numOfMFNRoutes = 0

    # set a loop variable
    x = 0

    # loop through each item in the data set you made
    while x < len(numOfMFNRoutesOne):

        # display the information in the terminal
        print (
            'Route found: ', numOfMFNRoutesOne.index[x] , ' : ',  numOfMFNRoutesOne[numOfMFNRoutesOne.index[x]]
        )

        # make a conitional statment that if it finds what you are looking for it will increment the counter variable above
        if numOfMFNRoutesOne.index[x] == 'MFN':
            numOfMFNRoutes = numOfMFNRoutes + 1

        # increment the loop    
        x = x + 1

    # numOfMFNRoutes = data['route'].value_counts()['MFN']
    # print('mfn: ', numOfMFNRoutes)
    
    numOfFUllRoutes = numOfRoutes - numOfMFNRoutes
    # print('full: ', numOfFUllRoutes)


    #count number of LVP and LWP respectively
    numOfLVP = int(data['LVP'].sum())
    numOfLWP = int(data['LWP'].sum())
    numOfParcels = int(data['parcel'].sum())


    #here I just print out the results
    names = ['Routes: ',"FULL: ", 'MFN: ', 'LVP: ', 'LWP: ','Parcels: ']

    #print(names)
    values = [str(numOfRoutes),str(numOfFUllRoutes),str(numOfMFNRoutes),
          str(numOfLVP),str(numOfLWP),str(numOfParcels)]

    
    #print(values)
    myNum = len(values)

    for i in names:
        n1 = names[0] + f" " + values[0] 
        n2 = names[1] + f" " + values[1]
        n3 = names[2] + f" " + values[2]
        n4 = names[3] + f" " + values[3]
        n5 = names[4] + f" " + values[4]
        n6 = names[5] + f" " + values[5]
        text = f"Statistics for today:"
    print(text,n1,n2,n3,n4,n5,n6)
    return [text,n1,n2,n3,n4,n5,n6]


def returnOrderdData(driversList, datesList, imagesList, vehicles):
    ############## this function just copies everything and puts it into one array that can be returned...  ###########
    print(__package__)

    #### add an array of registrations for the vehicles that are owned by the company
    #### add array containing the status of the drivers

    myImagesArray = []
    myDriverArray = []
    myDatesArray = []
    myVehiclesArray = []

    for ele in vehicles:
        myTransientVehicle = {}
        myTransientImage['Vehicle_id'] = ele.Vehicle_id
        myTransientImage['VehiclesRegistration'] = ele.VehiclesRegistration
        myTransientImage['VehiclesDVLANumber'] = ele.VehiclesDVLANumber
        myTransientImage['VehicleOwned'] = ele.VehicleOwned
        myTransientImage['driver_id'] = str(ele.driver_id)

        myVehiclesArray.append(myTransientVehicle)

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

        myTransientObjectDates['date_id'] = ele.date_id
        myTransientObjectDates['name'] = ele.name
        myTransientObjectDates['inOff'] = ele.inOff
        myTransientObjectDates['route'] = ele.route
        myTransientObjectDates['routeNumber'] = ele.routeNumber
        myTransientObjectDates['logOut_time'] = ele.logOut_time
        myTransientObjectDates['logIn_time'] = ele.logIn_time
        myTransientObjectDates['location'] = ele.location
        myTransientObjectDates['date'] = ele.date
        myTransientObjectDates['driver_id'] = str(ele.driver_id)
        myTransientObjectDates['mileage'] = ele.mileage
        myTransientObjectDates['start_mileage'] = ele.start_mileage
        myTransientObjectDates['finish_mileage'] = ele.finish_mileage
        myTransientObjectDates['timeDifference'] = timeDifference(ele.logIn_time, ele.logOut_time)
        myTransientObjectDates['parcel'] = ele.parcel
        myTransientObjectDates['parcelNotDelivered'] = ele.parcelNotDelivered
        myTransientObjectDates['TORH'] = ele.TORH
        myTransientObjectDates['LateWavePayment'] = ele.LateWavePayment
        myTransientObjectDates['LVP'] = ele.LVP
        myTransientObjectDates['CRT'] = ele.CRT
        myTransientObjectDates['RL'] = ele.RL
        myTransientObjectDates['FDDS'] = ele.FDDS
        myTransientObjectDates['PHR'] = ele.PHR
        myTransientObjectDates['CALL'] = ele.CALL
        myTransientObjectDates['POD'] = ele.POD
        myTransientObjectDates['CONS'] = ele.CONS
        myTransientObjectDates['DPMO'] = ele.DPMO
        myTransientObjectDates['support'] = str(ele.support)
        myTransientObjectDates['fuel'] = str(ele.fuel)
        myTransientObjectDates['vans'] = str(ele.vans)
        myTransientObjectDates['deductions'] = str(ele.fuel + ele.support + ele.vans) # here
    
        myDatesArray.append(myTransientObjectDates)

    ## array for checking urls
    urlArray = []


    ## recreate the driver dataset
    for ele in driversList:
        myTransientObjectDriver = {}
        datesArray = []
        myTransientObjectDriver['driver_id'] = ele.driver_id
        myTransientObjectDriver['name'] = ele.name
        myTransientObjectDriver['location'] = ele.location
        myTransientObjectDriver['email'] = ele.email
        myTransientObjectDriver['phone'] = ele.phone
        myTransientObjectDriver['address'] = ele.address
        myTransientObjectDriver['status'] = ele.status
        myTransientObjectDriver['DriverUniqueId'] = ele.DriverUniqueId
        myTransientObjectDriver['SigningUrlNumber'] = ele.SigningUrlNumber
        myTransientObjectDriver['Signed'] = ele.Signed

        ## iterate through numbers
        if ele.SigningUrlNumber:
            if ele.Signed:
                urlArray.append(ele.SigningUrlNumber)

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

        # vehicles version
        vehiclesArray = []
        for vehicleObject in myVehiclesArray:
            if vehicleObject['driver_id'] == ele.name:
                vehiclesArray.append(vehicleObject)

        myTransientObjectDriver['vehicleArray'] = vehiclesArray  

        ## append object to array
        myDriverArray.append(myTransientObjectDriver)   

    myFinalObject = {
        'drivers': myDriverArray,
        'dates': myDatesArray,
        'images': myImagesArray,
        'vehicles': myVehiclesArray,
        'urls': urlArray
    }   
    

    return myFinalObject




def invoice(driversList, datesList, vehiclesList):
    # find out today
    currentDate = datetime.date.today()
    dateWeekDay = currentDate.weekday()
    mostRecentSunday = 0
    weekBeforeSunday = 0
    twoWeeksBeforeSunday = 0
    fourWeeksBeforeSunday = 0
    dateWeekDay+=1
    if currentDate.weekday() > 0:
        if currentDate.weekday() == 6:
            print(currentDate)    
        else:
            mostRecentSunday = currentDate - datetime.timedelta(days=dateWeekDay)
            weekBeforeSunday = mostRecentSunday - datetime.timedelta(days=7)
            twoWeeksBeforeSunday = mostRecentSunday - datetime.timedelta(days=14)
            fourWeeksBeforeSunday = mostRecentSunday - datetime.timedelta(days=28)
            print('last week was from: ', weekBeforeSunday, ' until: ', mostRecentSunday, ' last two weeks were: ', twoWeeksBeforeSunday, ' until ', mostRecentSunday)
    print(' what is the sunday two weeks ago', twoWeeksBeforeSunday)
            

    # create an array for drivers
    myDriverArray = []
    
    # create an array for dates
    myDatesArray = []

    # create an array for vehicles
    myVehiclesArray = []

    # loop through each item in vehicles and put each field into the new array of objects
    for ele in vehiclesList:
        myTransientVehicle = {}
        myTransientVehicle['Vehicle_id'] = ele.Vehicle_id
        myTransientVehicle['VehiclesRegistration'] = ele.VehiclesRegistration
        myTransientVehicle['VehiclesDVLANumber'] = ele.VehiclesDVLANumber
        myTransientVehicle['VehicleOwned'] = ele.VehicleOwned
        myTransientVehicle['driver_id'] = str(ele.driver_id)

        myVehiclesArray.append(myTransientVehicle)

    # loop through each item in dates and put each field into the new array of objects
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
        myTransientObjectDates['LateWavePayment'] = ele.LateWavePayment
        myTransientObjectDates['LVP'] = ele.LVP
        myTransientObjectDates['CRT'] = ele.CRT
        myTransientObjectDates['RL'] = ele.RL
        myTransientObjectDates['fuel'] = str(ele.fuel)
        myTransientObjectDates['support'] = str(ele.support)
        myTransientObjectDates['vans'] = str(ele.vans)
        myTransientObjectDates['deductions'] = str(ele.fuel + ele.support + ele.vans) # here
        myTransientObjectDates['training'] = ele.CRT + ele.RL # and here
    
        myDatesArray.append(myTransientObjectDates)

    # loop through each item in drivers and put each field into the new array of objects

    for id, ele in enumerate(driversList):
        # create an array to store the dates inside the time period we want to analyse
        myTwoWeekArray = []

        myTransientObjectDriver = {}
        myTransientObjectDriver['driver_id'] = ele.driver_id
        myTransientObjectDriver['name'] = ele.name
        myTransientObjectDriver['location'] = ele.location
        myTransientObjectDriver['email'] = ele.email
        myTransientObjectDriver['phone'] = ele.phone
        myTransientObjectDriver['address'] = ele.address
        myTransientObjectDriver['status'] = ele.status
        myTransientObjectDriver['DriverUniqueId'] = ele.DriverUniqueId
        myTransientObjectDriver['SigningUrlNumber'] = ele.SigningUrlNumber
        myTransientObjectDriver['Signed'] = ele.Signed
        
        # # create array to go onto the driver that will contain all the drivers dates
        payrollArray = []

        # # inside of the driver array loop write some logic that links each date to the driver and push the date into the driver date array

        datesObjectArray = []
        for dateObject in myDatesArray:
            if dateObject['driver_id'] == ele.name:
                datesObjectArray.append(dateObject)


        for dateObject in myDatesArray:
            if dateObject['driver_id'] == ele.name:
                payrollArray.append(dateObject['date'])
                myTransientObjectDriver['datesList'] = payrollArray 
        myTransientObjectDriver['payroll'] = datesObjectArray    
        myDriverArray.append(myTransientObjectDriver)
### --- 


#Own vans
        
        #fields we will need for invoice calulations
        # invoiceArray['day'] = (datetime.datetime.strptime(str(dateObject['date']), '%Y-%m-%d %H:%M:%S.%f')).weekday()

        for dateObject in myDatesArray:
            print('hello i am a date object', dateObject)
            if dateObject['driver_id'] == ele.name:
                invoiceObject = {}
                if dateObject['date']:

                    # there are two string lengths for the dates the logic is different so this checks if the right string is found
                    if len(dateObject['date']) > 11:
                        if weekBeforeSunday < (datetime.datetime.strptime(str(dateObject['date']), '%a %b %d %Y')).date() < mostRecentSunday:
                            if len(myTwoWeekArray) > 0:
                                for element in myTwoWeekArray[0]:
                                    # loop that sums all of the scheduled dates that aren't the first one
                                    if element == 'LVP':
                                        myTwoWeekArray[0][element] = myTwoWeekArray[0][element] + dateObject['LVP']
                                    if element == 'LWP':
                                        myTwoWeekArray[0][element] = myTwoWeekArray[0][element] + dateObject['LWP']
                                    if element == 'Support':
                                        print(float(myTwoWeekArray[0][element][3::]))
                                        myValue= float(myTwoWeekArray[0][element][3::]) + float(dateObject['support'][3::])
                                        myTwoWeekArray[0][element] = "GB£%f" % myValue
                                        print(myTwoWeekArray[0][element])

                            else:    
                                # creation of the zero index of the myTwoWeeksArray.... also going to be the final invoice 
                                invoiceObject['Route type'] = dateObject['route']
                                invoiceObject['LWP'] = dateObject['LWP']
                                invoiceObject['LVP'] = dateObject['LVP']
                                invoiceObject['Support'] = dateObject['support']
                                invoiceObject['Deductions'] = dateObject['deductions']
                                invoiceObject['Fuel'] = dateObject['fuel']
                                myTwoWeekArray.append(invoiceObject)
                                
        print('driver ', ele.name, ' has this in their array: ', myTwoWeekArray)  

#datetime.datetime(2020, 5, 12, 19, 38, 30, 397221)

    myFinalObject = {
        'drivers': myDriverArray,
        'dates': myDatesArray,
        'vehicles': myVehiclesArray
    }   
    

    return myFinalObject          











