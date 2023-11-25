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
drive_base.straight(430)
drive_base.turn(-58)
drive_base.straight(900)

#Move towards the light show 
drive_base.turn(-32) # This was 36 before, changed to 32 for now
drive_base.straight(-180) # Was 200 before 
# Make the motor run clockwise at 500 degrees per second.
back_motor.run_angle(500,-1650) 

#Finish mission 4
front_motor.run_angle(400,-250) # Negative value of angle means move arm DOWN
drive_base.straight(75)
drive_base.turn(43)
drive_base.straight(187) 
# turn the drive base with high speed
drive_base.turn(87)

drive_base.straight(140)


# Now move towards mission 4 - 3D reality
drive_base.turn(137)
front_motor.run_angle(400,250) # reset motor arm 
drive_base.straight(400)
drive_base.turn(90)
drive_base.straight(15)
front_motor.run_angle(200,-300)
wait(1500)
drive_base.curve(-600,-110)


