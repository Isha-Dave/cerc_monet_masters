from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
#------------------------------------------
# Code for the robot
#------------------------------------------

# Run 7
# Below code is to complete the mission number
# Mission start
# ===============================================
class run7():
#------------------------------------------
# Code for the robot
#------------------------------------------
    def run(self, drive_base = DriveBase, front_motor = Motor, back_motor = Motor):
        drive_base.straight(500) #forward 500mm
        drive_base.turn(-43) #turn
        drive_base.straight(260)
        drive_base.turn(88)
        drive_base.straight(140)
        front_motor.run_angle(500,-900)
        drive_base.straight(-200)
        drive_base.settings(307,1152,202,910) # Reset the speed settings to default