from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task


# Choose a letter.
selected = hub_menu(1,2,3,4,5,6,7)

# Based on the selection, run a program.
if selected == 1:
    import run_1_031223 #Colleact Noah, Museum, Light sound, VR, 3D immersive
elif selected == 2:
    import run_2_031223 
elif selected == 3:
    import run_3_031223
elif selected == 4:
    import run_4_031223
elif selected == 5:
    import run_5_241123
elif selected == 6: 
    import run_6_261123
elif selected == 7: # what happens if someone presses 7 by mistake??
    SystemExit
