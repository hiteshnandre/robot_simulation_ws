from launch import LaunchDescription
from  launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_path
import os

def generate_launch_description():
    ld = LaunchDescription()
    # Get the paths of required files
    urdf_path = os.path.join(get_package_share_path('robot_description'), 'urdf', 'main.urdf.xacro')
    
    # gazebo_node_path = os.path.join(get_package_share_path('gazebo_ros'), 'launch', 'gazebo.launch.py')
    
    # save the config_first and then uncomment the following line for not setting up again and again
    # rviz_config_path = os.path.join(get_package_share_path('jarvis_bringup'), 'rviz', 'robot.rviz')
    
    robot_description = ParameterValue(Command(
        ['xacro ', urdf_path]), value_type=str)
    
    # Nodes
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description':robot_description}]
    )
    
    gazebo_node = Node(
        package="gazebo_ros",
        executable="gazebo.launch.py",
        output="screen",
        parameters=[{'useSimTime': ParameterValue(True, value_type=bool)}],
        arguments=['-d', gazebo_node]
    )
    
    robot_spawn_node = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        output="screen",
        parameters=[{'topic': 'robot_description', 'entity':"robo"}]
    )
    
    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )
    
    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        output="screen"
        # arguments=['-d', os.path.join(get_package_share_path('robot_description'), 'rviz', 'robo.rviz')]
        # arguments=["robot.rviz"]
        # arguments=['-d', rviz_config_path]
    )
    
    ld.add_action(robot_state_publisher_node)
    ld.add_action(gazebo_node)
    ld.add_action(robot_spawn_node)
    ld.add_action(rviz2_node)
    ld.add_action(joint_state_publisher_gui_node)
    return ld