#Dropping Experts and Audience in different areas

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask

class run4():
#------------------------------------------
# Code for the robot
#------------------------------------------
    def run(self, drive_base = DriveBase, front_motor = Motor, back_motor = Motor):

        #------------------------------------------
        # Code for the robot
        #------------------------------------------
        #Drive the robot to drop the art piece and museum director
        drive_base.straight(330)
        drive_base.straight(-50)
        drive_base.turn(22)
        drive_base.straight(530)
        drive_base.turn(20)
        front_motor.run_angle(500,400)
        drive_base.straight(-80)
        drive_base.turn(45)

        #Lower the arm as you move forward - this ensures that the vr statue closes 
        #if it was left open in the first run
        async def forward_and_lower_arm():
            await multitask(front_motor.run_angle(500,-380),drive_base.straight(950))

        run_task(forward_and_lower_arm())

        drive_base.turn(-35)
        drive_base.turn(35)
        drive_base.straight(210)
        drive_base.turn(42) # changed to 40 from 45 on 15 Jan 2024
        back_motor.run_angle(400,-300) # Negative value of angle means move arm DOWN
        back_motor.run_angle(400,300) # Negative value of angle means move arm DOWN

        drive_base.settings(turn_rate=202,turn_acceleration=910)
        drive_base.settings(straight_speed=600,straight_acceleration=1200)
        drive_base.turn(30)
        drive_base.straight(700,Stop.COAST)
        drive_base.settings(307,1152,202,910) # Reset the speed settings to default