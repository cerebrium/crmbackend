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
        print('log In: ', element.logIn_time)  # for working on things I always do lots of comments to see what im looking at as I go!
        print('log Out: ', element.logOut_time) 

        ## dateTime objects cannot be subtracted in python..... booooooo!!!! they can in javascript! :) ... anyways no big deal lets turn them into things that can be subrtracted
        ### apparently the way to do this is turn them into datetime.datetime objects, and combine them with a null value to get the delta that can be compared... silly!
        date = datetime.date(1, 1, 1)  # null time value to compare our log in and log out times to

        dateTimeLogIn = datetime.datetime.combine(date, element.logIn_time)  # lots here... but combining null time and our elements log in time
        dateTimeLogOut = datetime.datetime.combine(date, element.logOut_time)  # same but log out, and now we can actually subrat them

        ## for each item in the object do the following computation and save it in a variable calledd differenceValue... reassigned for each iteration of the loop
        differenceValue = dateTimeLogIn - dateTimeLogOut

        print(differenceValue)
        ### so I looked at the output and it was 28800..... wtf is that.... welll, the difference value here is 8, and 8 times 3600 is 28800 . awesome, thanks python. so we have to convert this 
        ## number into something not silly
        differenceValue = differenceValue/3600

        ## now the result is in hours.. with decimal places for minutes... <3

        ## now that we have the value we want to return, let push each value into the array we will return to be put into the object for the front end
        myReturnArray.append(differenceValue)

    ## make sure to return a value so that when the function is called the array is the actual value that is given back
    return myReturnArray    
    
