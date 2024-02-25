from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task

class run3():
#------------------------------------------
# Code for the robot
#------------------------------------------
    def run(self, drive_base = DriveBase, front_motor = Motor, back_motor = Motor):

        #------------------------------------------
        # Code for the robot
        #-----------------------------------------
        #move for 10cm
        drive_base.straight(110)
        #turn right 42 degrees
        drive_base.turn(38)
        #Move towards sound mixer
        drive_base.straight(295)

        #Default speed settings for the drive_base (307,1152,202,910)
        #Reduce the straight and turn speed + acceleration to improve accuracy
        drive_base.settings(straight_speed=100,straight_acceleration=600)
        #mimic the action of pushing up, moving forward - do this two times to lift
        #the sound mixer
        front_motor.run_angle(200,120)
        drive_base.straight(15) # reducing this a bit from 15 to 10 
        front_motor.run_angle(200,120)
        drive_base.straight(10)

        #Now slowly turn the sound mixer so that the middle control can stay 
        drive_base.settings(turn_rate=80,turn_acceleration=150)
        drive_base.turn(16) # it was 16 before
        wait(400) # was 400 before 
        drive_base.straight(-40)

        drive_base.settings(turn_rate=150,turn_acceleration=600)
        drive_base.turn(30)

        ##Reset the drive base settings to slightly less than the original value
        drive_base.settings(straight_speed=200,straight_acceleration=800)

        drive_base.straight(370)
        drive_base.turn(90)
        drive_base.straight(140) # Appoach the camera  
        front_motor.run_angle(200,-220) # Reduced 10 degrees on 25 Feb

        #slow speed to move backwards and slow turn
        drive_base.settings(straight_speed=100,straight_acceleration=600)
        drive_base.settings(turn_rate=80,turn_acceleration=450)
        drive_base.straight(-52) # move back from the camera bit - it was-50
        drive_base.turn(71)

        ##move back and raise the arm at the same time to save some time 
        async def backwards_and_raise_arm():
            await multitask(front_motor.run_angle(500,240),drive_base.straight(-80))

        run_task(backwards_and_raise_arm())

        #front_motor.run_angle(200,240)
        #drive_base.straight(-80) # move backwards from the camera

        #set to original value
        drive_base.settings(straight_speed=200,straight_acceleration=800)
        drive_base.settings(turn_rate=100,turn_acceleration=450)
        drive_base.turn(-130) # turn towards one of the figures
        #Drop the two audience members mid way in the run 
        drive_base.straight(240)

        #### Drive base turn to straighten before dropping mini figures 
        drive_base.turn(-25)
        back_motor.run_angle(400,-250) # Negative value of angle means move arm DOWN
        back_motor.run_angle(400,250) # Negative value of angle means move arm DOWN

        #slow down to increase the accuracy of the movement towards the expert
        drive_base.settings(straight_speed=200,straight_acceleration=800)
        drive_base.settings(turn_rate=80,turn_acceleration=200)
        drive_base.turn(10) # turn back to point to the expert - Sam??
        drive_base.straight(190)

        drive_base.turn(-53) # increased a few degrees from 51 to 53 on 15 Jan
        ##collect and secure the second expert
        drive_base.straight(150)
        front_motor.run_angle(150,-200)
        drive_base.straight(-47)
        front_motor.run_angle(150,-70) 
        drive_base.turn(42)

        #set to original value
        drive_base.settings(straight_speed=600,straight_acceleration=1200)
        #Drive the robot back to left area 
        drive_base.straight(-550)
        drive_base.turn(30)
        drive_base.curve(-380,120,Stop.COAST)
        drive_base.settings(307,1152,202,910) # Reset the speed settings to default