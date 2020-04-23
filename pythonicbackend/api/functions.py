##### functions file #####
## make sure to import anything you plan to use
import datetime
import math

## declare a function - this one is going to return an array containing the difference between log in and log out times
def timeDifference(logIn, logOut):
    date = datetime.date(1, 1, 1)  # null time value to compare our log in and log out times to

    dateTimeLogIn = datetime.datetime.strptime(str(logIn), '%H:%M:%S') # lots here... but combining null time and our elements log in time
    dateTimeLogOut = datetime.datetime.strptime(str(logOut), '%H:%M:%S')  # same but log out, and now we can actually subrat them

    differenceValue = dateTimeLogIn - dateTimeLogOut

    differenceValue = str(abs(differenceValue))  # if you look at the console it says 8:00:00.... which is fine, but comment this out then look what postman gives you
    myString = differenceValue.split()

    return myString


def returnOrderdData(driversList, datesList):
    ############## this function just copies everything and puts it into one array that can be returned...  ###########

    # Ginishka ----
    # so cool!! LVP and LWP are different thought, we won't add them
    #LWP means late wave payment and if there is "1" that menas we pay the driver 10 extra pounds

    # LVP means large van payment  "1" that means we pay the driver i think 16 extra pounds
    #for the invoice we will need to sum all the extra reposrt stuff and substract deductions, we have
    #time for that though :*

    # --- end

    # here we want to return the sum of the dedcution fields in shceduleDates
    #     #  that sum will be deducted from the driver payment

    #  Here we want to check the number of day a driver has been on training
        #  CRT and RL needs to be 4 for every driver
        # Every driver needs to comlete the trainings before starting to work
        # CRT (classroom) and RL (on the road) training needs to be 4  (2 of each)
        # if the driver has been on RL the managers rights '1' that means he has completed one ride along training for the day
        # same for CRT
        # maybe we can usethis someweher else later, to keep track of the drivers info
    myDriverArray = []
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
        myTransientObjectDates['supportDeductions'] = str(ele.supportDeductions)
        myTransientObjectDates['vans'] = str(ele.vans)
        myTransientObjectDates['deductions'] = str(ele.SUP + ele.fuel + ele.supportDeductions + ele.vans) # here
        myTransientObjectDates['training'] = ele.CRT + ele.RL # and here
    
        myDatesArray.append(myTransientObjectDates)

    ## recreate the driver dataset
    for ele in driversList:
        myTransientObjectDriver = {}
        documentArray = []
        datesArray = []
        myTransientObjectDriver['driver_id'] = ele.driver_id
        myTransientObjectDriver['name'] = ele.name
        myTransientObjectDriver['location'] = ele.location

        ## iterate through each document in documents
        if len(ele.documents) > 0:
            for item in ele.documents:
                documentArray.append(item)
            myTransientObjectDriver['documents'] = documentArray
        else:
            myTransientObjectDriver['documents'] = [] 

        ## iterate through each document in vehicle documents
        if len(ele.vehicleDocuments) > 0:
            for item in ele.vehicleDocuments:
                documentArray.append(item)
            myTransientObjectDriver['vehicleDocuments'] = documentArray
        else:
            myTransientObjectDriver['vehicleDocuments'] = [] 

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
            ## see, now we can actually access everything as objects not stupid psql untouchable data fields
            ## i . e if this was:
            # for dateObject in datesList:
            #   print(dateObject)  --> this would throw an error ...
            
            # print(dateObject['driver_id']) 

            ## so what I want is that if the scheduled dates objects foreign key matches the driver... i want to add it into an array I am going to 
            # create on teh drivers object:
            if dateObject['driver_id'] == ele.name:
                datesObjectArray.append(dateObject)

            ## all the data is in the array now ... cool ... now lets add the array to the object visible on the front end    

        ## im making up the name dates array, it is not a field on the driver class.... but the object returned here it will look like it is with all the scheduled dates added in! :D
        myTransientObjectDriver['datesArray'] = datesObjectArray    

        ## append object to array
        myDriverArray.append(myTransientObjectDriver)   

    myFinalObject = {
        'drivers': myDriverArray,
        'dates': myDatesArray
    }   
    

    return myFinalObject
            