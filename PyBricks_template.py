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
#------------------------------------------

drive_base.straight(300)
#drive_base.turn(-57)
#drive_base.straight(840)
# Make the motor run clockwise at 500 degrees per second.
#back_motor.run_time(-200,1500,Stop.HOLD,True)
#drive_base.turn(-30)
#drive_base.straight(-1700)
#Code for the colorful raibow wheel
#drive_base.turn(-25)
#drive_base.straight(-148)
front_motor.speed(30)
front_motor.run_time(-500,3200,Stop.HOLD,True)


#------------------------------------------
# Example speed for changing the speed of the robot
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

#Example of how to create and run two different bits at the same time
# It needs to import multitask and run_task from the menu

async def turn_and_run():
    await multitask(drive_base.straight(90),front_motor.run_time(300,1000))

run_task(turn_and_run())
#-------------------------
#ANOTHER example 
#The following example shows how to use multitasking to 
#make a robot drive forward, 
#then turn and move a gripper at the same time, 
#and then drive backward.
#-------------------------------
# Move the gripper up and down.
#async def move_gripper():
 #   await gripper.run_angle(500, -90)
  #  await gripper.run_angle(500, 90)


# Drive forward, turn move gripper at the same time, and drive backward.
#async def turn_and_move_gripper():
 #   await drive_base.straight(250)
  #  await multitask(drive_base.turn(90), move_gripper())
   # await drive_base.straight(-250)


# Runs the main program from start to finish.
#run_task(turn_and_move_gripper())