from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(
            package='lidar_slam_robot',
            executable='teleop_controller',
            name='teleop_controller',
            output='screen'
        ),

    ])