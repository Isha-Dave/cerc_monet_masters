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

drive_base.straight(365)

#Default speed settings for the drive_base (307,1152,202,910)
#Reduce the straight and turn speed + acceleration to improve accuracy
drive_base.settings(straight_speed=100,straight_acceleration=600)
drive_base.settings(turn_rate=80,turn_acceleration=250)

front_motor.run_angle(200,100)
drive_base.straight(15)
front_motor.run_angle(180,100)
drive_base.straight(10)


drive_base.turn(15)
wait(600)
drive_base.straight(-40)
drive_base.turn(30)

#set the drive base turn rate to same values as earlier
##Reset the drive base settings to original value

drive_base.settings(straight_speed=307,straight_acceleration=1152)
drive_base.settings(turn_rate=202,turn_acceleration=910)
drive_base.straight(420)
drive_base.turn(85)
drive_base.straight(115)
front_motor.run_angle(150,-200)

#slow speed to move backwards and slow turn
drive_base.settings(straight_speed=100,straight_acceleration=600)
drive_base.settings(turn_rate=80,turn_acceleration=250)

drive_base.straight(-100)
drive_base.turn(70)

#set to original value
drive_base.settings(turn_rate=202,turn_acceleration=910)
drive_base.settings(straight_speed=307,straight_acceleration=1152)


front_motor.run_angle(150,240)
drive_base.straight(-50) # move backwards from the camera

drive_base.turn(-140) # turn towards one of the figures
#Drop the two audience members mid way in the run 
drive_base.straight(240)
back_motor.run_angle(300,-250) # Negative value of angle means move arm DOWN
back_motor.run_angle(300,250) # Negative value of angle means move arm DOWN

#Continue to the expert 
drive_base.straight(230)
drive_base.settings(turn_rate=80,turn_acceleration=250)
drive_base.settings(straight_speed=100,straight_acceleration=600)

#secure the first expert
drive_base.turn(-60)
#collect and secure the second expert
drive_base.straight(120)
front_motor.run_angle(150,-220)



#set to original value
drive_base.settings(turn_rate=202,turn_acceleration=910)
drive_base.settings(straight_speed=307,straight_acceleration=1152)

drive_base.turn(45)
drive_base.straight(-1200)
drive_base.turn(-60)
drive_base.straight(-300)