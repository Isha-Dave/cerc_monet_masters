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
#print(drive_base.distance())
drive_base.turn(-58)
#print(drive_base.angle())
#print(drive_base.state())
drive_base.straight(900)
#print(drive_base.distance())


#Commented for debugging
drive_base.straight(-70)
#print(drive_base.distance())

#Move towards the light show 
drive_base.turn(-32) # This was 36 before, changed to 32 for now
drive_base.straight(-180) # Was 200 before 
# Make the motor run clockwise at 500 degrees per second.
back_motor.run_angle(500,-1650) 

#Finish mission 4
front_motor.run_angle(500,-220) # Negative value of angle means move arm DOWN
drive_base.straight(50)
drive_base.turn(45)
drive_base.straight(250)
# turn the drive base with high speed
drive_base.turn(85)
front_motor.run_angle(300,45) # Positive value of the angle means UP

# Next mission is to lift the flap on mission 13
drive_base.straight(210)
#drive_base.turn(137) # Turn the robot towards mission 3 
front_motor.run_angle(250,200) #Position the arm to its original position

# Now move towards mission 4 - 3D reality
drive_base.turn(135)
drive_base.straight(450)
drive_base.turn(90)
drive_base.straight(90)
front_motor.run_angle(300,-200)
front_motor.run_angle(300,200)
drive_base.straight(-500)




