"""
Lists
EventName = [] #List of Strings
EventDateYear = [] #List of Integer
EventDateMonth = [] #List of Integer
EventDateDay = [] #List of Integer
EventStartTime = [] #List of Integer
EventEndTime = [] #List of Integer
EventVenue = [] #List of String
EventDescription = [] #List of String
#Attendee Lists Below
NumberAttendee = [] #Number of Attendees of Indexed Event, List of Integer
AttendeeID = [] #List of Integer
AttendeeName = [] #List of String
AttendeeDetails = [] #List of String
EventID = [] #ID of Attendees of Indexed Event, List of String

Global variables
NumberEvent = 0
AttendeeCounter = 0
"""

#Change List of String to List of Integer
def FormatToInteger(Parameter):
    ListReturn = []
    for Counter in range(len(Parameter)):
        ListReturn.append(int(Parameter[Counter]))
    return ListReturn

#Change List of Integer to List of String
def FormatToString(Parameter):
    ListReturn = []
    for Counter in range(len(Parameter)):
        ListReturn.append(str(Parameter[Counter]))
    return ListReturn

#Read "Events_Information.txt" to get previous information
Separator = "-"
File = open("Events_Information.txt","r")
Line1 = File.readline().strip("\n")
if Line1 != "":
    EventName = Line1.split(Separator) #Line 1
else:
    EventName = []
EventDateYear = FormatToInteger(File.readline().split()) #Line 2
EventDateMonth = FormatToInteger(File.readline().split()) #Line 3
EventDateDay = FormatToInteger(File.readline().split()) #Line 4
EventStartTime = FormatToInteger(File.readline().split()) #Line 5
EventEndTime = FormatToInteger(File.readline().split()) #Line 6
Line7 = File.readline().strip("\n")
if Line7 != "":
    EventVenue = Line7.split(Separator) #Line 7
else:
    EventVenue = []
Line8 = File.readline().strip("\n")
if Line8 != "":
    EventDescription = Line8.split(Separator) #Line 8
else:
    EventDescription = []
NumberAttendee = FormatToInteger(File.readline().split()) #Line 9
AttendeeID = FormatToInteger(File.readline().split()) #Line 10
Line11 = File.readline().strip("\n")
if Line11 != "":
    AttendeeName = Line11.split(Separator) #Line 11
else:
    AttendeeName = []
Line12 = File.readline().strip("\n")
if Line12 != "":
    AttendeeDetails = Line12.split(Separator) #Line 12
else:
    AttendeeDetails = []
Line13 = File.readline().strip("\n")
if Line13 != "":
    EventID = Line13.split(Separator) #Line 13
else:
    EventID = []
NumberEvent = int(File.readline()) #Line 14
AttendeeCounter = int(File.readline()) #Line 15
File.close()

#Empty strings to allow them to be used
for Index in range(NumberEvent):
    if EventDescription[Index] == "No description":
        EventDescription[Index] = ""
for ID in range(len(AttendeeID)):
    if AttendeeDetails[ID] == "No details":
        AttendeeDetails[ID] = ""

#Get the information of index Remove then put it in index Insert, used only in function, InsertEventInOrder()
def InsertAndRemove(Insert, Remove): #Insert and Remove are integers
    #Copy all information of event indexed Remove
    TempEventName = EventName[Remove]
    TempEventDateYear = EventDateYear[Remove]
    TempEventDateMonth = EventDateMonth[Remove]
    TempEventDateDay = EventDateDay[Remove]
    TempEventStartTime = EventStartTime[Remove]
    TempEventEndTime = EventEndTime[Remove]
    TempEventVenue = EventVenue[Remove]
    TempEventDescription = EventDescription[Remove]
    TempNumberAttendee = NumberAttendee[Remove]
    TempEventID = EventID[Remove]

    #Remove all information of event indexed Remove
    EventName.pop(Remove)
    EventDateYear.pop(Remove)
    EventDateMonth.pop(Remove)
    EventDateDay.pop(Remove)
    EventStartTime.pop(Remove)
    EventEndTime.pop(Remove)
    EventVenue.pop(Remove)
    EventDescription.pop(Remove)
    NumberAttendee.pop(Remove)
    EventID.pop(Remove)

    #Insert all information of event indexed Remove into position indexed Insert
    EventName.insert(Insert, TempEventName)
    EventDateYear.insert(Insert, TempEventDateYear)
    EventDateMonth.insert(Insert, TempEventDateMonth)
    EventDateDay.insert(Insert, TempEventDateDay)
    EventStartTime.insert(Insert, TempEventStartTime)
    EventEndTime.insert(Insert, TempEventEndTime)
    EventVenue.insert(Insert, TempEventVenue)
    EventDescription.insert(Insert, TempEventDescription)
    NumberAttendee.insert(Insert, TempNumberAttendee)
    EventID.insert(Insert, TempEventID)

#Insert event in order of date and time, used during Add and Update
def InsertEventInOrder(Index):
    #Loop that checks where the information of event indexed Index should be inserted
    for Counter in range(len(EventName)):
        if Counter == Index: #Prevent checking with oneself
            continue
        elif EventDateYear[Counter] > EventDateYear[Index]: #Compare the Year
            InsertAndRemove(Counter, Index)
            break
        elif EventDateYear[Counter] < EventDateYear[Index]:
            continue
        elif EventDateMonth[Counter] > EventDateMonth[Index]: #Compare the Month
            InsertAndRemove(Counter, Index)
            break
        elif EventDateMonth[Counter] < EventDateMonth[Index]:
            continue
        elif EventDateDay[Counter] > EventDateDay[Index]: #Compare the Day
            InsertAndRemove(Counter, Index)
            break
        elif EventDateDay[Counter] < EventDateDay[Index]:
            continue
        elif EventStartTime[Counter] > EventStartTime[Index]: #Compare the Start Time
            InsertAndRemove(Counter, Index)
            break
        elif EventStartTime[Counter] == EventStartTime[Index] and EventEndTime[Counter] > EventEndTime[Index]: #Compare the End Time
            InsertAndRemove(Counter, Index)
            break
        else: #End Time of Counter <= End Time of Index
            continue

#Function for inserting event name
def InsertEventName(Index):
    Valid = False
    while not Valid:
        TempEventName = input("Enter event name: ").strip()
        if TempEventName != "" and len(TempEventName) <= 15:
            if TempEventName not in EventName:
                EventName[Index] = TempEventName
                Valid = True

            else:
                while not Valid:
                    print("Event name already exists.")
                    UserCheck = input("Do you still want to use the same name? (Y/N): ").strip().upper()
                    if UserCheck == "Y":
                        EventName[Index] = TempEventName
                        Valid = True
                        
                    elif UserCheck == "N":
                        print("Please reenter the event name.")
                        break
                
                    else:
                        print("Invalid input. Please enter Y or N.")

        else:
            print("Event name cannot be empty or more than 15 characters.")

#Function for inserting event date
def InsertEventDate(Index):
    CorrectDate = False
    while not CorrectDate:
        ValidYear = False
        while not ValidYear:
            TempEventDateYear = input("Enter event year: ").strip()
            if TempEventDateYear != "":
                if TempEventDateYear.isdigit():
                    TempEventDateYear = int(TempEventDateYear)
                    if TempEventDateYear > 0 and TempEventDateYear < 10000:
                        ValidYear = True
                        if (TempEventDateYear % 4 == 0 and TempEventDateYear % 100 != 0) or TempEventDateYear % 400 == 0:
                            LeapYear = True
                        
                        else:
                            LeapYear = False

                    else:
                        print("Event year is invalid.")

                else:
                    print("Event year must be a number.")

            else:
                print("Event year cannot be empty.")

        ValidMonth = False
        while not ValidMonth:
            TempEventDateMonth = input("Enter event month: ").strip()
            if TempEventDateMonth != "":
                if TempEventDateMonth.isdigit():
                    TempEventDateMonth = int(TempEventDateMonth)
                    if TempEventDateMonth >= 1 and TempEventDateMonth <= 7:
                        ValidMonth = True
                        if TempEventDateMonth % 2 == 0:
                            LongMonth = False
                        
                        else:
                            LongMonth = True

                    elif TempEventDateMonth >= 8 and TempEventDateMonth <= 12:
                        ValidMonth = True
                        if TempEventDateMonth % 2 == 0:
                            LongMonth = True
                        
                        else:
                            LongMonth = False

                    else:
                        print("Event month must be between 1 and 12 inclusive.")

                else:
                    print("Event month must be a number.")

            else:
                print("Event month cannot be empty.")

        ValidDay = False
        while not ValidDay:
            TempEventDateDay = input("Enter event day: ").strip()
            if TempEventDateDay != "":
                if TempEventDateDay.isdigit():
                    TempEventDateDay = int(TempEventDateDay)
                    if TempEventDateDay >= 1 and ((TempEventDateMonth == 2 and ((LeapYear and TempEventDateDay <=29) or (not LeapYear and TempEventDateDay <=28))) or (not TempEventDateMonth == 2 and ((LongMonth and TempEventDateDay <= 31) or (not LongMonth and TempEventDateDay <=30)))):
                        ValidDay = True

                    else:
                        print("Event date does not exist.")

                else:
                    print("Event day must be a number.")

            else:
                print("Event day cannot be empty.")

        ValidInput = False
        while not ValidInput:
            print(f"Event date is {TempEventDateDay:02d}/{TempEventDateMonth:02d}/{TempEventDateYear:04d}")
            UserCheck = input("Is the date correct? (Y/N): ").strip().upper()
            if UserCheck != "":
                if UserCheck == "Y":
                    ValidInput = True
                    CorrectDate = True

                elif UserCheck == "N":
                    break
                
                else:
                    print("Invalid input. Please enter Y or N.")

            else:
                print("Input cannot be empty.")

        if CorrectDate:
            EventDateYear[Index] = TempEventDateYear
            EventDateMonth[Index] = TempEventDateMonth
            EventDateDay[Index] = TempEventDateDay

        else:
            print("Please reenter the date.")

#Function for inserting event time
def InsertEventTime(Index):
    CorrectTime = False
    while not CorrectTime:
        ValidStartTime = False
        while not ValidStartTime:
            TempEventStartTime = input("Enter event start time (in 24-hour format, e.g. 1300 for 1p.m.): ").strip()
            if TempEventStartTime != "":
                if TempEventStartTime.isdigit():
                    TempEventStartTime = int(TempEventStartTime)
                    if TempEventStartTime >= 0 and TempEventStartTime < 2400 and TempEventStartTime % 100 >= 0 and TempEventStartTime % 100 < 60:
                        ValidStartTime = True

                    else:
                        print("Event start time's hour must be between 0 and 23 inclusive and minute must be between 0 and 59 inclusive.")

                else:
                    print("Event start time must be a number.")

            else:
                print("Event start time cannot be empty.")

        ValidEndTime = False
        while not ValidEndTime:
            TempEventEndTime = input("Enter event end time (in 24-hour format, e.g. 1400 for 2p.m.): ").strip()
            if TempEventEndTime != "":
                if TempEventEndTime.isdigit():
                    TempEventEndTime = int(TempEventEndTime)
                    if TempEventEndTime >= 0 and TempEventEndTime < 2400 and TempEventEndTime % 100 >= 0 and TempEventEndTime % 100 < 60:
                        ValidEndTime = True

                    else:
                        print("Event end time's hour must be between 0 and 23 inclusive and minute must be between 0 and 59 inclusive.")
                
                else:
                    print("Event end time must be a number.")

            else:
                print("Event end time cannot be empty.")

        ValidInput = False
        while not ValidInput:
            if TempEventEndTime > TempEventStartTime:
                DurationHour = TempEventEndTime // 100 - TempEventStartTime // 100
                DurationMinute = TempEventEndTime % 100 - TempEventStartTime % 100
                if DurationMinute < 0:
                    DurationMinute += 60
                    DurationHour -= 1
                
                print(f"Event time is from {TempEventStartTime:04d} to {TempEventEndTime:04d} for {DurationHour} h {DurationMinute} min.")
                UserCheck = input("Is the time correct? (Y/N) ").strip().upper()
                if UserCheck != "":
                    if UserCheck == "Y":
                        ValidInput = True
                        CorrectTime = True

                    elif UserCheck == "N":
                        print("Please reenter the time.")
                        break
                    
                    else:
                        print("Invalid input. Please enter Y or N.")

                else:
                    print("Input cannot be empty.") 

            else:
                print("Event end time cannot be earlier than event start time.")
                break

        if CorrectTime:
            EventStartTime[Index] = TempEventStartTime
            EventEndTime[Index] = TempEventEndTime

        else:
            print("Please reenter the time.")

#Function for inserting event venue
def InsertEventVenue(Index):
    Valid = False
    while not Valid:
        TempEventVenue = input("Enter event venue: ").strip()
        if TempEventVenue != "" and len(TempEventVenue) <= 15:
            EventVenue[Index] = TempEventVenue
            Valid = True

        else:
            print("Event venue cannot be empty or more than 15 characters.")

#Function for inserting event description
def InsertEventDescription(Index):
    Valid = False
    while not Valid:
        TempEventDescription = input("Enter event description (Optional): ").strip()
        if len(TempEventDescription) <= 30:
            Valid = True
            if TempEventDescription != "":
                EventDescription[Index] = TempEventDescription

            else:
                EventDescription[Index] = "-"
        else:
            print("Event description cannot be more than 30 characters.")

#Function for adding event
def AddEvent():
    print(f"\n{"=" * 30}\n{"Add Event Interface":^30}\n{"=" * 30}")
    UserCheck = "K"
    while UserCheck != "Y" or UserCheck != "N":
        UserCheck = input("Are you sure you want to add a new event? (Y/N) ").strip().upper()
        if UserCheck != "":
            if UserCheck == "Y":
                break

            elif UserCheck == "N":
                print("Event addition cancelled.\n")
                return

            else:
                print("Invalid input. Please enter Y or N.")

        else:
            print("Input cannot be empty.")

    global NumberEvent
    NumberEvent += 1
    EventName.append("")
    InsertEventName(NumberEvent-1)
    EventDateYear.append(0)
    EventDateMonth.append(0)
    EventDateDay.append(0)
    InsertEventDate(NumberEvent-1)
    EventStartTime.append(0)
    EventEndTime.append(0)
    InsertEventTime(NumberEvent-1)
    EventVenue.append("")
    InsertEventVenue(NumberEvent-1)
    EventDescription.append("")
    InsertEventDescription(NumberEvent-1)
    NumberAttendee.append(0)
    EventID.append("")
    if NumberEvent != 1:
        if CheckClashes(NumberEvent-1) == True:
            RemoveEvent(NumberEvent-1)

        else:
            print("Event added successfully.\n")
            InsertEventInOrder(NumberEvent-1)

    else:
        print("Event added successfully.\n")

def UpdateEvent():
    length_of_EventName = len(EventName)
    if length_of_EventName == 0:
        print("There are no events. Please type 1 in the interface to add an event first.\n")
        return
    
    ChoiceUpdation = True
    while ChoiceUpdation:            
        choice_on_updating_event = input("Do you want to update an event? (Y/N): ").strip().upper()
        if choice_on_updating_event == "Y":
            ChoiceUpdation = False
            
        elif choice_on_updating_event == "N":
            ChoiceUpdation = False
            return
       
        else:
            print("Invalid input. Please enter Y or N.")
            continue
                
    Updating = True      
    while Updating:      
        Output()
        choice_on_updating = input(f"Which one would you like to update? (Please enter a number from 1 - {length_of_EventName}) or B to go back: ").strip()
        if choice_on_updating.upper() == "B":
            Updating = False
                    
        if not choice_on_updating.isdigit():
            print("Invalid input. Please enter a number or B to go back.")
            continue
        choice = int(choice_on_updating)
        if 1 <= choice <= length_of_EventName:
            choice -= 1
                    
        else:
            print("Invalid event number.")
            continue
        FinishedUpdatingCurrentEvent = False
        while not FinishedUpdatingCurrentEvent:
            print(f"1. Name: {EventName[choice]}\n2. Date: {EventDateDay[choice]}/{EventDateMonth[choice]}/{EventDateYear[choice]}\n3. Venue: {EventVenue[choice]}\n4. Time: {EventStartTime[choice]:04d}-{EventEndTime[choice]:04d}\n5. Description: {EventDescription[choice]}\n6. Update all\n7. Back")
            Action = input("Select option to update (1-7): ").strip()
            if Action != "":
                FinishedUpdatingCurrentEvent = True 
                if Action == "1":
                    InsertEventName(choice)
                    print("Name updated.")
                    
                elif Action == "2":
                    if UpdateEventDate(choice) == True:
                            print("Date updated.")
                                
                    else:
                        print("Date not updated.")
                            
                elif Action == "3":                                    
                    if UpdateEventVenue(choice) == True:
                        print("Venue updated.")
                                
                    else:
                        print("Venue not updated.")                                                       
                                       
                elif Action == "4":
                    if UpdateEventTime(choice) == True:
                        print("Time updated.")
                        
                    else:
                        print("Time not updated.")                    
                            
                elif Action == "5":
                    InsertEventDescription(choice)
                    print("Description updated.")
                                                            
                elif Action == "6":
                    InsertEventName(choice)
                    DateUpdated = UpdateEventDate(choice)
                    VenueUpdated = UpdateEventVenue(choice)
                    TimeUpdated = UpdateEventTime(choice)
                    InsertEventDescription(choice)
                    if DateUpdated and VenueUpdated and TimeUpdated:
                        print("Event updated.")
                                
                    else:
                        print("Event updated with some issues.")
                                                          
                elif Action == "7":
                    break
                            
                else:
                    print("Invalid option! Please select an option from 1-7.")
                    continue
                            
                InsertEventInOrder(choice)
                Result = AskContinueUpdating()
                if Result == "same":
                    FinishedUpdatingCurrentEvent = False
                            
                elif Result == "another":
                    FinishedUpdatingCurrentEvent = True
                            
                elif Result == "quit":
                    Updating = False

            else:
                print("Invalid input! Please enter a number.")
                continue

#Function for updating event date
def UpdateEventDate(choice): 
    StoreEventDateYear = EventDateYear[choice]
    StoreEventDateMonth = EventDateMonth[choice]
    StoreEventDateDay = EventDateDay[choice]
    ValidUpdation = False
    while not ValidUpdation:
        InsertEventDate(choice)
        if CheckClashes(choice) == True:
            print(f"An event Clash was detected.\nDate has changed back to {StoreEventDateDay}/{StoreEventDateMonth}/{StoreEventDateYear}")
            EventDateYear[choice] = StoreEventDateYear
            EventDateMonth[choice] = StoreEventDateMonth
            EventDateDay[choice] = StoreEventDateDay
            while True:
                ChoiceOnRedoing= input("Do you want to re-enter your date? (Y/N): ").strip().upper()
                if ChoiceOnRedoing == "Y":
                    break
                
                elif ChoiceOnRedoing == "N":
                    ValidUpdation = True
                    return False
                
                else:
                    print("Invalid input! Please enter Y or N.")
        
        else:
            ValidUpdation = True
            return True
        
#Function for updating event start time and end time     
def UpdateEventTime(choice): 
    StoreEventStartTime = EventStartTime[choice]
    StoreEventEndTime = EventEndTime[choice]
    ValidUpdation = False
    while not ValidUpdation:
        InsertEventTime(choice)
        if CheckClashes(choice) == True:
            print(f"An event Clash was detected.\nTime has changed back to {StoreEventStartTime:04d}-{StoreEventEndTime:04d}")
            EventStartTime[choice] = StoreEventStartTime
            EventEndTime[choice] = StoreEventEndTime
            while True:
                ChoiceOnRedoing= input("Do you want to re-enter your time? (Y/N): ").strip().upper()
                if ChoiceOnRedoing == "Y":
                    break
                
                elif ChoiceOnRedoing == "N":
                    ValidUpdation = True
                    return False
                
                else:
                    print("Invalid input. Please enter Y or N.")
        
        else:
            ValidUpdation = True
            return True

#Function for updating event venue
def UpdateEventVenue(choice):
    StoreEventVenue = EventVenue[choice]
    ValidUpdation = False
    while not ValidUpdation:
        InsertEventVenue(choice)
        if CheckClashes(choice) == True:
            print(f"An event Clash was detected.\nVenue has changed back to {StoreEventVenue}")
            EventVenue[choice] = StoreEventVenue
            while True:
                ChoiceOnRedoing= input("Do you want to re-enter your venue? (Y/N): ").strip().upper()
                if ChoiceOnRedoing == "Y":
                    break
                
                elif ChoiceOnRedoing == "N":
                    ValidUpdation = True
                    return False
                
                else:
                    print("Invalid input. Please enter Y or N.")
        
        else:
            ValidUpdation = True
            return True

def AskContinueUpdating():
    while True:
        SameEvent = input("Continue updating this event? (Y/N): ").strip().upper()
        if SameEvent == "Y":
            return "same"
        elif SameEvent == "N":
            while True:
                AnotherEvent = input("Update another event? (Y/N): ").strip().upper()
                if AnotherEvent == "Y":
                    return "another"
                
                elif AnotherEvent == "N":
                    return "quit"
                
                else:
                    print("Invalid input. Please enter Y or N.")
        
        else:
            print("Invalid input. Please enter Y or N.")

#Function to remove all details of an event of given index
def RemoveEvent(Index):
    global NumberEvent
    EventName.pop(Index)
    EventDateYear.pop(Index)
    EventDateDay.pop(Index)
    EventStartTime.pop(Index)
    EventDateMonth.pop(Index)
    EventEndTime.pop(Index)
    EventVenue.pop(Index)
    EventDescription.pop(Index)
    NumberAttendee.pop(Index)
    EventID.pop(Index)
    NumberEvent -= 1

#Function to let user choose the event that is going to be deleted by entering the index
def ChooseDeleteEvent():
    Output()
    ValidEvent = False
    while not ValidEvent:
        EventChoice = input("Which event would you like to delete? (Enter Index): ").strip()
        if EventChoice.isdigit() == True:
            EventChoice = int(EventChoice)-1
            if EventChoice in range(0, NumberEvent):
                ValidEvent = True
            
            else:
                print("Invalid index.")
        
        else:
            print("Input must be an integer.")
    
    return EventChoice

#Function to choose and delete details of an event
def DeleteEvent():
    DeletingEvent = True
    while DeletingEvent:
        if NumberEvent == 0:
            print("There are no events.\n")
            return
        
        else:
            EventChoice = ChooseDeleteEvent() #Get the index of event that is being deleted
            RemoveEvent(EventChoice)
            #Ask user whether to continue deleting event
            ValidInput = False
            while not ValidInput:
                ContinueDelete = input("Do you want to continue deleting events? (Y/N): ").strip().upper()
                if ContinueDelete == "Y":
                    print("Continue to delete events.")
                    ValidInput = True
                
                elif ContinueDelete == "N":
                    print("Exiting.")
                    DeletingEvent = False
                    ValidInput = True
                
                else:
                    print("Invalid input.")

#Function to check whether a clash with time and venue occur, (Taking Index of event as parameter and returning a boolean, where True when a clash occurs)
def CheckClashes(Index):
    for Counter in range(0,NumberEvent):
        if Index == Counter:
            continue
        
        else:
            if EventVenue[Counter] == EventVenue[Index] and EventDateYear[Counter] == EventDateYear[Index] and EventDateMonth[Counter] == EventDateMonth[Index] and EventDateDay[Counter] == EventDateDay[Index] and EventStartTime[Index] < EventEndTime[Counter] and EventEndTime[Index] > EventStartTime[Counter]:
                print("Clash event detected.\nPlease reenter.")
                return True
                          
    return False

def Output():
    """
    Purpose: Print a formatted table of all events and their details, including registered attendees.
    Usage: Called by Main and ChooseEvent().
    """
    
    # Check if there are any events to display
    if not EventName:
        print(f"\n{"=" * 50}\nNo events found in the system.\n{"=" * 50}")
        return

    print(f"\n{"=" * 90}\n{'EVENT MANAGEMENT SYSTEM - SCHEDULE':^90}\n{"=" * 90}")

    # Loop through each event using index matching
    for i in range(len(EventName)):
        print(f"[Event Index: {i+1}]")
        print(f"Event Name: {EventName[i]}")
        print("-" * 50)
        # Formats single-digit days/months with leading zeros (e.g., 05/09/2026)
        print(f"Date: {EventDateDay[i]:02d}/{EventDateMonth[i]:02d}/{EventDateYear[i]:04d}")
        # Formats military time values cleanly (e.g., 0900 - 1700)
        print(f"Time: {EventStartTime[i]:04d} to {EventEndTime[i]:04d}")
        print(f"Venue: {EventVenue[i]}")
        print(f"Description: {EventDescription[i]}")
        print(f"Total Registered Attendees: {NumberAttendee[i]}")
        print("Registered Attendees List:")
        
        # Check if the nested list has elements for the current event index
        if EventID[i].strip() != "":
            print(f"{'No.':<5} {'ID':<5} {'Attendee Name':<25} {'Attendee Details'}")
            print("  " + "-" * 60)
            IDList = EventID[i].split()
            for j in range(len(IDList)):
                ID = IDList[j]
                name = AttendeeName[AttendeeID.index(int(ID))]
                details = AttendeeDetails[AttendeeID.index(int(ID))]
                print(f"{j + 1:<5} {ID:<5} {name:<25} {details}")
        
        else:
            print("No attendees registered yet.")
            
        print("=" * 90)

#Show all events with respective indexes then get the index of event and return the index
def ChooseEvent():
    Output()
    ValidEvent = False
    while not ValidEvent:
        EventChoice = input("Which event would you like to edit? (Enter Index): ")
        if EventChoice.isdigit():
            EventChoice = int(EventChoice)-1
            if EventChoice in range(NumberEvent):
                ValidEvent = True
            
            else:
                print("Invalid index.")
        
        else:
            print("Input must be an integer.")
    
    return EventChoice

#Show all attendees with respective IDs then get the ID of attendee and return the ID
def ChooseAttendee(Prompt):
    ValidID = False
    while not ValidID:
        ShowAttendee()
        IDChoice = input(f"{Prompt}").strip()
        if IDChoice.isdigit():
            IDChoice = int(IDChoice)
            if IDChoice in AttendeeID:
                ValidID = True
                return IDChoice
            
            else:
                print("Invalid index.")
        
        else:
            print("Input must be an integer.")

#Check for any clashes by taking in the ID of Attendee and Index of Event Attendee is registering for, return True when there is clash event
def CheckClashAttendee(ID,EventIndex):
    for IDIndex in range(len(EventID)):
        for IDEvent in EventID[IDIndex].split(): #IDEvent is list of IDs as string in an Event
            if IDEvent == str(ID):
                if EventIndex == IDIndex: #Check whether ID is already in event
                    print("Attendee is already registered.")
                    return True

                if EventDateYear[EventIndex] == EventDateYear[IDIndex] and EventDateMonth[EventIndex] == EventDateMonth[IDIndex] and EventDateDay[EventIndex] == EventDateDay[
                    IDIndex] and EventStartTime[IDIndex] < EventEndTime[EventIndex] and EventEndTime[IDIndex] > EventStartTime[
                    EventIndex]: #Check for clashes
                    print("Clash event detected.")
                    return True
    
    return False

#Registering an Attendee
def RegisterAttendee():
    global AttendeeCounter
    Index = ChooseEvent() #Let user choose the event they will be registered in

    #Check whether the attendee is a new user
    NewUser = "K"
    while NewUser.upper() != "N" and NewUser.upper() != "Y":
        if len(AttendeeID) != 0: #Go to registering new user if there are no attendee
            NewUser = input("Are you a new user? (Y/N): ").strip().upper()
        
        if NewUser.upper() == "Y" or len(AttendeeID) == 0:
            NewName = ""
            while NewName == "" or len(NewName) > 25:
                NewName = input("Enter Attendee Name: ").strip() #Get name of user
                if NewName == "" or len(NewName) > 25:
                    print("Invalid name.")
            AttendeeName.append(NewName)
            NewDetails = "-" * 16
            while len(NewDetails) > 15:
                NewDetails = input("Enter Attendee Details: ").strip() #Get details of user
                if len(NewDetails) > 15:
                    print("Details cannot be more than 15 characters.")
            if NewDetails == "":
                NewDetails = "-"
            AttendeeDetails.append(NewDetails) #Add the detail
            AttendeeID.append(AttendeeCounter) #Add a new ID
            print(f"Your ID is {AttendeeID[AttendeeID.index(AttendeeCounter)]}") #Show the ID of user
            EventID[Index] = f"{EventID[Index]}{AttendeeCounter} " #Add ID to the Event
            AttendeeCounter += 1
            NumberAttendee[Index] += 1
            print("Attendee registered successfully.")
            break
        
        elif NewUser.upper() == "N":
            ValidID = False
            while not ValidID:
                OldID = input("Enter your ID: ").strip() #Get ID of user
                if OldID.isdigit():
                    OldID = int(OldID)
                    if OldID in AttendeeID: #Find name of user
                        print(f"ID found, with name: {AttendeeName[AttendeeID.index(OldID)]}.")
                        if CheckClashAttendee(OldID,Index): #Check whether attendee have clashing event
                            print("Attendee is not added.")
                        
                        else:
                            EventID[Index] = f"{EventID[Index]}{OldID} " #Add ID to the Event
                            NumberAttendee[Index] += 1
                            print("Attendee registered successfully.")
                        ValidID = True
                    
                    else:
                        print("ID not found. ")
                
                else:
                    print("ID can only be integers. ")
        
        else:
            print("Invalid Input. Please enter Y or N.")

#Updating Attendee Name or Details
def UpdateAttendee():
    if len(AttendeeID) == 0:
        print("No attendees have been registered.")
        return

    #Get attendee's ID
    IDChoice = ChooseAttendee("Attendee ID to be updated: ")

    #Get what user wants to update
    ValidOption = False
    while not ValidOption:
        Option = input("Update Attendee\'s\n1 | Name\n2 | Details\n:")
        if Option == "1":
            #Get the new name
            NewName = ""
            while NewName.strip() == "":
                NewName = input("Enter Attendee New Name: ").strip()
                if NewName == "":
                    print("Invalid name.")

            AttendeeName[AttendeeID.index(IDChoice)] = NewName
            print("Name has been updated.")
            ValidOption = True
            break

        elif Option == "2":
            #Get the new details
            NewDetails = input("Enter Attendee New Details: ").strip()
            AttendeeDetails[AttendeeID.index(IDChoice)] = NewDetails
            if AttendeeDetails[AttendeeID.index(IDChoice)] == "":
                AttendeeDetails[AttendeeID.index(IDChoice)] = "-"
            
            print("Details have been updated.")
            ValidOption = True
            break

        else:
            print("Invalid input.")

#Deleting attendee or registered event from attendee
def DeleteAttendee():
    global AttendeeCounter
    if len(AttendeeID) == 0: #Check whether there is attendee
        print("No attendees have been registered.")
        return

    #Get whether user wants to delete the all information of on attendee or registration of an attendee
    DeletingAttendee = True
    while DeletingAttendee:
        DeleteChoice = input("Do you want to delete an attendee or registration of an attendee?\n1 | Delete Attendee\n2 | Delete Registration\n: ").strip()
        if DeleteChoice == "1": #Delete all information of an attendee
            #Get attendee's ID
            IDChoice = ChooseAttendee("Attendee ID to be deleted: ")

            #Remove all instances of attendee
            for IDIndex in range(len(EventID)):
                for IDEvent in EventID[IDIndex].split():
                    if IDEvent == str(IDChoice):
                        IDList = EventID[IDIndex].split()
                        if str(IDChoice) in IDList:
                            IDList.remove(str(IDChoice))
                            if len(IDList) > 0:
                                EventID[IDIndex] = " ".join(IDList) + " "
                            else:
                                EventID[IDIndex] = ""
                        NumberAttendee[IDIndex] -= 1

            AttendeeName.pop(AttendeeID.index(IDChoice))
            AttendeeDetails.pop(AttendeeID.index(IDChoice))
            AttendeeID.remove(IDChoice)
            DeletingAttendee = False
            break


        elif DeleteChoice == "2": #Delete registration of an attendee
            #Get attendee's ID
            IDChoice = ChooseAttendee("Attendee ID to be deleted from an event: ")

            #Display all events that current attendee is registered in
            IndexList = []
            print(f"{"Index":<5}|{"Name":<15}|{"Date":<15}|{"Time":<15}|{"Venue":<15}|{"Description":<30}|Number of Attendee")
            for IDIndex in range(len(EventID)):
                for IDEvent in EventID[IDIndex].split():
                    if IDEvent == str(IDChoice):
                        FormattedDate = f"{EventDateDay[IDIndex]:02d}/{EventDateMonth[IDIndex]:02d}/{EventDateYear[IDIndex]:04d}"
                        FormattedTime = f"{EventStartTime[IDIndex]:04d} - {EventEndTime[IDIndex]:04d}"
                        print(f"{IDIndex + 1:<5}|{EventName[IDIndex]:<15}|{FormattedDate:<15}|{FormattedTime:<15}|{EventVenue[IDIndex]:<15}|{EventDescription[IDIndex]:<30}|{NumberAttendee[IDIndex]}")
                        IndexList.append(IDIndex)

            #Get the event to be removed from
            ValidIndex = False
            while not ValidIndex:
                IndexChoice = input(f"Which event do you want to remove {AttendeeName[AttendeeID.index(IDChoice)]} from? (Enter index):").strip()
                if IndexChoice.isdigit():
                    IndexChoice = int(IndexChoice) - 1
                    if IndexChoice in IndexList:
                        ValidIndex = True
                        break
                    
                    else:
                        print("Invalid index.")
                
                else:
                    print("Input must be an integer.")

            #Remove attendee's ID from event
            print(f"{AttendeeName[AttendeeID.index(IDChoice)]}\'s registration in {EventName[IndexChoice]} has been removed.")
            IDList = EventID[IndexChoice].split()
            if str(IDChoice) in IDList:
                IDList.remove(str(IDChoice))
                if len(IDList) > 0:
                    EventID[IndexChoice] = " ".join(IDList) + " "
                else:
                    EventID[IndexChoice] = ""
            NumberAttendee[IndexChoice] -= 1
            DeletingAttendee = False
            break
        
        else:
            print("Input must be either \"1\" or \"2\"")

def ShowAttendee():
    print(f"{"+" * 30}\n{"Attendee List":^30}\n{"+" * 30}")

    if len(AttendeeID) == 0: #Check whether there is attendee
        print("There are no attendee.\n")
        return

    print(f"{"ID":<5}|{"Name":<25}|{"Details":<15}|Events Registered")

    #Display attendees' ID, Name, Details and Registered Events
    for ID in AttendeeID:
        AttendeeIndex = AttendeeID.index(ID)
        AttendeeEvents = ""
        for IDIndex in range(len(EventID)):
            for IDEvent in EventID[IDIndex].split():
                if IDEvent == str(ID):
                    AttendeeEvents = AttendeeEvents + EventName[IDIndex] + ", "

        if AttendeeEvents == "":
            AttendeeEvents = "-  "
        print(f"{ID:<5}|{AttendeeName[AttendeeIndex]:<25}|{AttendeeDetails[AttendeeIndex]:<15}|{AttendeeEvents[0:len(AttendeeEvents)-2]}")

#Display menu of actions that changes information of attendees
def AttendeeAction():
    if len(EventName) == 0: #Check whether there are events
        print("There are no events.\n")
        return

    Run = True
    while Run:
        print(f"\n{"*" * 30}\n{"Attendee Menu":^30}\n{"*" * 30}")
        print("1. Register Attendee")
        print("2. Update Attendee")
        print("3. Delete Attendee")
        print("4. Show Attendee")
        print("5. Go Back")
        Choice = input("Enter your choice: (1-5) ").strip()
        if Choice == "1":
            RegisterAttendee()

        elif Choice == "2":
            UpdateAttendee()

        elif Choice == "3":
            DeleteAttendee()

        elif Choice == "4":
            ShowAttendee()

        elif Choice == "5":
            Run = False

        else:
            print("Invalid input.")

#Main Interface
Run = True
while Run:
    ValidAction = False
    while not ValidAction:
        print(f"{"=" * 30}\n{"Main Interface":^30}\n{"=" * 30}")
        print("1. Add event")
        print("2. Update event details")
        print("3. Delete event")
        print("4. Register attendees")
        print("5. Display output")
        print("6. Quit")
        Action = input("What would you like to do? (1-6): ").strip()
        if Action != "":
            ValidAction = True
            if Action == "1":
                AddEvent()

            elif Action == "2":
                UpdateEvent()

            elif Action == "3":
                DeleteEvent()

            elif Action == "4":
                AttendeeAction()

            elif Action == "5":
                Output()

            elif Action == "6":
                print("Thanks for using the system. Now displaying the final event output.\n")
                Run = False
                break

            else:
                ValidAction = False
                print("Invalid input. Please select an option from 1-6.\n")

        else:
            print("Input cannot be empty.\n")

Output()

#Fill in empty strings to prevent bugs when read
for Index in range(NumberEvent):
    if EventDescription[Index] == "":
        EventDescription[Index] = "No description"
for ID in range(len(AttendeeID)):
    if AttendeeDetails[ID] == "":
        AttendeeDetails[ID] = "No details"

#Write information into "Events_Information.txt"
File = open("Events_Information.txt","w")
File.write((Separator.join(EventName).strip("\n")) + "\n")
File.write(" ".join(FormatToString(EventDateYear)) + "\n")
File.write(" ".join(FormatToString(EventDateMonth)) + "\n")
File.write(" ".join(FormatToString(EventDateDay)) + "\n")
File.write(" ".join(FormatToString(EventStartTime)) + "\n")
File.write(" ".join(FormatToString(EventEndTime)) + "\n")
File.write((Separator.join(EventVenue).strip("\n")) + "\n")
File.write((Separator.join(EventDescription).strip("\n")) + "\n")
File.write(" ".join(FormatToString(NumberAttendee)) + "\n")
File.write(" ".join(FormatToString(AttendeeID)) + "\n")
File.write((Separator.join(AttendeeName).strip("\n")) + "\n")
File.write((Separator.join(AttendeeDetails).strip("\n")) + "\n")
File.write((Separator.join(EventID).strip("\n")) + "\n")
File.write(str(NumberEvent) + "\n")
File.write(str(AttendeeCounter) + "\n")
File.close()
