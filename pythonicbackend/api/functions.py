##### functions file #####
## make sure to import anything you plan to use
import datetime

## declare a function - this one is going to return an array containing the difference between log in and log out times
def timeDifference(scheduledDates):
    # takes one argument which is going to be the entirety of the class containing the scheduled work dates... which has access to all fields on each item

    ## here i am declaring an empty array, I amgoing to do my computation in a loop and push each final number into this array to be returned later
    myReturnArray = []

    ## since the 'scheduledDates' passed in is all of the dates.... i can loop through them and call each field i want to use
    for element in scheduledDates:
        ## now element is an object ... or an instance... of the scheduled dates class that is accesibel to call fields on
        # print('log In: ', element.logIn_time)  # for working on things I always do lots of comments to see what im looking at as I go!
        # print('log Out: ', element.logOut_time) 

        ## dateTime objects cannot be subtracted in python..... booooooo!!!! they can in javascript! :) ... anyways no big deal lets turn them into things that can be subrtracted
        ### apparently the way to do this is turn them into datetime.datetime objects, and combine them with a null value to get the delta that can be compared... silly!
        date = datetime.date(1, 1, 1)  # null time value to compare our log in and log out times to

        dateTimeLogIn = datetime.datetime.combine(date, element.logIn_time)  # lots here... but combining null time and our elements log in time
        dateTimeLogOut = datetime.datetime.combine(date, element.logOut_time)  # same but log out, and now we can actually subrat them

        ## for each item in the object do the following computation and save it in a variable calledd differenceValue... reassigned for each iteration of the loop
        differenceValue = dateTimeLogIn - dateTimeLogOut

        # print(differenceValue)
        ### so I looked at the output and it was 28800..... wtf is that.... welll, the difference value here is 8, and 8 times 3600 is 28800 . awesome, thanks python. so we have to convert this 
        ## number into something not silly
        differenceValue = differenceValue/3600   # if you look at the console it says 8:00:00.... which is fine, but comment this out then look what postman gives you

        ## now the result is in hours.. with decimal places for minutes... <3

        ## now that we have the value we want to return, let push each value into the array we will return to be put into the object for the front end
        myReturnArray.append(differenceValue)

    ## make sure to return a value so that when the function is called the array is the actual value that is given back
    return myReturnArray    


def returnOrderdData(driversList, datesList):
    myDriverArray = []
    myDatesArray = []
    
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

        ## iterate through each date in datesList
        if len(ele.datesList) > 0:
            for item in ele.datesList:
                datesArray.append(item)
            myTransientObjectDriver['datesList'] = datesArray
        else:
            myTransientObjectDriver['datesList'] = [] 

        ## append object to array
        myDriverArray.append(myTransientObjectDriver)   

    for ele in datesList:
        myTransientObjectDates = {}
        print(ele.driver_id)
        myTransientObjectDates['date_id'] = ele.date_id
        myTransientObjectDates['name'] = ele.name
        myTransientObjectDates['inOff'] = ele.inOff
        myTransientObjectDates['route'] = ele.route
        myTransientObjectDates['logIn_time'] = ele.logIn_time
        myTransientObjectDates['logOut_time'] = ele.logOut_time
        myTransientObjectDates['timeDifference'] = ele.timeDifference
        myTransientObjectDates['location'] = ele.location
        myTransientObjectDates['date'] = ele.date
        myTransientObjectDates['driver_id'] = str(ele.driver_id)
        myTransientObjectDates['parcel'] = ele.parcel
        myTransientObjectDates['LWP'] = ele.LWP
        myTransientObjectDates['LVP'] = ele.LVP
        myTransientObjectDates['CRT'] = ele.CRT
        myTransientObjectDates['RL'] = ele.RL
        myTransientObjectDates['SUP'] = str(ele.SUP)
        myTransientObjectDates['fuel'] = str(ele.fuel)
        myTransientObjectDates['supportDeductions'] = str(ele.supportDeductions)
        myTransientObjectDates['vans'] = str(ele.vans)
        
        myDatesArray.append(myTransientObjectDates)

    myFinalObject = {
        'drivers': myDriverArray,
        'dates': myDatesArray
    }   
    

    return myFinalObject
            