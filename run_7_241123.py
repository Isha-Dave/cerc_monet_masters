from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch,multitask, run_task


hub = PrimeHub()
#Initialisate the robot 
# Step 1 - Initialize the drive base 
# Step 2 - Initialize the front and back motors 
# Step 3 - Initialize the left and right color sensors in the front
#---------------------------------------------------------------------
async def turn_and_run():
    await multitask(drive_base.turn(-25),front_motor.run_angle(500,85))

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
drive_base.straight(765)
front_motor.run_angle(200,-250)
drive_base.straight(-50)
front_motor.run_angle(200,250)
drive_base.turn(45)
drive_base.straight(150)
drive_base.straight(-120)
front_motor.run_angle(200,-260)
drive_base.straight(-20)
drive_base.turn(-15)
drive_base.straight(110)
front_motor.run_angle(4000,100,Stop.HOLD,True)
drive_base.turn(-10,Stop.HOLD,True)
front_motor.run_angle(4000,-100,Stop.HOLD,True)
drive_base.straight(-220)
drive_base.turn(65)
front_motor.run_angle(4000,225,Stop.HOLD,True)#
drive_base.straight(350)
drive_base.turn(-90)
drive_base.straight(120)
drive_base.turn(-60)
