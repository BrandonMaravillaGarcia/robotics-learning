from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package = 'my_robot',
            executable = 'lawnmower_publisher',
            name = 'lawnmower_publisher'
        ),

        Node(
            package = 'my_robot',
            executable = 'lawnmower_subscriber',
            name = 'lawnmower_subscriber'
        ),
    ])
