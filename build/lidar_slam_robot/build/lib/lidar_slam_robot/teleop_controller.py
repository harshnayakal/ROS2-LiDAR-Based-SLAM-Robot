#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TeleopController(Node):

    def __init__(self):
        super().__init__('teleop_controller')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.move_robot
        )

        self.get_logger().info("Teleop Controller Started")

    def move_robot(self):

        msg = Twist()

        msg.linear.x = 0.2
        msg.angular.z = 0.0

        self.publisher.publish(msg)

        self.get_logger().info("Moving Forward")


def main(args=None):

    rclpy.init(args=args)

    node = TeleopController()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()