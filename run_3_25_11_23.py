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


#------------------------------------------
# Code for the robot
#-----------------------------------------
#move for 10cm
drive_base.straight(110)
#turn right 42 degrees
drive_base.turn(46)
#Move towards sound mixer
drive_base.straight(375)

#Default speed settings for the drive_base (307,1152,202,910)
#Reduce the straight and turn speed + acceleration to improve accuracy
drive_base.settings(straight_speed=100,straight_acceleration=600)
drive_base.settings(turn_rate=80,turn_acceleration=250)
#mimic the action of pushing up, moving forward - do this two times to lift
#the sound mixer
front_motor.run_angle(200,120)
drive_base.straight(15)
front_motor.run_angle(200,120)
drive_base.straight(10)

#Now slowly turn the sound mixer so that the middle control can stay 
drive_base.turn(12)
wait(600)
drive_base.straight(-40)
drive_base.turn(30)

##Reset the drive base settings to slightly less than the original value
drive_base.settings(straight_speed=307,straight_acceleration=1152)
drive_base.settings(turn_rate=150,turn_acceleration=600)

drive_base.straight(400)
drive_base.turn(85)
drive_base.straight(150) # changing
front_motor.run_angle(150,-200)

#slow speed to move backwards and slow turn
drive_base.settings(straight_speed=100,straight_acceleration=600)
drive_base.settings(turn_rate=80,turn_acceleration=450)
drive_base.straight(-100)
drive_base.turn(68)

front_motor.run_angle(200,240)
drive_base.straight(-80) # move backwards from the camera

#set to original value
drive_base.settings(straight_speed=307,straight_acceleration=1152)
drive_base.settings(turn_rate=202,turn_acceleration=910)
#wait(100)
drive_base.turn(-120) # turn towards one of the figures
#Drop the two audience members mid way in the run 
drive_base.straight(230)

#### Drive base turn to straighten before dropping mini figures 
drive_base.turn(-30)
back_motor.run_angle(500,-300) # Negative value of angle means move arm DOWN
back_motor.run_angle(500,300) # Negative value of angle means move arm DOWN

#slow down to increase the accuracy of the movement towards the expert
drive_base.settings(straight_speed=200,straight_acceleration=800)
drive_base.settings(turn_rate=80,turn_acceleration=200)
drive_base.turn(10) # turn back to point to the expert - Sam??
drive_base.straight(220)

drive_base.turn(-50)
##collect and secure the second expert
drive_base.straight(140)
front_motor.run_angle(150,-230)

#set to original value
drive_base.settings(turn_rate=202,turn_acceleration=910)
drive_base.settings(straight_speed=307,straight_acceleration=1152)

#Drive the robot back to left area 
drive_base.turn(42)
drive_base.straight(-1200)
drive_base.turn(-70)
drive_base.straight(-300)