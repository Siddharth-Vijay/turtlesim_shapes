import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class HexagonDrawer(Node):
    def __init__(self):
        super().__init__('hexagon_drawer')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def draw_hexagon(self):
        for i in range(6):
            msg = Twist()
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.publisher.publish(msg)
            time.sleep(1)
            msg.linear.x = 0.0
            msg.angular.z = 1.04
            self.publisher.publish(msg)
            time.sleep(1)

def main(args=None):
    rclpy.init(args=args)
    node = HexagonDrawer()
    node.draw_hexagon()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
