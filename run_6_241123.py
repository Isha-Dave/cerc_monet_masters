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
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A)

# Initialize the drive base. 
# In our robot, the wheel diameter is 88mm.
# The distance between the two wheel-ground contact points is 145mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=88, axle_track=145)
# Optionally, uncomment the line below to use the gyro for improved accuracy.
#drive_base.use_gyro(True)
#drive_base.use_gyro(True)

#Initialize the front abnd back motors 
front_motor = Motor(Port.D)
back_motor = Motor(Port.C)

# Initialize the color sensors.
right_sensor = ColorSensor(Port.F)
left_sensor = ColorSensor(Port.E)


#------------------------------------------
# Code for the robot
#------------------------------------------

# Run 4 Athena
# Below code is to complete the mission number
# Mission start
# ===============================================

drive_base.straight(25)
print(drive_base.settings())
drive_base.settings(turn_rate=100,turn_acceleration=400)
drive_base.turn(-50)
drive_base.straight(412)
front_motor.run_time(-500,5000,Stop.HOLD,True)
# Mission end
# ===============================================

# Below code is to complete the mission number
# Mission start
# ===============================================
drive_base.straight(-100)
drive_base.turn(100)
drive_base.straight(250)
drive_base.turn(80)
drive_base.straight(-160)
back_motor.run_time(-200,700,Stop.HOLD,True)
drive_base.straight(35)
back_motor.run_time(60,300,Stop.HOLD,True)
drive_base.straight(50)
back_motor.run_time(100,500,Stop.HOLD,True)
drive_base.straight(300)
drive_base.turn(50)
drive_base.straight(145)

# ===============================================
# Mission complete
