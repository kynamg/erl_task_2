#! /usr/bin/env python
#Title: erl_task_2.py
#Author: Kyna Mowat-Gosnell
#Date: 14/8/17

import qi
import sys
import os
import time
import argparse
import naoqi
from naoqi import *
from diagnostic_msgs.msg import KeyValue # this is the message type /iot_updates uses
from std_msgs.msg import Empty


def callback(data):
	print("in callback")
	animatedProxy.say("Someone is at the door")

def devices_callback(data):
    if(data.key == "Hall_Intcm" and data.value == "ON"):
        bell_ring()

def bell_ring():
    animatedProxy.say("There is someone at the door")

    def listener():
        rospy.init_node('bell_listener', anonymous=True) #initialise node to subscribe to topic /iot_updates
        rospy.Subscriber("/devices/bell", Empty, callback)
        rospy.Subscriber("/iot_updates", KeyValue, devices_callback) # subscribe to topic /iot_updates
        rospy.spin() #stops exiting until node is stopped

if __name__ == '__main__':
    from naoqi import ALProxy
    broker = ALBroker("pepperBroker", "192.168.1.129", 9999, "pepper.local", 9559) #local broker connected to remote naoqi

    listener()
