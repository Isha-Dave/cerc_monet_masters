from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task

from run1_24_02 import run1

from run_2_24_02 import run2
from run_3_24_02 import run3
from run_4_24_02 import run4
from run_5_24_02 import run5
from run_6_24_02 import run6
from run_7_24_02 import run7

#Initialize the PrimeHub as hub
hub = PrimeHub()

#Initialisate the robot 
# Step 1 - Initialize the drive base 
# Step 2 - Initialize the front and back motors 
# Step 3 - Initialize the left and right color sensors in the front
#---------------------------------------------------------------------

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A)

# Initialize the drive base. 
# In our robot, the wheel diameter is 88mm.
# The distance between the two wheel-ground contact points is 145mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=88, axle_track=145)
# Optionally, uncomment the line below to use the gyro for improved accuracy.
drive_base.use_gyro(True)

#Initialize the front abnd back motors 
front_motor = Motor(Port.D)
back_motor = Motor(Port.C)

# Initialize the color sensors.
right_sensor = ColorSensor(Port.F)
left_sensor = ColorSensor(Port.E)
#Create the instances of each run 
run1 = run1()
run2 = run2()
run3 = run3()
run4 = run4()
run5= run5()
run6 = run6()
run7 = run7()
    

# Let's offer these menu options. You can add as many as you like.
menu_options = ("1", "2", "3", "4", "5", "6", "7")
menu_index = 0

while True:

    # Normally, the center button stops the program. But we want to use the
    # center button for our menu. So we can disable the stop button.
    hub.system.set_stop_button(None)

    while True:

        hub.display.char(menu_options[menu_index])

        # Wait for any button.
        pressed = ()
        while not pressed:
            pressed = hub.buttons.pressed()
            wait(10)
        
        # Wait for the button to be released.
        while hub.buttons.pressed():
            wait(10)

        # Now check which button was pressed.
        if Button.CENTER in pressed:
            # Center button, so the menu is done!
            break
        elif Button.LEFT in pressed:
            # Left button, so decrement menu menu_index.
            menu_index = (menu_index - 1) % len(menu_options)
        elif Button.RIGHT in pressed:
            # Right button, so increment menu menu_index.
            menu_index = (menu_index + 1) % len(menu_options)
        

    # Now we want to use the Center button as the stop button again.
    hub.system.set_stop_button(Button.CENTER)

    # Based on the selection, choose a program.
    selected = menu_options[menu_index]
    if selected == "1":
        run1.run(drive_base, front_motor,back_motor) 
        menu_index = 1 # increase the menu index to point to next program
    elif selected == "2":
        run2.run(drive_base, front_motor, back_motor)
        menu_index = 2
    elif selected == "3":
        run3.run(drive_base, front_motor, back_motor)
        menu_index = 3
    elif selected == "4":
        run4.run(drive_base, front_motor, back_motor)
        menu_index = 4
    elif selected == "5":
        run5.run(drive_base, front_motor, back_motor)
        menu_index = 5
    elif selected == "6":
        run6.run(drive_base, front_motor, back_motor)
        menu_index = 6
    elif selected == "7":
        run7.run(drive_base, front_motor, back_motor)
        break


