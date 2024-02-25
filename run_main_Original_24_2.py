from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task

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

##Define each run as a function

#------------------------------------------
# Code for the run 1
#------------------------------------------

def run1():
    #----------------------------------
    #Masterpiece,Expert,Audience Member
    #----------------------------------
    #Drive the robot to drop the art piece and museum director
    drive_base.straight(407) #start from home area
    #Reduce the turn speed to improve accuracy
    drive_base.settings(turn_rate=80,turn_acceleration=300)
    drive_base.turn(-57) # slow turn towards museum area
    drive_base.straight(900) #drop Anna,Masterpiece, one audience member

    #---------------------------------
    #M11 light show
    #---------------------------------

    drive_base.turn(-32) # turn towards light show
    drive_base.straight(-180) # drive backwards to light show
    #back_motor.run_angle(500,-1650)
    #Define a function to run back and front motor simultaneously

    async def front_and_back():
        await multitask(back_motor.run_angle(500,-1650),front_motor.run_angle(400,-250))                                                    
    run_task(front_and_back())  #spin light show and front arm moves down

    #---------------------------------
    # M05, Augmented reality statue
    #---------------------------------

    drive_base.straight(75) #drive forward a little  
    drive_base.turn(43) # turn towards M05
    drive_base.straight(180) #drive towards M05
    # increase the turn speed and acceleration settings
    drive_base.settings(turn_rate=202,turn_acceleration=910)                      
    drive_base.turn(87) #turn the base quickly to open the statue

    #---------------------------------
    # M03 - Immersive Experience
    #---------------------------------

    drive_base.straight(140) #move forwards a bit
    drive_base.turn(137) # turn towards M03 direction
    # Define a function to Move forward and raise the front arm simultaneously  
    ####
    async def forward_and_raise_arm():
        await multitask(front_motor.run_angle(400,250),drive_base.straight(400))
    run_task(forward_and_raise_arm())  #move forward while raising the arm up

    drive_base.turn(90)  #turn the front of the robot to M03
    drive_base.straight(15)  #drive forward a little
    front_motor.run_angle(420,-210,Stop.COAST) # push immersive experience down
    wait(50) 
    #front_motor.run_angle(400,210) #lift arm up - removed on 17 Jan for improved reliability

    #---------------------------------
    #Go Home 
    #---------------------------------

    #increase the speed to save time while heading back to home area
    drive_base.settings(straight_speed=600,straight_acceleration=1200)
    drive_base.curve(-600,-110,Stop.COAST) # come back in a curve 

#------------------------------------------
# Code for the run 2
#------------------------------------------
def run2():

    drive_base.straight(250)
    drive_base.turn(-42) ## increased by 2 degrees on 15 01
    drive_base.straight(125)
    front_motor.run_angle(500,-400)

    front_motor.run_angle(500,400)
    drive_base.straight(-69)

    drive_base.turn(70)
    drive_base.straight(430)
    drive_base.turn(-75)

    #slow down to increase the accuracy of the movement towards the expert
    drive_base.settings(straight_speed=200,straight_acceleration=800)
    drive_base.settings(turn_rate=80,turn_acceleration=200)
    drive_base.straight(23) # move towards mission - reduced from 27 mm
    front_motor.run_angle(250,-450) # it was 400, now reduced to 200
    wait(750)
    drive_base.straight(10)
    wait(150)
    drive_base.straight(-55) # moving this a bit further back

    front_motor.run_angle(400,450) # it was 450 before


    drive_base.turn(22)
    drive_base.straight(140) # reduced this by 10 mm on 15 01 2024
    front_motor.run_angle(750,-380)
    drive_base.turn(33) # increased by 3 degrees on 18 Jan 

    #Drop the audience member
    back_motor.run_angle(350,-250) # Negative value of angle means move arm DOWN

    back_motor.run_angle(350,250) # Negative value of angle means move arm DOWN

    #set to original value
    drive_base.settings(turn_rate=202,turn_acceleration=910)
    drive_base.settings(straight_speed=600,straight_acceleration=1200)
    drive_base.curve(-1130,-40,Stop.COAST)

#------------------------------------------
# Code for the run 3 
#-----------------------------------------
def run3():
    
    #move for 10cm
    drive_base.straight(110)
    #turn right 42 degrees
    drive_base.turn(38)
    #Move towards sound mixer
    drive_base.straight(295)

    #Default speed settings for the drive_base (307,1152,202,910)
    #Reduce the straight and turn speed + acceleration to improve accuracy
    drive_base.settings(straight_speed=100,straight_acceleration=600)
    #mimic the action of pushing up, moving forward - do this two times to lift
    #the sound mixer
    front_motor.run_angle(200,120)
    drive_base.straight(15) # reducing this a bit from 15 to 10 
    front_motor.run_angle(200,120)
    drive_base.straight(10)

    #Now slowly turn the sound mixer so that the middle control can stay 
    drive_base.settings(turn_rate=80,turn_acceleration=150)
    drive_base.turn(16)
    wait(400) 
    drive_base.straight(-40)

    drive_base.settings(turn_rate=150,turn_acceleration=600)
    drive_base.turn(30)

    ##Reset the drive base settings to slightly less than the original value
    drive_base.settings(straight_speed=200,straight_acceleration=800)

    drive_base.straight(370)
    drive_base.turn(90)
    drive_base.straight(140) # Appoach the camera - it was 140 mm on 15 Jan 
    front_motor.run_angle(200,-225)

    #slow speed to move backwards and slow turn
    drive_base.settings(straight_speed=100,straight_acceleration=600)
    drive_base.settings(turn_rate=80,turn_acceleration=450)
    drive_base.straight(-52) # move back from the camera bit - it was-50
    drive_base.turn(71)

    ##move back and raise the arm at the same time to save some time 
    async def backwards_and_raise_arm():
        await multitask(front_motor.run_angle(500,240),drive_base.straight(-80))

    run_task(backwards_and_raise_arm())

    #front_motor.run_angle(200,240)
    #drive_base.straight(-80) # move backwards from the camera

    #set to original value
    drive_base.settings(straight_speed=200,straight_acceleration=800)
    drive_base.settings(turn_rate=100,turn_acceleration=450)
    drive_base.turn(-130) # turn towards one of the figures
    #Drop the two audience members mid way in the run 
    drive_base.straight(240)

    #### Drive base turn to straighten before dropping mini figures 
    drive_base.turn(-25)
    back_motor.run_angle(400,-250) # Negative value of angle means move arm DOWN
    back_motor.run_angle(400,250) # Negative value of angle means move arm DOWN

    #slow down to increase the accuracy of the movement towards the expert
    drive_base.settings(straight_speed=200,straight_acceleration=800)
    drive_base.settings(turn_rate=80,turn_acceleration=200)
    drive_base.turn(10) # turn back to point to the expert - Sam??
    drive_base.straight(190)

    drive_base.turn(-53) # increased a few degrees from 51 to 53 on 15 Jan
    ##collect and secure the second expert
    drive_base.straight(150)
    front_motor.run_angle(150,-200)
    drive_base.straight(-47)
    front_motor.run_angle(150,-70) 
    drive_base.turn(42)

    #set to original value
    drive_base.settings(straight_speed=600,straight_acceleration=1200)
    #Drive the robot back to left area 
    drive_base.straight(-550)
    drive_base.turn(30)
    drive_base.curve(-380,120,Stop.COAST)

#------------------------------------------
# Code for the run 4
#------------------------------------------
def run4():
    drive_base.straight(330)
    drive_base.straight(-50)
    drive_base.turn(22)
    drive_base.straight(520)
    drive_base.turn(20)
    front_motor.run_angle(500,400)
    drive_base.straight(-80)
    drive_base.turn(45)

    #Lower the arm as you move forward - this ensures that the vr statue closes 
    #if it was left open in the first run
    async def forward_and_lower_arm():
        await multitask(front_motor.run_angle(500,-380),drive_base.straight(950))

    run_task(forward_and_lower_arm())

    drive_base.turn(-35)
    drive_base.turn(35)
    drive_base.straight(210)
    drive_base.turn(42) # changed to 40 from 45 on 15 Jan 2024
    back_motor.run_angle(400,-300) # Negative value of angle means move arm DOWN
    back_motor.run_angle(400,300) # Negative value of angle means move arm DOWN

    drive_base.settings(turn_rate=202,turn_acceleration=910)
    drive_base.settings(straight_speed=600,straight_acceleration=1200)
    drive_base.turn(30)
    drive_base.straight(700,Stop.COAST)

#------------------------------------------
# Code for the run 5
#------------------------------------------
def run5():
    #Drive the robot to drop the art piece and museum director
    drive_base.straight(380,Stop.NONE) # Motow rwont decelerate
    drive_base.straight(-380,Stop.COAST)

#------------------------------------------
# Code for the run 6
#------------------------------------------
def run6():
    drive_base.straight(25)
    drive_base.settings(turn_rate=100,turn_acceleration=400)
    drive_base.turn(-50)
    drive_base.straight(415) 
    front_motor.run_time(-900,3200)
    drive_base.settings(straight_speed=150,straight_acceleration=600)
    drive_base.straight(-325)

    drive_base.turn(44)
    drive_base.settings(straight_speed=300,straight_acceleration=600)
    drive_base.straight(500)
    drive_base.turn(50)
    drive_base.settings(straight_speed=200,straight_acceleration=600)
    drive_base.straight(210)

    drive_base.settings(straight_speed=300,straight_acceleration=600)
    drive_base.straight(-230,Stop.COAST)

#------------------------------------------
# Code for the run 7
#------------------------------------------
def run7():

    drive_base.straight(500) #forward 500mm
    drive_base.turn(-43) #turn
    drive_base.straight(260)
    drive_base.turn(88)
    drive_base.straight(140)
    front_motor.run_angle(500,-600)
    drive_base.straight(-200)


    

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
        run1() 
        menu_index = 1 # increase the menu index to point to next program
    elif selected == "2":
        run2()
        menu_index = 2
    elif selected == "3":
        run3()
        menu_index = 3
    elif selected == "4":
        run4()
        menu_index = 4
    elif selected == "5":
        run5()
        menu_index = 5
    elif selected == "6":
        run6()
        menu_index = 6
    elif selected == "7":
        run7()
        break


