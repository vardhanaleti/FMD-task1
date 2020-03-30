#!/usr/bin/env python

import rospy
from task1.msg import status 

def callback(data):
	rospy.loginfo("person %s is %s",data.name,data.eligibility)

def listener():
	rospy.init_node('node3',anonymous = True)
	rospy.Subscriber("topic2",status,callback)
	rospy.spin()

if __name__=='__main__':
	listener()
