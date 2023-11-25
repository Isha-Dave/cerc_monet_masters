from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task


# Choose a letter.
selected = hub_menu(1,2,3,4,5,6,7,8,9,10)

# Based on the selection, run a program.
if selected == 1:
    import run_1_241123 #Colleact Noah, Museum, Light sound, VR, 3D immersive
elif selected == 2:
    import run_2_241123 #
elif selected == 3:
    import run_3_241123
elif selected == 4:
    import run_4_241123
elif selected == 5:
    import run_5_241123
elif selected == 6: 
    import run_6_241123
elif selected == 7: 
    import run_7_241123
elif selected == 8:
    SystemExit