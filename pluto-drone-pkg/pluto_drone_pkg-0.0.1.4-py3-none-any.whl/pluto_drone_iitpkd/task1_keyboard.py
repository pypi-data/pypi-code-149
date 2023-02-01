from plutodrone import *
import keyboard
import time

class pluto_control():
    
    def __init__(self):        
        self.quadCopter=plutodrone("192.168.4.1", 23)
        # self.quadCopter.arm()
        
        self.quadCopter.roll = 1500
        self.quadCopter.pitch = 1500
        self.quadCopter.throttle = 1000
        self.quadCopter.yaw = 1500
        self.flag_takeoff=0
        self.flag_arm = 0

    def key_cmd(self):
        # print('ok')
        if keyboard.is_pressed('v'): #v
            if self.flag_arm == 0:
                print('arm')
                self.quadCopter.arm()
                self.flag_arm =1
            else:
                print('armed')
        
        elif keyboard.is_pressed('b'): #b
            if self.flag_arm == 1:
                print('disarm')
                self.quadCopter.disarm()
                self.flag_arm = 0
            else:
                print('disarmed')

        elif keyboard.is_pressed('w'): #w
            print('increase height')
            self.quadCopter.throttle = 1800
            self.quadCopter.setcmd(0.02)

        elif keyboard.is_pressed('s'): #s
            print('decrease height')
            self.quadCopter.throttle = 1400
            self.quadCopter.setcmd(0.02)

        elif keyboard.is_pressed('l'): #l
            print('roll right')
            self.quadCopter.roll = 1600
            self.quadCopter.setcmd(0.02)

        elif keyboard.is_pressed('j'): #j
            print('roll left')
            self.quadCopter.roll = 1400
            self.quadCopter.setcmd(0.02)

        elif keyboard.is_pressed('i'): #i
            print('pitch front')
            self.quadCopter.pitch = 1600
            self.quadCopter.setcmd(0.02)

        elif keyboard.is_pressed('k'): #k
            print('pitch back')
            self.quadCopter.pitch = 1400
            self.quadCopter.setcmd(0.02)

        elif keyboard.is_pressed('d'): #d
            print('yaw clockwise')
            self.quadCopter.yaw = 1800
            self.quadCopter.setcmd(0.02)

        elif keyboard.is_pressed('a'): #a
            print('yaw anticlockwise')
            self.quadCopter.yaw = 1200
            self.quadCopter.setcmd(0.02)

        elif keyboard.is_pressed('t'): #t

            if self.flag_takeoff==0:
                print('takeoff')
                self.quadCopter.takeoff()
                self.flag_takeoff = 1

        elif keyboard.is_pressed('y'): #y
            if self.flag_takeoff == 1:
                print('land')
                self.quadCopter.land()
                self.flag_takeoff = 0

        else:
            self.quadCopter.roll = 1500
            self.quadCopter.pitch = 1500
            self.quadCopter.throttle = 1500
            self.quadCopter.yaw = 1500
            self.quadCopter.setcmd(0.02)

        



        #key map

        

        
    # def sequence(self):
        
    #     try:
    #         # self.quadCopter.arm()
    #         self.quadCopter.takeoff()
    #         # self.quadCopter.disarm()
    #         self.quadCopter.throttle = 1700
    #         self.quadCopter.setcmd(3)
    #         self.quadCopter.land_msp()
    #         # self.quadCopter.box_takeoff()
    #         # self.quadCopter.throttle = 1530
    #         # self.quadCopter.setcmd(1)
    # #         self.quadCopter.throttle=1000
    # #         self.quadCopter.setcmd(0.1)

    # #         self.quadCopter.takeoff()
            
    # #         # pitch forward
    # #         print("PITCH FRONT")
    # #         self.quadCopter.pitch = 1600
    # #         period = 1
    # #         self.quadCopter.setcmd(period)
            
            
    # #         # counter Pitch
    # #         print("COUNTER PITCH")
    # #         self.quadCopter.pitch = 1300
    # #         period = 0.3
    # #         self.quadCopter.setcmd(period)
            

    # #         #Reset Pitch
    # #         self.quadCopter.pitch=1500

    # #         # Roll
    # #         print("ROLL RIGHT")
    # #         self.quadCopter.roll =1600 
    # #         period = 1
    # #         self.quadCopter.setcmd(period)
            
            
    # #         # Counter Roll
    # #         print("COUNTER ROLL")
    # #         self.quadCopter.roll = 1300
    # #         period = 0.3
    # #         self.quadCopter.setcmd(period)
            
            
    # #         #Reset Roll
    # #         self.quadCopter.roll=1500

    # #         # Pitch backward
    # #         print("PITCH BACK")
    # #         self.quadCopter.pitch = 1400
    # #         period = 1
    # #         self.quadCopter.setcmd(period)
            
            
    # #         # Counter pitch
    # #         print("COUNTER PITCH")
    # #         self.quadCopter.pitch = 1700
    # #         period = 0.2
    # #         self.quadCopter.setcmd(period)
            

    # #         #Reset Pitch
    # #         self.quadCopter.pitch=1500

    # #         # Roll
    # #         print("ROLL LEFT")
    # #         self.quadCopter.roll =1400 
    # #         period = 1
    # #         self.quadCopter.setcmd(period)
            
            
    # #         # Counter roll
    # #         print("COUNTER ROLL")
    # #         self.quadCopter.roll = 1700
    # #         period = 0.2
    # #         self.quadCopter.setcmd(period)
            

    # #         #Reset Roll
    # #         self.quadCopter.roll=1500
        
    # #         self.quadCopter.throttle=1500
    # #         # Yaw
    # #         print("YAW CLOCKWISE")
    # #         self.quadCopter.yaw =1800
    # #         period = 1
    # #         self.quadCopter.setcmd(period)
            

    # #         # Yaw to zero
    # #         self.quadCopter.yaw=1500
    # #         period = 0.5
    # #         self.quadCopter.setcmd(period)


    # #         # Counter Yaw
    # #         print("YAW ANTI-CLOCKWISE")
    # #         self.quadCopter.yaw =1200
    # #         period = 1
    # #         self.quadCopter.setcmd(period)
            

    # #         # Yaw to zero
    # #         self.quadCopter.yaw=1500
    # #         period = 0.5
    # #         self.quadCopter.setcmd(period)


    # #         #land
    # #         self.quadCopter.land()
            
    # #         #disarm and disconnect
    # #         self.quadCopter.disarm()
    # #         self.quadCopter.disconnect()

    #     except KeyboardInterrupt:
    #         self.quadCopter.disarm()
    #         self.quadCopter.disconnect()
        
def keyboard_drone():
    drone = pluto_control()
    # drone.sequence()
    # drone.quadCopter.disarm()
    # drone.quadCopter.disconnect()
    while 1:
        drone.key_cmd()
        # time.sleep(0.02)