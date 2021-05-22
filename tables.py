from venueclasses import *

currentAction=input('Create, Update, List, Delete,eXit venue => ')
if currentAction=='c':
    print('Create')
    newname=input('Name => ')
    numberofSeats=input('Number of Available Seats => ')
    numberofPeeps=input('Number Attending => ')
    theVenue= Venue("1", newname, "thatdate", numberofSeats, numberofPeeps)
    print(f'created : {theVenue.name}')
elif currentAction=='x':
    theVenue.save()
    
    exit

