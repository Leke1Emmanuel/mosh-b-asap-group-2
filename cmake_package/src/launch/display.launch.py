from launch_ros.actions import Node
from launch import LaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution, Command
from launch_ros.descriptions import ParameterValue
import os


def generate_launch_description():

    package_share = FindPackageShare('cmake_package')
    path_to_urdf = PathJoinSubstitution([package_share, 'urdf', 'day_7_bot.urdf.xacro'])
    robot_description = ParameterValue(Command(['xacro ', path_to_urdf]), value_type=str)
    rviz_config = PathJoinSubstitution([package_share, 'rviz', 'default.rviz'])

    robot_state_publisher_node = Node(
        package="robot_state_publisher", 
        executable="robot_state_publisher",
        parameters=[{'robot_description': robot_description}]
        )

    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"

    )

    rviz_node = Node(
        package="rviz2", 
        executable="rviz2", 
        arguments=['-d', rviz_config]
    )
    
    return LaunchDescription([
        robot_state_publisher_node, 
        joint_state_publisher_gui_node, 
        rviz_node
        ])
