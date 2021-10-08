# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:

for i in range(9):
    robotArm.moveRight()


for block in range(1, 4):
    if block == 1:
        move_amount = 9 
    elif block == 2:
        move_amount = 5
    else:
        move_amount = 2

    for i in range(move_amount):
        robotArm.moveLeft()

    robotArm.grab()

    for i in range(move_amount):
        robotArm.moveRight()

    robotArm.drop()
    

    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()