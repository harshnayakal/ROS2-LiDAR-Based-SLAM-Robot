#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class ObstacleAvoidance(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.get_logger().info("Obstacle Avoidance Node Started")

    def scan_callback(self, msg):

        twist = Twist()

        # Front distance
        front = min(msg.ranges[0:20] + msg.ranges[-20:])

        if front < 0.6:

            self.get_logger().info("Obstacle Detected")

            twist.linear.x = 0.0
            twist.angular.z = 0.5

        else:

            self.get_logger().info("Moving Forward")

            twist.linear.x = 0.2
            twist.angular.z = 0.0

        self.publisher.publish(twist)


def main(args=None):

    rclpy.init(args=args)

    node = ObstacleAvoidance()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()