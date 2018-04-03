#!/usr/bin/env python

PACKAGE = 'turtle_controller'
NODE = 'pose_controller'

import rospy
import std_msgs

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class PoseController:

	def __init__(self):
		# Initialize the node
		rospy.init_node(NODE)

		# Create publisher
		self.target_vel_pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size = 10)

		# Create current and target pose
		self.current_pose = Pose()
		self.target_pose = Pose()

		# Create velocity
		self.target_vel = Twist()

		# Create subscriber for pose from turtle
		self.vel_sub = rospy.Subscriber("turtle1/pose", Pose, self.current_pose_callback)

		# Create subscriber for pose from keyboard
		self.vel_sub = rospy.Subscriber("turtle_controller/pose", Pose, self.target_pose_callback)

		# Create publisher for velocity
		self.target_vel_pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size = 10)

	def current_pose_callback(self, msg):
		# Your code here
		pass

	def target_pose_callback(self, msg):
		# Your code here
		pass

	def calculate_velocity(self):
		# Your code here
		pass

if __name__ == '__main__':
	n = PoseController()
	rate = rospy.Rate(1)
	# Read in input
	while not rospy.is_shutdown():
		# Publish message
		n.target_vel_pub.publish(n.target_vel)
		rate.sleep()