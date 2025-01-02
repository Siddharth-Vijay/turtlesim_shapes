import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn, Kill
from geometry_msgs.msg import Twist
import time

class Draw3D(Node):
    def __init__(self):
        super().__init__('draw_3d')
        self.spawn_client = self.create_client(Spawn, '/spawn')
        self.kill_client = self.create_client(Kill, '/kill')
        self.pub_turtle1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pub_turtle2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)

        self.call_service(self.kill_client, Kill.Request(name = 'turtle1'))
        self.draw_3()
        self.draw_D()

    def call_service(self, client, request):
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(f'Waiting for {client.srv_name} service...')
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

    def draw_3(self):
        self.call_service(self.spawn_client, Spawn.Request(x=3.0, y=4.25, theta=-1.57, name='turtle1'))

        movements = [
            (5.0, 4.71),
            (0.0, -3.14),
            (5.0, 4.71),
        ]

        for linear_vel, angular_vel in movements:
            twist = Twist()
            twist.linear.x = linear_vel
            twist.angular.z = angular_vel
            self.pub_turtle1.publish(twist)
            time.sleep(1)

    def draw_D(self):
        self.call_service(self.spawn_client, Spawn.Request(x=8.0, y=3.0, name='turtle2'))

        movements = [
            (7.85, 3.14),
            (0.0, 1.57),
            (5.0, 0.0),
        ]

        for linear_vel, angular_vel in movements:
            twist = Twist()
            twist.linear.x = linear_vel
            twist.angular.z = angular_vel
            self.pub_turtle2.publish(twist)
            time.sleep(1)

def main(args=None):
    rclpy.init(args=args)
    node = Draw3D()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()