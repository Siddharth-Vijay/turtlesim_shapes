from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # First turtlesim node for hexagon
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtle_hexagon',
            output='screen',
            namespace='turtle_hexagon'
        ),
        # Hexagon drawing node
        Node(
            package='turtlesim_shapes',
            executable='hexagon',
            name='hexagon_drawer',
            output='screen',
            remappings=[
                ('/turtle1/cmd_vel', '/turtle_hexagon/turtle1/cmd_vel'),
            ],
        ),
        # Second turtlesim node for 3D
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtle_3d',
            output='screen',
            namespace='turtle_3d'
        ),
        # 3D drawing node
        Node(
            package='turtlesim_shapes',
            executable='3D',
            name='draw_3d',
            output='screen',
            remappings=[
                ('/turtle1/cmd_vel', '/turtle_3d/turtle1/cmd_vel'),
                ('/turtle2/cmd_vel', '/turtle_3d/turtle2/cmd_vel'),
                ('/spawn', '/turtle_3d/spawn'),
                ('/kill', '/turtle_3d/kill'),
            ],
        ),
    ])
