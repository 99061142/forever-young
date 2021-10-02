# Print the AM and PM times
for period in range(1, 3):
    # 1:00 to 12:00
    for i in range(1, 12):
        hour = str(i)

        time =  "0" + hour + ":00" if len(hour) < 2 else hour + ":00" # Add the :00 behind the hour

        time += " AM" if period == 1 else " PM" # Add "AM" or "PM" after the time

        print(time)

    # print the time before it gets changed to "AM" or "PM"
    
    time = "12:00" 
    time += " PM" if period == 1 else " AM"
    
    print(time)