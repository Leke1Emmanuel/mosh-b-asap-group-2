# Spawn mosh_b in Gazebo. Target: ROS 2 Lyrical · Gazebo Jetty.
import os

from launch import LaunchDescription
from launch.actions import AppendEnvironmentVariable, DeclareLaunchArgument, IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory

PACKAGE = 'mosh_b_description'
ROBOT = 'mosh_b'


def generate_launch_description():
    share = get_package_share_directory(PACKAGE)
    xacro_file = os.path.join(share, 'urdf', ROBOT + '.urdf')
    robot_description = ParameterValue(Command(['xacro ', xacro_file]), value_type=str)
    x, y, z = LaunchConfiguration('x'), LaunchConfiguration('y'), LaunchConfiguration('z')

    rsp = Node(package='robot_state_publisher', executable='robot_state_publisher', output='screen',
               parameters=[{'robot_description': robot_description, 'use_sim_time': True}])

    world = PathJoinSubstitution([share, 'worlds', LaunchConfiguration('world')])
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [PathJoinSubstitution([FindPackageShare('ros_gz_sim'), 'launch', 'gz_sim.launch.py'])]),
        launch_arguments={'gz_args': ['-r ', world]}.items())
    spawn = Node(package='ros_gz_sim', executable='create', output='screen',
                 arguments=['-topic', 'robot_description', '-name', ROBOT, '-x', x, '-y', y, '-z', z])
    bridge = Node(package='ros_gz_bridge', executable='parameter_bridge', output='screen',
                  parameters=[{'config_file': os.path.join(share, 'config', 'gz_bridge.yaml'),
                               'use_sim_time': True}])
    actions = [
        DeclareLaunchArgument('world', default_value='empty.sdf',
                              description='World file name in worlds/: empty, room, maze, office, tb3_sandbox, depot or warehouse (.sdf)'),
        DeclareLaunchArgument('x', default_value='0'),
        DeclareLaunchArgument('y', default_value='0'),
        DeclareLaunchArgument('z', default_value='0.1'),
        AppendEnvironmentVariable('GZ_SIM_RESOURCE_PATH', os.path.dirname(share)),
        rsp, gazebo, spawn, bridge,
    ]
    return LaunchDescription(actions)
