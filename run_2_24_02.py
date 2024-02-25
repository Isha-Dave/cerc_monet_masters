from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#------------------------------------------
# Code for the robot
#------------------------------------------
class run2():

    def run(self, drive_base = DriveBase, front_motor = Motor, back_motor = Motor):
        drive_base.straight(250)
        drive_base.turn(-42) ## increased by 2 degrees on 15 01
        drive_base.straight(125)
        front_motor.run_angle(500,-400)

        front_motor.run_angle(500,400)
        drive_base.straight(-69)

        drive_base.turn(70)
        drive_base.straight(430)
        drive_base.turn(-75)

        #slow down to increase the accuracy of the movement towards the expert
        drive_base.settings(straight_speed=200,straight_acceleration=800)
        drive_base.settings(turn_rate=80,turn_acceleration=200)
        drive_base.straight(23) # move towards mission - reduced from 27 mm
        front_motor.run_angle(250,-450) # it was 400, now reduced to 200
        wait(750)
        drive_base.straight(10)
        wait(150)
        drive_base.straight(-55) # moving this a bit further back

        front_motor.run_angle(400,450) # it was 450 before


        drive_base.turn(22)
        drive_base.straight(140) # reduced this by 10 mm on 15 01 2024
        front_motor.run_angle(750,-380)
        drive_base.turn(33) # increased by 3 degrees on 18 Jan 

        #Drop the audience member
        back_motor.run_angle(350,-250) # Negative value of angle means move arm DOWN

        back_motor.run_angle(350,250) # Negative value of angle means move arm DOWN

        #set to original value
        drive_base.settings(turn_rate=202,turn_acceleration=910)
        drive_base.settings(straight_speed=600,straight_acceleration=1200)
        drive_base.curve(-1130,-40,Stop.COAST)
        drive_base.settings(307,1152,202,910) # Reset the speed settings to default


