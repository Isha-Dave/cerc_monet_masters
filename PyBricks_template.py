from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
#Initialisate the robot 
# Step 1 - Initialize the drive base 
# Step 2 - Initialize the front and right motors 
# Step 3 - Initialize the left and right color sensors in the front
#---------------------------------------------------------------------

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)

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

drive_base.straight(300)
drive_base.turn(-57)
drive_base.straight(840)
# Make the motor run clockwise at 500 degrees per second.
back_motor.run_time(500,1000,Stop.HOLD,True)

drive_base.turn(-30)
drive_base.straight(-160)
#Code for the colorful raibow wheel
#drive_base.turn(-25)
#drive_base.straight(-148)
front_motor.speed(30)
front_motor.run_time(500,1000,Stop.HOLD,True)

drive_base.turn(-90)
drive_base.straight(190)
drive_base.turn(90)
drive_base.straight(30)
back_motor.run_time(-500,1500,Stop.HOLD,True)
back_motor.run_time(500,1500,Stop.HOLD,True)
drive_base.straight(-100)
back_motor.run_time(-500,1500,Stop.HOLD,True)


