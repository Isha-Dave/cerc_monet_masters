from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

##Run with the new position as the robot cannot extend outside the home area

#----------------------------------------------
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
#------------------------------------------
#Drive the robot to drop the art piece and museum director
drive_base.straight(250)
drive_base.turn(-41)
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
drive_base.straight(30)
front_motor.run_angle(400,-450)
wait(1000)
drive_base.straight(10)
wait(150)
drive_base.straight(-50)

front_motor.run_angle(400,450)


drive_base.turn(20)
drive_base.straight(150)
front_motor.run_angle(750,-400)
drive_base.turn(30)

#Drop the audience member
back_motor.run_angle(350,-250) # Negative value of angle means move arm DOWN

back_motor.run_angle(350,250) # Negative value of angle means move arm DOWN

#set to original value
drive_base.settings(turn_rate=202,turn_acceleration=910)
drive_base.settings(straight_speed=600,straight_acceleration=1200)
drive_base.curve(-1000,-40)



