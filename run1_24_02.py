from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task


#----------------------------------
#Masterpiece,Expert,Audience Member
#----------------------------------
class run1():
    
    def run(self, drive_base = DriveBase, front_motor = Motor, back_motor = Motor):
        #Drive the robot to drop the art piece and museum director
        drive_base.straight(407) #start from home area
        #Reduce the turn speed to improve accuracy
        drive_base.settings(turn_rate=80,turn_acceleration=300)
        drive_base.turn(-57) # slow turn towards museum area
        drive_base.straight(900) #drop Anna,Masterpiece, one audience member

        #---------------------------------
        #M11 light show
        #---------------------------------

        drive_base.turn(-32) # turn towards light show
        drive_base.straight(-180) # drive backwards to light show
        #back_motor.run_angle(500,-1650)
        #Define a function to run back and front motor simultaneously

        async def front_and_back():
            await multitask(back_motor.run_angle(500,-1650),front_motor.run_angle(400,-250))                                                    
        run_task(front_and_back())  #spin light show and front arm moves down

        #---------------------------------
        # M05, Augmented reality statue
        #---------------------------------

        drive_base.straight(75) #drive forward a little  
        drive_base.turn(43) # turn towards M05
        drive_base.straight(180) #drive towards M05
        # increase the turn speed and acceleration settings
        drive_base.settings(turn_rate=202,turn_acceleration=910)                      
        drive_base.turn(87) #turn the base quickly to open the statue

        #---------------------------------
        # M03 - Immersive Experience
        #---------------------------------

        drive_base.straight(140) #move forwards a bit
        drive_base.turn(137) # turn towards M03 direction
        # Define a function to Move forward and raise the front arm simultaneously  
        ####
        async def forward_and_raise_arm():
            await multitask(front_motor.run_angle(400,250),drive_base.straight(400))
        run_task(forward_and_raise_arm())  #move forward while raising the arm up

        drive_base.turn(90)  #turn the front of the robot to M03
        drive_base.straight(15)  #drive forward a little
        front_motor.run_angle(420,-210,Stop.COAST) # push immersive experience down
        wait(50) 
        #front_motor.run_angle(400,210) #lift arm up - removed on 17 Jan for improved reliability

        #---------------------------------
        #Go Home 
        #---------------------------------

        #increase the speed to save time while heading back to home area
        drive_base.settings(straight_speed=600,straight_acceleration=1200)
        drive_base.curve(-600,-110,Stop.COAST) # come back in a curve 
        drive_base.settings(307,1152,202,910) # Reset the speed settings to default