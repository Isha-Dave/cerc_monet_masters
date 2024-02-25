from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class run6():
#------------------------------------------
# Code for the robot
#------------------------------------------
    def run(self, drive_base = DriveBase, front_motor = Motor, back_motor = Motor):

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

        drive_base.settings(straight_speed=300,straight_acceleration=600)
        drive_base.straight(-500,Stop.COAST)
        drive_base.settings(307,1152,202,910) # Reset the speed settings to default
        # ===============================================
        # Mission complete
