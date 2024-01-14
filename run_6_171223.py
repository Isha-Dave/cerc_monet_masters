from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
#Initialisae the robot 
# Step 1 - Initialize the drive base 
# Step 2 - Initialize the front and right motors 
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
# Use the gyro for improved accuracy.
drive_base.use_gyro(True)

#Initialize the front and back motors 
front_motor = Motor(Port.D)
back_motor = Motor(Port.C)

# Initialize the color sensors.
right_sensor = ColorSensor(Port.F)
left_sensor = ColorSensor(Port.E)


#------------------------------------------
# Code for the robot
#------------------------------------------

# Run 6
# Below code is to complete the mission number
# Mission start
# ===============================================

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

# Code to turn speakers
#front_motor.run_time(-900,1200)

#
# ===============================================
# Mission complete
