#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from rclpy.subscription import Subscription
from rclpy.publisher import Publisher
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64MultiArray
import math
class ImuSubscriber(Node):
    def __init__(self):
        super().__init__('imu_subscriber')
        self.subscription = self.create_subscription(
            Imu,
            '/imu_plugin/out',
            self.callback,
            10)
        self.publisher = self.create_publisher(Float64MultiArray, 'imu_eular',10)

    def callback(self, msg):
        # Convert quaternion to roll, pitch, yaw
        quat = (msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w)
        roll, pitch, yaw = self.quaternion_to_euler(quat)

        pub_msg = Float64MultiArray()
        pub_msg.data = [roll, pitch, yaw]
        # Now you can use the roll, pitch, and yaw values
        print("Roll:", roll)
        print("Pitch:", pitch)
        print("Yaw:", yaw)
        self.publisher.publish(pub_msg)

    def quaternion_to_euler(self, quat):
        # Convert quaternion to Euler angles (roll, pitch, yaw)
        w, x, y, z = quat
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        X = math.degrees(math.atan2(t0, t1))
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        Y = math.degrees(math.asin(t2))
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        Z = math.degrees(math.atan2(t3, t4))
        return X, Y, Z

rclpy.init()
node = ImuSubscriber()
rclpy.spin(node)