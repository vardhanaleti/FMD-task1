#!/usr/bin/env python

import rospy
from task1.msg import nameandage

def name_and_age():	
	
	pub = rospy.Publisher('topic1',nameandage,queue_size=10)
	rospy.init_node('node1',anonymous = True)
	rate = rospy.Rate(1)
	msg = nameandage()
	k = raw_input("enter your name: ")
	l = raw_input("enter your age: ")
	msg.name = k
	msg.age = int(l)
	
	while not rospy.is_shutdown():
		rospy.loginfo(msg)
		pub.publish(msg)
		rate.sleep()

if __name__=="__main__":
	try:
		name_and_age()
	except rospy.ROSInterruptException : pass
