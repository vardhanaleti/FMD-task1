#!/usr/bin/env python

import rospy 
from task1.msg import nameandage
from task1.msg import status

last_data = ""
started = False
pub = rospy.Publisher('topic2',status,queue_size=10)


def callback(data):
	rospy.loginfo("%s is age: %d" % (data.name,data.age))
	global started, last_data
	last_data = data
	if(not started):
		started = True

def timer_callback(event):
	global started,pub,last_data
	msg_2 = status()
	if(started):
		age = last_data.age
		name = last_data.name 
		msg_2 = status()
		if age>=18:
			msg_2.eligibility = "eligible"
		else:
			msg_2.eligibility = "not eligible"
		msg_2.name = name 


	rospy.loginfo(msg_2)
	pub.publish(msg_2)
	


def listener():
	rospy.init_node('node2',anonymous = True)
	rospy.Subscriber("topic1",nameandage,callback)
	timer = rospy.Timer(rospy.Duration(0.5),timer_callback)
	rospy.spin()
	timer.shutdown()


if __name__=='__main__':
	listener()


