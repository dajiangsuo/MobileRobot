#!/usr/bin/python
# licence removed for brevity
import rospy
import threading
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
import sys
import time

import navio.pwm
#from robot_control.navio import pwm
#from robot_control.navio  import util
import navio.util
import datetime

PWM_OUT = 1
Motor_Reverse = 1.60
Motor_Brake = 1.750
Motor_Drag = 1.2
Motor_Max = 2.0
Motor_Min = 1.0
Motor_Neutral = 1.5
pwm = navio.pwm.PWM(PWM_OUT)
Motor_currentSpeed = 0

def motor_speed_loop():
    if Motor_currentSpeed == 0:
	Motor_curentSpeed = Motor_Neutral
    while (True):
	pwm.set_duty_cycle(Motor_currentSpeed)


class velocitySubscriber:

    def __init__(self):
	# Initialize the motor
	#pwm = navio.pwm.PWM(PWM_OUT)
	navio.util.check_apm()
	self.pwm.initialize()
	self.pwm.set_period(50)
	self.pwm.enable()
	#print("Hello World")
	self.loop_for(8,self.pwm.set_duty_cycle,self.Motor_Max)
	self.loop_for(4,self.pwm.set_duty_cycle,self.Motor_Min)
	self.loop_for(5,self.pwm.set_duty_cycle,self.Motor_Neutral)
	print("Motor initialization finished")
	# subscribe to velocity published by navigation node
    	rospy.Subscriber("/MobileRobot/velocity",Float32,self.callback)

    def loop_for(self,seconds,func,*args):
	#print("Within loop_for")
	#print(seconds)
	#print("Hello Word")
	endTime = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
	#print("get endTime")
	while True:
	   if datetime.datetime.now() >= endTime:
	       break
	   func(*args)


    def callback(self,velocity):
	self.Motor_currentSpeed = 1.3

    def motor_speed_loop(self):
	if self.Motor_currentSpeed == 0:
	    self.Motor_currentSpeed = self.Motor_Neutral
	while (True):
	    self.pwm.set_duty_cycle(self.Motor_currentSpeed)

if __name__=='__main__':

    rospy.init_node("velocity_subscriber_node")

    motorSpeed_thread = threading.Thread(target = motor_speed_loop)
    motorSpeed_thread.start()

    node = velocitySubscriber()

    rospy.spin()
	
    
