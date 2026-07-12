import rclpy
from rclpy.node import Node
from lawnmower_msgs.msg import LawnmowerStatus
from lawnmower_msgs.srv import GetStatus

class LawnmowerPublisher(Node):
    def __init__(self):
        super().__init__('lawnmower_publisher')
        self.declare_parameter('publish_rate', 1.0)
        self.publisher_ = self.create_publisher(LawnmowerStatus, 'lawnmower_status', 10)
        publish_rate = self.get_parameter('publish_rate').value
        self.timer = self.create_timer(publish_rate, self.timer_callback)
        self.speed = 0.0
        self.service = self.create_service(GetStatus, 'get_lawnmower_status', self.handle_get_status)

    def timer_callback(self):
        msg = LawnmowerStatus()
        msg.speed = self.speed
        msg.battery = 85.0
        msg.latitude = 39.123
        msg.longitude = -75.456
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.speed:.2f} m/s")
        self.speed += 0.1
    
    def handle_get_status(self, request, response):
        response.speed = self.speed
        response.battery = 85.0
        response.latitude = 39.123
        response.longitude = -75.456
        return response

def main(args = None):
    rclpy.init(args = args)
    node = LawnmowerPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()