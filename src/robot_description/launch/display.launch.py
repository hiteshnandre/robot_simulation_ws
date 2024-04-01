from launch import LaunchDescription
from  launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_path
import os

def generate_launch_description():
    # Get the paths of required files
    urdf_path = os.path.join(get_package_share_path('robot_description'), 'urdf', 'main.urdf.xacro')
    
    # save the config_first and then uncomment the following line for not setting up again and again
    # rviz_config_path = os.path.join(get_package_share_path('jarvis_description'), 'rviz', 'demo_robot.rviz')
    
    robot_description = ParameterValue(Command(
        ['xacro ', urdf_path]), value_type=str)
    
    # Nodes
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description':robot_description}]
    )
    
    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )
    
    rviz2_node = Node(
        package="rviz2",
        executable="rviz2"
        # arguments=["demo_robot.rviz"]
        # arguments=['-d', rviz_config_path]  
    )
    
    return LaunchDescription(
        [
            robot_state_publisher_node,
            joint_state_publisher_gui_node,
            rviz2_node
        ]
    )