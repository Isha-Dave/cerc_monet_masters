from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, hub_menu, run_task

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
#print(drive_base.settings())
#drive_base.straight(100)
#old_base_value = drive_base.settings() #save the current value of drive base settings in a tuple
#print(old_base_value[0])
#drive_base.settings(straight_speed=60) 
#print(drive_base.settings())
#drive_base.straight(-100)
#drive_base.settings(straight_speed=old_base_value[0])
#print(drive_base.settings())

async def turn_and_run():
    await multitask(drive_base.straight(90),front_motor.run_time(300,1000))

run_task(turn_and_run())

#drive_base.turn(-57)
#drive_base.straight(840)
# Make the motor run clockwise at 500 degrees per second.
#back_motor.run_time(-200,1500,Stop.HOLD,True)
#drive_base.turn(-30)
#drive_base.straight(-1700)
#Code for the colorful raibow wheel
#drive_base.turn(-25)
#drive_base.straight(-148)
#front_motor.speed(30)
#front_motor.run_time(-500,3200,Stop.HOLD,True)


