from pose_est import camera_pose
from plutodrone import *
# from rectangular_trajectory import rect_trajectory
import numpy as np
# import csv
# import math


class quadControl():

    def __init__(self):

        # initiate connection and arm the drone
        self.quadCopter = plutodrone()
        self.quadCopter.arm()
        # self.quadCopter.throttle = 1000
        # self.quadCopter.setcmd(0.02)

        # takeoff and hover
        # self.quadCopter.takeoff()

        # current pos sense initialization
        self.curr_pos_x = 0
        self.curr_pos_y = 0
        self.curr_pos_z = 0
        self.curr_vel_x = 0
        self.curr_vel_y = 0
        self.curr_vel_z = 0

        self.position_array = np.zeros(3)
        self.vel_array = np.zeros(3)
        self.pos = camera_pose()
        self.prev_position_array = self.pos.getPose()

        # initial position (same as the initial position detected by camera)
        self.init_pos_x = self.prev_position_array[0]
        self.init_pos_y = self.prev_position_array[1]
        self.init_pos_z = self.prev_position_array[2]

        # desired position
        self.x_desired = np.round(self.init_pos_x, 2)
        self.y_desired = np.round(self.init_pos_y, 2)
        self.z_desired = np.round(self.init_pos_z, 2) - 0.5

        # desired velocity
        self.xvel_desired = 0
        self.yvel_desired = 0
        self.zvel_desired = 0

        # error
        self.err_x = 0
        self.err_y = 0
        self.err_z = 0
        self.err_ix = 0
        self.err_iy = 0
        self.err_iz = 0


        self.kpz = 500
        self.kdz = 40
        self.kiz = 0.00

        # self.kpz = 100
        # self.kdz = 0
        # self.kiz = 0.001

        self.kppitch = 200 #250
        self.kdpitch = 90
        self.kipitch = 0.001

        self.kproll = 200
        self.kdroll = 90
        self.kiroll = 0.001

        # saturation
        self.pitch_sat_high = 1600
        self.pitch_sat_low = 1400
        self.roll_sat_high = 1600
        self.roll_sat_low = 1400
        self.throttle_sat_high = 2100
        self.throttle_sat_low = 1000

        # update frequency 
        self.freq = 40

        # moving average filter
        self.filter_size = 5
        self.x_array = np.zeros(self.filter_size)
        self.y_array = np.zeros(self.filter_size)
        self.z_array = np.zeros(self.filter_size)
        self.t = 0
        
        # maximums
        self.mathrottle=0

        self.disarmFlag = 0

        #data logging
        # self.velx_log = np.array([])
        # self.vely_log = np.array([])
        # self.velz_log = np.array([])
        file = open('pose_data_log.csv', 'w')
        # writer = csv.writer(file)
        file.write('x,y,z,xvel,yvel,zvel')
        file.close()

    def posControl(self,x,y,xvel,yvel,disarm):

        if disarm:
            self.quadCopter.land()
            self.quadCopter.disarm()
            self.quadCopter.disconnect()
            return 

        self.getCurrentPose()
        self.curr_pos_x = self.position_array[0]
        self.curr_pos_y = self.position_array[1]
        self.curr_vel_x = self.vel_array[0]
        self.curr_vel_y = self.vel_array[1]
        self.curr_pos_z = self.position_array[2]
        self.curr_vel_z = self.vel_array[2]

        self.x_desired = x
        self.y_desired = y
        self.xvel_desired = xvel
        self.yvel_desired = yvel
        self.disarmFlag = disarm


        # PID control algo goes here
        self.err_x = self.x_desired - self.curr_pos_x
        self.err_y = self.y_desired - self.curr_pos_y
        self.err_z = self.z_desired - self.curr_pos_z
        self.err_vx = self.xvel_desired - self.curr_vel_x
        self.err_vy = self.yvel_desired - self.curr_vel_y
        self.err_vz = self.zvel_desired - self.curr_vel_z
        self.err_ix += self.err_x
        self.err_iy += self.err_y
        self.err_iz += self.err_z

        # control allocation
        pitch_des = int(1500 +( self.kppitch*self.err_x + self.kdpitch*self.err_vx + self.kipitch*self.err_ix))
        roll_des = int(1500 + (self.kproll*self.err_y + self.kdroll*self.err_vy + self.kiroll*self.err_iy))
        throttle_des = int(1575 - (self.kpz*self.err_z + self.kdz*self.err_vz + self.kiz*self.err_iz)) #z decreases in up direction


        # pitch_des=1500
        # roll_des=1500

        if pitch_des > self.pitch_sat_high:
            pitch_des = self.pitch_sat_high
        elif pitch_des < self.pitch_sat_low:
            pitch_des = self.pitch_sat_low

        if roll_des > self.roll_sat_high:
            roll_des = self.roll_sat_high
        elif roll_des < self.roll_sat_low:
            roll_des = self.roll_sat_low

        if throttle_des > self.throttle_sat_high:
            throttle_des = self.throttle_sat_high
        elif throttle_des < self.throttle_sat_low:
            throttle_des = self.throttle_sat_low

        self.quadCopter.pitch = pitch_des
        self.quadCopter.roll = roll_des
        self.quadCopter.throttle = throttle_des

        # print('sending', self.quadCopter.throttle, self.quadCopter.pitch,self.quadCopter.roll)
        # self.quadCopter.pitch = 1500
        # self.quadCopter.roll = 1500
        
        if self.quadCopter.throttle >self.mathrottle:
            self.mathrottle=self.quadCopter.throttle

        # send the command
        self.quadCopter.setcmd(1/self.freq)

        # update frequency
        self.t += 1/self.freq

    def getCurrentPose(self):

        self.position_array = self.pos.getPose()

        #moving average filter
        self.x_array[0:-1] = self.x_array[1:]
        self.x_array[-1] = self.position_array[0]
        self.position_array[0] = np.mean(self.x_array)

        self.y_array[0:-1] = self.y_array[1:]
        self.y_array[-1] = self.position_array[1]
        self.position_array[1] = np.mean(self.y_array)

        self.z_array[0:-1] = self.z_array[1:]
        self.z_array[-1] = self.position_array[2]
        self.position_array[2] = np.mean(self.z_array)

        self.vel_array = -(self.prev_position_array - self.position_array)*self.freq

        self.prev_position_array[:] = self.position_array

        #logging
        file = open('pose_data_log.csv', 'a')
        # writer = csv.writer(file)
        file.write('\n'+str(self.position_array[0])+','+str(self.position_array[1])+','+str(self.position_array[2])+','+str(self.vel_array[0])+','+str(self.vel_array[1])+','+str(self.vel_array[2]))
        file.close()






# if __name__ == '__main__':
#     quad = quadControl()

#     while 1:
#         try:
#             quad.posControl()
#             # if quad.err_x < 0.05 and quad.err_y < 0.05 and quad.err_z < 0.05:
#             #     print('DONE!!!!')
#             if quad.disarmFlag == 1:
#                 quad.quadCopter.land()
#                 break


#         except KeyboardInterrupt:
#             print(quad.mathrottle)
#             quad.quadCopter.land()
#             # print(quad.init_pos_z)
#             # while abs(quad.self.curr_pos_z-quad.init_pos_z)>=0.05:
#             #     quad.quadCopter.throttle=1500
#             #     quad.quadCopter.setcmd(1/quad.freq)
#             # quad.z_desired=quad.init_pos_z+0.05
#             # err_z = abs(quad.self.curr_pos_z - quad.init_pos_z)

#             # while err_z >=0.05:
#             #     quad.posControl()
#             #     err_z = abs(quad.err_z)
#             #     # print("while")
            
#             break

#     quad.quadCopter.disarm()
#     quad.quadCopter.disconnect()
            