#!/usr/bin/env python

PACKAGE = 'turtle_controller'
NODE = 'velocity_client'

import rospy
import std_msgs

from geometry_msgs.msg import Twist

class VelocityClient:

	def __init__(self):
		# Initialize the node
		rospy.init_node(NODE)

		# Create publisher
		self.target_vel_pub = rospy.Publisher("turtle_controller/cmd_vel", Twist, queue_size = 10)

		# Create target velocity msg
		self.target_vel = Twist()


	def read_input(self):
		try:
			self.target_vel.linear.x = float(raw_input("Enter velocity x: "))
		except ValueError:
			self.target_vel.linear.x = 0.0
		try:
			self.target_vel.angular.z = float(raw_input("Enter angular velocity: "))
		except ValueError:
			self.target_vel.angular.z = 0.0


if __name__ == '__main__':
	n = VelocityClient()
	rate = rospy.Rate(1)
	# Read in input
	while not rospy.is_shutdown():
		n.read_input()
		# Publish message
		n.target_vel_pub.publish(n.target_vel)
		rate.sleep()

