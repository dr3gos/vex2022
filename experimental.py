#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
endgame = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)
mrope = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
flywheel2 = Motor(Ports.PORT12, GearSetting.RATIO_18_1, True)
spinner = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
leftback = Motor(Ports.PORT16, GearSetting.RATIO_18_1, True)
rightback = Motor(Ports.PORT17, GearSetting.RATIO_18_1, True)
lloader = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)
rloader = Motor(Ports.PORT19, GearSetting.RATIO_18_1, True)
mloader = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)


# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      [REDACTED] Feb. 2023 HS Robotics
#	Author:       Dragos S.
#	Created:      6.12.2022 - 2.2.2023
#	Description:  Vex V5 Code for the HS Robotics build, 2023
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code

#slloader
lloader.set_stopping(HOLD)
lloader.set_velocity(75, PERCENT)

#srloader
rloader.set_stopping(HOLD)
rloader.set_velocity(75, PERCENT)

#smloader
mloader.set_stopping(HOLD)
mloader.set_velocity(100, PERCENT)

#sendgame
endgame.set_stopping(BRAKE)
endgame.set_max_torque(100, PERCENT)
endgame.set_velocity(100, PERCENT)

#smrope
mrope.set_max_torque(70, PERCENT)
mrope.set_velocity(100, PERCENT)
mrope.set_stopping(BRAKE)

#sflywheel1 (left)
# flywheel.set_stopping(COAST)
# flywheel.set_max_torque(100, PERCENT)
# flywheel.set_velocity(100, PERCENT)

#sflywheel2 (right)
# flywheel2.set_stopping(COAST)
# flywheel2.set_max_torque(100, PERCENT)
# flywheel2.set_velocity(100, PERCENT)

#sspinner
spinner.set_stopping(BRAKE)
spinner.set_max_torque(100, PERCENT)    
spinner.set_velocity(100, PERCENT) 

#sleftback
leftback.set_stopping(COAST)
rightback.set_stopping(COAST)
 
#functions:

def ropeing():
    if controller_1.buttonA.pressing():
        mrope.spin(FORWARD, 1000, VOLT)
    elif controller_1.buttonX.pressing():
        mrope.spin(REVERSE)
    elif controller_1.buttonB.pressing():
        mrope.stop()

# def flywheeling():
#     if controller_1.buttonA.pressing():
#         #flywheel.spin(FORWARD, 1000, VOLT)
#         #flywheel2.spin(FORWARD, 1000, VOLT)
#     elif controller_1.buttonB.pressing():
#         #flywheel.stop()
#         #flywheel2.stop()

# def endgameing():
#     if controller_1.buttonX.pressing():
#         endgame.spin_to_position(50, DEGREES)
#         wait(1, MSEC)
#     elif controller_1.buttonY.pressing():
#         endgame.spin_to_position(0, DEGREES)
#     else:
#         endgame.stop()
        
def spinning():
    if controller_1.buttonR1.pressing():
        spinner.spin(FORWARD)
    elif controller_1.buttonL1.pressing(): 
        spinner.spin(REVERSE)
    else:
        spinner.stop()

def driving():
    updown = controller_1.axis3.position()
    leftright = controller_1.axis1.position()
    leftback.set_velocity(((leftright * -1)  + (updown * 1)), PERCENT)
    rightback.set_velocity(((leftright * -1) - (updown * 1)), PERCENT)
    leftback.spin(FORWARD)
    rightback.spin(FORWARD)

def loading():
    if controller_1.buttonR2.pressing():
        rloader.spin(FORWARD)
        lloader.spin(FORWARD)
        mloader.spin(FORWARD)
    elif controller_1.buttonL2.pressing():
        rloader.spin(REVERSE)
        lloader.spin(REVERSE)
        mloader.spin(REVERSE)
    else:
        rloader.stop()
        lloader.stop()
        mloader.stop()

#autonomous code: 

def autonomous():
        leftback.set_velocity(-10, PERCENT)
        rightback.set_velocity(-10, PERCENT)
        #forward
        rightback.spin(FORWARD)
        leftback.spin(REVERSE)
        wait(1.5, SECONDS)
        rightback.stop()
        leftback.stop()
        wait(5, MSEC)
        #turn right
        rightback.spin(FORWARD)
        leftback.spin(FORWARD)
        wait(1.2, SECONDS)
        rightback.stop()
        leftback.stop()
        wait(5, MSEC)
        #go back + roller
        rightback.spin(REVERSE)
        leftback.spin(FORWARD)
        wait(1.7, SECONDS)
        spinner.spin_for(REVERSE, 0.3, TURNS, wait=True)
        rightback.stop()
        leftback.stop()
        #cut here

        # #forward
        # rightback.spin(REVERSE)
        # leftback.spin(FORWARD)
        # wait(1.5, SECONDS)
        # rightback.stop()
        # leftback.stop()
        # wait(5, MSEC)
        # #turn right
        # rightback.spin(REVERSE)
        # leftback.spin(REVERSE)
        # wait(1.2, SECONDS)
        # rightback.stop()
        # leftback.stop()
        # wait(5, MSEC)
        # #go back + roller
        # rightback.spin(FORWARD)
        # leftback.spin(REVERSE)
        # wait(1, SECONDS)
        # rightback.stop()
        # leftback.stop()
        # # wait(5, MSEC)

        #turn right more
        
        leftback.set_velocity(-30, PERCENT)
        rightback.set_velocity(-30, PERCENT)
        rightback.spin(FORWARD)
        leftback.spin(REVERSE)
        wait(0.05, SECONDS)
        rightback.spin(FORWARD)
        leftback.spin(FORWARD)
        wait(0.6, SECONDS)
        rightback.stop()
        leftback.stop()
        wait(5,MSEC)
        #go forward for box
        leftback.set_velocity(-60, PERCENT)
        rightback.set_velocity(-60, PERCENT)
        rightback.spin(FORWARD)
        leftback.spin(REVERSE)
        wait(2, SECONDS)
        rightback.stop()
        leftback.stop()
        wait(5,MSEC)
        #discs go up
        rloader.spin(REVERSE)
        lloader.spin(REVERSE)
        wait(5, SECONDS)
        rloader.stop()
        lloader.stop()
        
#sa imi bag pula in toate echipele astea de au avut timp

#realtime code
endgame.set_position(0, DEGREES)
while 1:
    if controller_1.buttonRight.pressing():
        autonomous()
    
    if controller_1.buttonLeft.pressing():
        while 1:
            ropeing()
            #endgameing()
            #flywheeling()
            spinning()
            driving()
            loading()
            wait(5, MSEC)
    wait(5, MSEC)