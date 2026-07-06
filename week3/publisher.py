import rclpy
from rclpy.node import Node
from lawnmower_msgs.msg import LawnmowerStatus

class LawnmowerPublisher(Node):
    def __init__(self):
        super().__init__('lawnmower_publisher')
        self.publisher_ = self.create_publisher(LawnmowerStatus, 'lawnmower_status', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.speed = 0.0

    def timer_callback(self):
        msg = LawnmowerStatus()
        msg.speed = self.speed
        msg.battery = 85.0
        msg.latitude = 39.123
        msg.longitude = -75.456
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.speed:.2f} m/s")
        self.speed += 0.1

def main(args = None):
    rclpy.init(args = args)
    node = LawnmowerPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()