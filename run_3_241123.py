from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

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
#------------------------------------------
#Drive the robot to drop the art piece and museum director
drive_base.straight(315)
drive_base.turn(-22)
front_motor.run_angle(500,-400)
wait(200)
front_motor.run_angle(500,400)

drive_base.straight(-105)
drive_base.turn(60)
drive_base.straight(345)
drive_base.turn(-30)
drive_base.straight(180)
drive_base.turn(-50)

front_motor.run_angle(400,-450)
wait(1000)
drive_base.straight(10)
wait(250)
drive_base.straight(-50)
front_motor.run_angle(400,450)
drive_base.turn(23)
drive_base.straight(130)
front_motor.run_angle(500,-350)
drive_base.turn(30)
drive_base.straight(-800)
front_motor.run_angle(500,350)


