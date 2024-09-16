#!/usr/bin/env python3

import rclpy
from rclpy.duration import Duration
from rclpy.action import ActionClient
from rclpy.node import Node
from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint


class TrajectoryActionClient(Node):

	def __init__(self):

		super().__init__('points_publisher_node_action_client')
		self.action_client = ActionClient (self, FollowJointTrajectory, '/joint_trajectory_controller/follow_joint_trajectory')
		JointTrajectoryPoint.effort.setter(0.5)
	def send_goal(self):

		points = []
#Turn 180 = pi
#Left up = +ve
#Rear Left up = -ve
#Right up = -ve
#Rear Right up = +ve

		point1_msg = JointTrajectoryPoint()
		# point1_msg.positions = [0.0, 0.0,0.0,-0.0]
		point1_msg.positions = [3.141,-3.141,-3.141,3.141]

		# point1_msg.positions = [-0.8,0.8,1.8,-1.8]


		# point1_msg.positions = [-0.8,0.8,1.0,-1.0]

		point1_msg.time_from_start = Duration(seconds=2.0).to_msg()

		point2_msg = JointTrajectoryPoint()
		point2_msg.positions = [0.0, 0.0, 0.8]
		point2_msg.time_from_start = Duration(seconds=2.0, nanoseconds=0).to_msg()


		points.append(point1_msg)

		joint_names = ['left_flipper_joint', 'right_flipper_joint', 'rear_left_flipper_joint', 'rear_right_flipper_joint']
		goal_msg = FollowJointTrajectory.Goal()
		goal_msg.goal_time_tolerance = Duration(seconds=1, nanoseconds=0).to_msg()
		goal_msg.trajectory.joint_names = joint_names
		goal_msg.trajectory.points = points

		self.action_client.wait_for_server()
		self.send_goal_future = self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
		self.send_goal_future.add_done_callback(self.goal_response_callback)

	
	def goal_response_callback(self, future):
		
		goal_handle = future.result()

		if not goal_handle.accepted:
			self.get_logger().info('Goal rejected ')
			return

		self.get_logger().info('Goal accepted')

		self.get_result_future= goal_handle.get_result_async()
		self.get_result_future.add_done_callback(self.get_result_callback)

	def get_result_callback (self, future):
		
		result = future.result().result
		self.get_logger().info('Result: '+str(result))
		rclpy.shutdown()

		
	def feedback_callback(self, feedback_msg):
		feedback = feedback_msg.feedback


def main(args=None):

	rclpy.init()
	
	action_client = TrajectoryActionClient()
	future = action_client.send_goal()
	rclpy.spin(action_client)

if __name__ == '__main__':
	main()
