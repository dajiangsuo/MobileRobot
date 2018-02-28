#!/usr/bin/python
# licence removed for brevity
import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
import sys
import time

import navio.pwm
#from robot_control.navio import pwm
#from robot_control.navio  import util
import navio.util
import datetime

navio.util.check_apm()

PWM_OUT = 2
Motor_Reverse = 1.60
Motor_Brake = 1.750
Motor_Drag = 1.2
Motor_Max = 2.0
Motor_min = 1.0
Motor_Neutral = 1.5

def loop_for(seconds, func, *args):
    endTime = datetime.datetime.now() + datetime.timedelta(seconds=seconds)

    while True: 
	if datetime.datetime.now() >= endTime:
	    break
	func(*args)

def callback(data):
    pwm.set_duty_cycle()

def listener():

    with navio.pwm.PWM(PWM_OUT) as pwm:
        pwm.initialize()
        self.pwm.set_period(50)
        self.pwm.enable()
        #print("Hello World")
        loop_for(8,pwm.set_duty_cycle,Motor_Max)
        loop_for(4,pwm.set_duty_cycle,Motor_Min)
        loop_for(5,pwm.set_duty_cycle,Motor_Neutral)
	
	rospy.init_node('listener',anonymous=True)
	# subscribe to velocity published by navigation node
	rospy.Subscriber("/MobileRobot/velocity",Float32,callback)

  
if __name__=='__main__':

    #rospy.init_node("velocity_subscriber_node")

    listener()
