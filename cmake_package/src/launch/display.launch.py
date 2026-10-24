from launch_ros.actions import Node
from launch import LaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution, Command
from launch_ros.descriptions import ParameterValue
import os


def generate_launch_description():

    day_7_description = FindPackageShare('day_7_description')
    path_to_urdf = PathJoinSubstitution([day_7_description, 'urdf', 'day_7_bot.urdf.xacro'])
    robot_description = ParameterValue(Command(['xacro ', path_to_urdf]), value_type=str)
    rviz_config = PathJoinSubstitution([day_7_description, 'rviz', 'default.rviz'])

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
