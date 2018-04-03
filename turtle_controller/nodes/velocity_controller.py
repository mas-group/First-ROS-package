#!/usr/bin/env python

PACKAGE = 'turtle_controller'
NODE = 'velocity_controller'

import rospy
import std_msgs

from geometry_msgs.msg import Twist

class VelocityController:

	def __init__(self):
		# Initialize the node
		rospy.init_node(NODE)

		# Create publisher
		self.target_vel_pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size = 10)

		# Create subscriber for velocity from keyboard
		self.vel_sub = rospy.Subscriber("turtle_controller/cmd_vel", Twist, self.velocity_callback)

		# Create target velocity msg
		self.target_vel = Twist()

	def velocity_callback(self, msg):
		self.target_vel = msg


if __name__ == '__main__':
	n = VelocityController()
	rate = rospy.Rate(1)
	# Read in input
	while not rospy.is_shutdown():
		# Publish message
		n.target_vel_pub.publish(n.target_vel)
		rate.sleep()

