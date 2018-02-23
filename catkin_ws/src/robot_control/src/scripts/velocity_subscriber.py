#!/usr/bin/python
# licence removed for brevity
import rospy
from std_msg.msg import Float32
from geometry_msgs.msg import Twist
import sys
import time

import navio.pwm
import navio.util
import datetime



class velocitySubscriber:
    PWM_OUT = 2
    Motor_Reverse = 1.60
    Motor_Brake = 1.750
    Motor_Drag = 1.2
    Motor_Max = 2.0
    Motor_min = 1.0
    Motor_Neutral = 1.5
    pwm = navio.pwm.PWM(PWM_OUT)

    def __init__(self):
	# Initialize the motor
	#pwm = navio.pwm.PWM(PWM_OUT)
	self.pwm.initialize()
	self.pwm.set_period(50)
	self.pwm.enable()
	loop_for(8,self.pwm.set_duty_cycle,self.Motor_Max)
	loop_for(4,self.pwm.set_duty_cycle,self.Motor_Min)
	loop_for(5,self.pwm.set_duty_cycle,self.Motor_Neutral)
	
	# subscribe to velocity published by navigation node
    	rospy.Subscriber("/MobileRobot/velocity",Float32,self.callback)

    def loop_for(seconds,func,*args):
	endTime = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
	
	while True:
	  if datetime.datetime.now() >= endTime:
	     braek
	  func(*args)


    def callback(self,velocity)
	self.pwm.set_duty_cycle(velocity)

if __name__=='__main__':

    rospy_init_node("velocity_subscriber_node")

    node = velocitySubscriber()

    rospy.spin()
	
	
	
