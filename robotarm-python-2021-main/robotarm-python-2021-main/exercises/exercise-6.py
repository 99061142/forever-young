# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 6')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:

for i in range(7):
    robotArm.moveRight()


for i in range(8):

    robotArm.grab()

    robotArm.moveRight()

    robotArm.drop()

    for i in range(2):
        robotArm.moveLeft()


robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()