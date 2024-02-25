from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
#------------------------------------------
class run5():
#------------------------------------------
# Code for the robot
#------------------------------------------
    def run(self, drive_base = DriveBase, front_motor = Motor, back_motor = Motor):
        #------------------------------------------
        # Code for the robot
        #------------------------------------------
        #Drive the robot to drop the art piece and museum director
        drive_base.straight(380,Stop.NONE) # Motow rwont decelerate
        drive_base.straight(-380,Stop.COAST)
        drive_base.settings(307,1152,202,910) # Reset the speed settings to default