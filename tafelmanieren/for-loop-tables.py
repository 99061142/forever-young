choosing_number = True # Boolean for the number 


while choosing_number:
    number = input("Kies een getal voor de tafel: ")

    # Check if its a number, and if not the question gets asked again
    try:
        if int(number) >= 0:
            number = int(number)
            choosing_number = False
    
    except: 
        print("Kies een geldig getal")


# Print the table from 1 to 10 with the number the user has chosen
for i in range(1, 11):
    total = i * number
    print(i, "*", number, "=", total)
