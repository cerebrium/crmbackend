import csv
#from django.contrib.auth.models import User
#from .models import Driver, ScheduledDate
import pandas as pd
#import matplotlib.pyplot as plt
#from .settings import import_export
#form import_export import resources


#load data in jyputer 

# #first laod the csv file in the project, then run
data = pd.read_csv("sunday2.csv")


# #here i am just dropping the rows in which Route = NaN, ie the driver has 
# #     not been on the road
data.dropna(subset=['ROUTE'],axis = 'rows', how ='all', inplace = True) 
print(data) #display the data 
for row in data:
    print(row)




# def run():
#     fhand = open('sunday2.csv')
#     reader = csv.reader(fhand)

    






#ScheduledDate.objects.all().delete()


 #   s, created = ScheduledDate.objects.get_or_create(name = row[0])


