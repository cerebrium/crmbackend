##### functions file #####
## make sure to import anything you plan to use
import datetime
import math
import pandas as pd
import numpy as np
import glob
from collections import defaultdict
from collections import Counter
import math
import csv
import collections, functools, operator

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
        # myTransientObjectDates['LWP'] = ele.LWP
        # myTransientObjectDates['LVP'] = ele.LVP
        # myTransientObjectDates['CRT'] = ele.CRT
        # myTransientObjectDates['RL'] = ele.RL
        # myTransientObjectDates['fuel'] = str(ele.fuel)
        myTransientObjectDates['support'] = str(ele.support)
        # myTransientObjectDates['vans'] = str(ele.vans)
        myTransientObjectDates['deductions'] = str(ele.deductions) # here
        # myTransientObjectDates['training'] = ele.CRT + ele.RL # and here

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

    

    # numOfRoutes = data['inOff'].value_counts()[1]  
    # # print('routes: ', numOfRoutes)

    # # this is how I would do this.... I am sure pandas has a way, but i dont know it
    # numOfMFNRoutesOne = data['route'].value_counts()
    
    # # set a counter variable
    # numOfMFNRoutes = 0

    # # set a loop variable
    # x = 0

    # # loop through each item in the data set you made
    # while x < len(numOfMFNRoutesOne):

    #     # display the information in the terminal
    #     print (
    #         'Route found: ', numOfMFNRoutesOne.index[x] , ' : ',  numOfMFNRoutesOne[numOfMFNRoutesOne.index[x]]
    #     )

    #     # make a conitional statment that if it finds what you are looking for it will increment the counter variable above
    #     if numOfMFNRoutesOne.index[x] == 'MFN':
    #         numOfMFNRoutes = numOfMFNRoutes + 1

    #     # increment the loop    
    #     x = x + 1

    # # numOfMFNRoutes = data['route'].value_counts()['MFN']
    # # print('mfn: ', numOfMFNRoutes)
    
    # numOfFUllRoutes = numOfRoutes - numOfMFNRoutes
    # # print('full: ', numOfFUllRoutes)


    # #count number of LVP and LWP respectively
    # # numOfLVP = int(data['LVP'].sum())
    # # numOfLWP = int(data['LWP'].sum())
    # numOfParcels = int(data['parcel'].sum())


    # #here I just print out the results
    # names = ['Routes: ',"FULL: ", 'MFN: ', 'LVP: ', 'LWP: ','Parcels: ']

    # #print(names)
    # values = [str(numOfRoutes),str(numOfFUllRoutes),str(numOfMFNRoutes),
    #       str(numOfLVP),str(numOfLWP),str(numOfParcels)]

    
    # #print(values)
    # myNum = len(values)

    # for i in names:
    #     n1 = names[0] + f" " + values[0] 
    #     n2 = names[1] + f" " + values[1]
    #     n3 = names[2] + f" " + values[2]
    #     n4 = names[3] + f" " + values[3]
    #     n5 = names[4] + f" " + values[4]
    #     n6 = names[5] + f" " + values[5]
    #     text = f"Statistics for today:"
    # print(text,n1,n2,n3,n4,n5,n6)
    # return [text,n1,n2,n3,n4,n5,n6]

def returnOrderdData(driversList, datesList, imagesList, vehicles, deductions, support):

    #### add an array of registrations for the vehicles that are owned by the company
    #### add array containing the status of the drivers

    myImagesArray = []
    myDriverArray = []
    myDatesArray = []
    myVehiclesArray = []
    myDeductionArray = []
    mySupportArray = []

    for ele in deductions:
        myTransientDeduction = {}
        myTransientDeduction['deduction_id'] = ele.deduction_id
        myTransientDeduction['date_id'] = str(ele.date_id)
        myTransientDeduction['name'] = ele.name
        myTransientDeduction['amount'] = str(ele.amount)

        myDeductionArray.append(myTransientDeduction)

    for ele in support:
        myTransientSupport = {}
        myTransientSupport['support_id'] = ele.support_id
        myTransientSupport['date_id'] = str(ele.date_id)
        myTransientSupport['name'] = ele.name
        myTransientSupport['amount'] = str(ele.amount)

        mySupportArray.append(myTransientSupport)

    for ele in imagesList:
        myTransientImage = {}
        myTransientImage['driver_id'] = str(ele.driver_id)
        myTransientImage['vehicle_id'] = str(ele.vehicle_id)
        myTransientImage['image_id'] = ele.image_id
        myTransientImage['name'] = ele.name
        myTransientImage['countryOfIssue'] = ele.countryOfIssue
        myTransientImage['expiryDate'] = ele.expiryDate
        myTransientImage['dueDate'] = ele.dueDate
        myTransientImage['datePassed'] = ele.datePassed
        myTransientImage['photo'] = ele.photo
        myTransientImage['managerApprovedName'] = ele.managerApprovedName
        myTransientImage['managerApprovedDate'] = ele.managerApprovedDate
        myTransientImage['imagesLink'] = ele.imagesLink
        myTransientImage['verified'] = ele.verified
        myTransientImage['driverSigned'] = ele.driverSigned
        myTransientImage['points'] = ele.points
        myTransientImage['nextDVLAScreenshot'] = ele.nextDVLAScreenshot
        

        myImagesArray.append(myTransientImage)

    for ele in vehicles:
        myTransientVehicle = {}
        myTransientVehicle['driver_id'] = str(ele.driver_id)
        myTransientVehicle['vehicle_id'] = ele.vehicle_id
        myTransientVehicle['registration'] = ele.registration
        myTransientVehicle['make'] = ele.make
        myTransientVehicle['model'] = ele.model
        myTransientVehicle['year'] = ele.year
        myTransientVehicle['companyOwned'] = ele.companyOwned
        myTransientVehicle['vtype'] = ele.vtype
        myTransientVehicle['quotePrice'] = str(ele.quotePrice)
        myTransientVehicle['invoice'] = str(ele.invoice)

        myVehiclesArray.append(myTransientVehicle)

        # images version
        imagesArray = []
        for imgObject in myImagesArray:
            if imgObject['vehicle_id'] == ele.registration:
                imagesArray.append(imgObject)

        myTransientVehicle['imgArray'] = imagesArray  

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
    
        myDeductionSum = 0
        mySupportSum = 0
        total = 0
        deductionList = []
        supportList = []

        for element in myDeductionArray: 
            if element['date_id'] == str(ele.date_id):
                myDeductionSum += float(element['amount'][3::])
                deductionList.append(element)
                
        myTransientObjectDates['deductionSum'] = 'GB£{}'.format(myDeductionSum) 
        myTransientObjectDates['deductionList'] = deductionList 

        for element in mySupportArray: 
            if element['date_id'] == str(ele.date_id):
                mySupportSum += float(element['amount'][3::])
                supportList.append(element)

        total = mySupportSum - myDeductionSum        

        myTransientObjectDates['supportSum'] ='GB£{}'.format(mySupportSum) 
        myTransientObjectDates['supportList'] = supportList 

        myTransientObjectDates['total'] = total

        myDatesArray.append(myTransientObjectDates)

    ## array for checking urls
    urlArray = []


    ## recreate the driver dataset
    for ele in driversList:
        myTransientObjectDriver = {}
        datesArray = []
        myTransientObjectDriver['driver_id'] = ele.driver_id
        myTransientObjectDriver['vehicle_name'] = ele.driver_id
        myTransientObjectDriver['name'] = ele.name
        myTransientObjectDriver['location'] = ele.location
        myTransientObjectDriver['email'] = ele.email
        myTransientObjectDriver['phone'] = ele.phone
        myTransientObjectDriver['address'] = ele.address
        myTransientObjectDriver['status'] = ele.status
        myTransientObjectDriver['DriverUniqueId'] = ele.DriverUniqueId
        myTransientObjectDriver['SigningUrlNumber'] = ele.SigningUrlNumber
        myTransientObjectDriver['Signed'] = ele.Signed
        myTransientObjectDriver['approvedBy'] = ele.approvedBy
        myTransientObjectDriver['approvedDateAndTime'] = ele.approvedDateAndTime
            
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
    }   
    

    return myFinalObject

def invoice(driversList, datesList, vehiclesList, deductions, support):

    #### add an array of registrations for the vehicles that are owned by the company
    #### add array containing the status of the drivers

    myImagesArray = []
    myDriverArray = []
    myDatesArray = []
    myVehiclesArray = []
    myDeductionArray = []
    mySupportArray = []

    for ele in deductions:
        myTransientDeduction = {}
        myTransientDeduction['deduction_id'] = ele.deduction_id
        myTransientDeduction['date_id'] = str(ele.date_id)
        myTransientDeduction['name'] = ele.name
        myTransientDeduction['amount'] = str(ele.amount)

        myDeductionArray.append(myTransientDeduction)

    for ele in support:
        myTransientSupport = {}
        myTransientSupport['support_id'] = ele.support_id
        myTransientSupport['date_id'] = str(ele.date_id)
        myTransientSupport['name'] = ele.name
        myTransientSupport['amount'] = str(ele.amount)

        mySupportArray.append(myTransientSupport)

    for ele in vehiclesList:
        myTransientVehicle = {}
        myTransientVehicle['driver_id'] = str(ele.driver_id)
        myTransientVehicle['vehicle_id'] = ele.vehicle_id
        myTransientVehicle['registration'] = ele.registration
        myTransientVehicle['make'] = ele.make
        myTransientVehicle['model'] = ele.model
        myTransientVehicle['year'] = ele.year
        myTransientVehicle['companyOwned'] = ele.companyOwned
        myTransientVehicle['vtype'] = ele.vtype
        myTransientVehicle['quotePrice'] = str(ele.quotePrice)
        myTransientVehicle['invoice'] = str(ele.invoice)

        myVehiclesArray.append(myTransientVehicle)

        # images version
        imagesArray = []
        for imgObject in myImagesArray:
            if imgObject['vehicle_id'] == ele.registration:
                print(imgObject)
                imagesArray.append(imgObject)

        myTransientVehicle['imgArray'] = imagesArray  

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
    
        myDeductionSum = 0
        mySupportSum = 0
        total = 0
        deductionList = []
        supportList = []

        for element in myDeductionArray: 
            if element['date_id'] == ele.date:
                myDeductionSum += float(element['amount'][3::])
                deductionList.append(element)

        myTransientObjectDates['deductionSum'] = 'GB£{}'.format(myDeductionSum) 
        myTransientObjectDates['deductionList'] = deductionList 

        for element in mySupportArray: 
            if element['date_id'] == ele.date:
                mySupportSum += float(element['amount'][3::])
                supportList.append(element)

        total = mySupportSum - myDeductionSum        

        myTransientObjectDates['supportSum'] ='GB£{}'.format(mySupportSum) 
        myTransientObjectDates['supportList'] = supportList 
        myTransientObjectDates['total'] = total


        myDatesArray.append(myTransientObjectDates)

    ## array for checking urls
    urlArray = []


    ## recreate the driver dataset
    for ele in driversList:
        myTransientObjectDriver = {}
        datesArray = []
        myTransientObjectDriver['driver_id'] = ele.driver_id
        myTransientObjectDriver['vehicle_name'] = ele.driver_id
        myTransientObjectDriver['name'] = ele.name
        myTransientObjectDriver['location'] = ele.location
        myTransientObjectDriver['email'] = ele.email
        myTransientObjectDriver['phone'] = ele.phone
        myTransientObjectDriver['address'] = ele.address
        myTransientObjectDriver['status'] = ele.status
        myTransientObjectDriver['DriverUniqueId'] = ele.DriverUniqueId
        myTransientObjectDriver['SigningUrlNumber'] = ele.SigningUrlNumber
        myTransientObjectDriver['Signed'] = ele.Signed
        myTransientObjectDriver['approvedBy'] = ele.approvedBy
        myTransientObjectDriver['approvedDateAndTime'] = ele.approvedDateAndTime
            
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
        
    # # create array to go onto the driver that will contain all the drivers dates
    payrollArray = []

    # # inside of the driver array loop write some logic that links each date to the driver and push the date into the driver date array
    myWeekArray = []
    for ele in myDriverArray:
        for date in ele["datesArray"]:
            isValidDate = 0
            
            # try:
            #     datetime.datetime.strptime(date['date'], '%a %d %B %Y').date()
            # except ValueError:
            #     isValidDate = 1

            try:
                datetime.datetime.strptime(date['date'], '%a %b %d %Y').date()
            except ValueError:
                isValidDate = 1

            # if isValidDate == 1:
            #     if weekBeforeSunday <= datetime.datetime.strptime(date['date'], '%a %d %B %Y').date() < mostRecentSunday:
            #         myWeekArray.append(date)  

            if isValidDate == 0:
                if weekBeforeSunday <= datetime.datetime.strptime(date['date'], '%a %b %d %Y').date() < mostRecentSunday:
                    myWeekArray.append(date)

            if isValidDate == 1:
                if weekBeforeSunday <= datetime.datetime.strptime(date['date'], '%Y-%m-%d').date() < mostRecentSunday:
                    myWeekArray.append(date)       


        ##################################   FINAL INVOICE CREATION SECTION ############################################################################                    
    df = pd.DataFrame(myWeekArray)     # this is a dataframe with all the dates in the week we want      
    myInvoiceObj = {}
    allDatesArray = []
    myNum = 0
    while myNum < len(df):
        localArray = []
        for element in df:
            # this line adds the data to the local array
            localArray.append(df[element][df[element].index[myNum]])
        myNum += 1        
        allDatesArray.append(localArray)
        localArray = [] 

# leaving out summing the time for a little while get the rest working then will do that one.... turns out that part is hard

# instead of looping through each item in allDatesArray... loop through each deduction in dateItem in allDatesArray.... these are all the deductions. take them and seperate them into the correct place and then return them as values

# loop through all the dates and find per driver how many of each route type there are

# make an object which has keys as names of route types, an dvalues as amount the driver makes per route
    myObj = {
        'Full Standard Van Route': 121.8,
        'Full Large Van Route': 141.8,
        'Transportation Route': 100,
        'MFN Route': 70,
        'Missort Route': 121.8,
        'Classroom Training': 75,
        'Ride Along': 75,
        'Sweeper': 121.8

    }

    for item, index in enumerate(allDatesArray[0]):
        print(item, ': ', index)


    
    for dateItem in allDatesArray:
        if dateItem[9] in myInvoiceObj:
         #   print(myInvoiceObj[dateItem[9]]['route'])

            # sums the routes
            myInvoiceObj[dateItem[9]]['route'] = myInvoiceObj[dateItem[9]]['route'] + float([myObj[dateItem[3]]][0])

            # sums the routes
            myInvoiceObj[dateItem[9]]['parcels'] = myInvoiceObj[dateItem[9]]['parcels'] + float(dateItem[14])

            # sums the routes
            myInvoiceObj[dateItem[9]]['mileage'] = myInvoiceObj[dateItem[9]]['mileage'] + float(dateItem[10])*0.17

            # sums the deduction
            myMoneyObj = float(myInvoiceObj[dateItem[9]]['deduction'][3::]) + float(dateItem[17][3::])
            myInvoiceObj[dateItem[9]]['deduction'] = 'GB£{}'.format(myMoneyObj) 

            # sums the support
            mySupportObj = float(myInvoiceObj[dateItem[9]]['support'][3::]) + float(dateItem[19][3::])
            myInvoiceObj[dateItem[9]]['support'] = 'GB£{}'.format(mySupportObj) 

            
        else:
            myInvoiceObj[dateItem[9]] = {
                    'route': myObj[dateItem[3]], 
                    'parcels': dateItem[14],
                    'mileage': (dateItem[10]*0.17),
                    'deduction': dateItem[17],
                    'support': dateItem[19] 
                }


           


    myFinalObject = {
        'myOneWeekArray': myInvoiceObj,
    }   

    

    return myFinalObject          


#Own vans

        # for row in df.itertuples(index=True, name='Pandas'):
        #     invoiceObject = {}
        #     if getattr(row, "name") == getattr(row, "name"):
        #         if weekBeforeSunday < (datetime.datetime.strptime(getattr(row, "date"), '%a %d %d %Y')).date() < mostRecentSunday:
        #             if len(myOneWeekArray) > 0:
        #                 for element in myOneWeekArray[0]:
        #                     if element == 'LVP':
        #                         myOneWeekArray[0][element] = myOneWeekArray[0][element] + getattr(row, "LVP")
        #                     if element == 'LWP':
        #                         myOneWeekArray[0][element] = myOneWeekArray[0][element] + getattr(row, "LWP")
        #                     if element == 'CRT':
        #                         myOneWeekArray[0][element] = myOneWeekArray[0][element] + getattr(row, "CRT")
        #                             #print(myOneWeekArray[0][element])
        #         else:
        #             invoiceObject['name'] = getattr(row, "name")
        #             invoiceObject['mileage'] = getattr(row, "mileage")
        #             invoiceObject['route'] = getattr(row, "route")
        #             invoiceObject['support'] = getattr(row, "support")
        #             invoiceObject['deductions'] = getattr(row, "deductions")
        #             invoiceObject['fuel'] = getattr(row, "fuel")
                    


        #             myOneWeekArray.append(invoiceObject)   


        # datesObjectArray = []
        # for dateObject in myDatesArray:
        #     if dateObject['driver_id'] == ele.name:
        #         datesObjectArray.append(dateObject)


        # for dateObject in myDatesArray:
        #     if dateObject['driver_id'] == ele.name:
        #         payrollArray.append(dateObject['date'])
        #         myTransientObjectDriver['datesList'] = payrollArray 
        # myTransientObjectDriver['payroll'] = datesObjectArray    
        # myDriverArray.append(myTransientObjectDriver)
        #print('This is myDriverArray:', myDriverArray)
        
        #fields we will need for invoice calulations
        # invoiceArray['day'] = (datetime.datetime.strptime(str(dateObject['date']), '%Y-%m-%d %H:%M:%S.%f')).weekday()

        # for dateObject in myDatesArray:
        #     if dateObject['driver_id'] == ele.name:
        #         invoiceObject = {}
        #         if dateObject['date']:

        #             # there are two string lengths for the dates the logic is different so this checks if the right string is found
        #             if len(dateObject['date']) > 11:
        #                 if weekBeforeSunday < (datetime.datetime.strptime(str(dateObject['date']), '%a %d %B %Y')).date() < mostRecentSunday:
        #                     if len(myOneWeekArray) > 0:
        #                         for element in myOneWeekArray[0]:
        #                             # loop that sums all of the scheduled dates that aren't the first one
        #                             if element == 'LVP':
        #                                 myOneWeekArray[0][element] = myOneWeekArray[0][element] + dateObject['LVP']
        #                             if element == 'LWP':
        #                                 myOneWeekArray[0][element] = myOneWeekArray[0][element] + dateObject['LWP']
        #                             if element == 'Support':
        #                                 myValue= float(myOneWeekArray[0][element][3::]) + float(dateObject['support'][3::])
        #                                 myOneWeekArray[0][element] = "GB%f" % myValue

        #                     else:    
        #                         # creation of the zero index of the myTwoWeeksArray.... also going to be the final invoice 
        #                         invoiceObject['Route type'] = dateObject['route']
        #                         invoiceObject['LWP'] = dateObject['LWP']
        #                         invoiceObject['LVP'] = dateObject['LVP']
        #                         invoiceObject['Support'] = dateObject['support']
        #                         invoiceObject['Deductions'] = dateObject['deductions']
        #                         invoiceObject['Fuel'] = dateObject['fuel']
        #                         myOneWeekArray.append(invoiceObject)


            #print(myOneWeekArray)    
            # tempVar = defaultdict(list)
            # payCheck = defaultdict(list)
            # tempRoute = defaultdict(list)
                

            # # for i in myOneWeekArray[0]:
            #     if d['name'] == d['name']:
                    


            #         payCheck['name'].append(d['mileage'])
            #         mileage = [{'name': k, 'mileage': v, 'count': sum(v)} for k, v in payCheck.items()] 

                


            #here we will get the total routes
            # for d in myOneWeekArray:
            #     tempRoute['name'].append(d['route'])
            #     routes = [{'name': k, 'route': v, 'count': len(v)} for k, v in tempRoute.items()] 


            #     # routes = [{'name': k, 'route': v, 'count': len(v)} for k, v in tempRoute.items()] 
            # totalRoutes = sum(item['count'] for item in routes)
        
            
        
            #sort the routes
    #         for d in myOneWeekArray:
    #             print(d['name'])
    #             if d['name'] == d['name']:
    #                 if d['route'] == 'BULK':
    #                     tempVar[d['name']].append(d['route'])
    #                 elif d['route'] == 'Transportation':
    #                     tempVar[d['name']].append(d['route'])
    #                 elif d['route'] == 'MFN':
    #                     tempVar[d['name']].append(d['route'])
    #                 else:
    #                     tempVar[d['name']].append(d['route'])
    # print


                #tempRoute[d['name']].append(d['route'])
                # for h in myOneWeekArray:
                #     myTempArray = []
                #     myTempArray.append([h['support']].append(h['support']))
                # tempRoute[d['name']].append(myTempArray)
                #print(d['route'])
                    # for item in d['route']:
                    #     if item == 'MFN':
                            
                        
                    #         #myMFN.append(item)
                    #         tempVar[d['name']].append(item)
                    #     elif item == 'BULK':
                    #         #myMFN.append(item)
                    #         tempVar[d['name']].append(item)  
                    #     elif item == 'Classroom Training':
                    #     #print(item)
                    #         tempVar[d['name']].append(item)
                    #     elif item == 'Ride Along':
                    #     #print(item)
                    #         tempVar[d['name']].append(item)
                    #     else:
                    #         tempVar[d['name']].append(item)    
 
    
    # print('my tempVar', tempVar)








