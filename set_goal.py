#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# callbacks defination

def active_cb(extra):
	rospy.loginfo("Goal pose being processed")

def feedback_cb(feedback):
	rospy.loginfo("current location: "+str(feedback))

def done_cb(status, result):
	if status == 3:
		rospy.loginfo("Goal reached")
	if status == 2 or status == 8:
		rospy.loginfo("Goal cancelled")
	if status == 4:
		rospy.loginfo("Goal aborted/goal is not found")

rospy.init_node('send_goal')

navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
navclient.wait_for_server()

# Example of navigation goal
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"
goal.target_pose.header.stamp = rospy.Time.now()

x1=[0.5,-1,-1.3,2,1.5,1.1]
y1=[0.5,1,1.2,-1.5,-2,1.1]

for i in range(6):
	goal.target_pose.pose.position.x = x1[i]
	goal.target_pose.pose.position.y = y1[i]
	goal.target_pose.pose.position.z = 0.0
	goal.target_pose.pose.orientation.x = 0.0
	goal.target_pose.pose.orientation.y = 0.0
	goal.target_pose.pose.orientation.z = 0.662
	goal.target_pose.pose.orientation.w = 0.750
	navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
	finished = navclient.wait_for_result()


	if not finished:
		rospy.logerr("Action server not avaliable")
	else:
		rospy.loginfo( navclient.get_result())
	i=i+1	








