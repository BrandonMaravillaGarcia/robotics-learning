import rclpy
from rclpy.node import Node
from lawnmower_msgs.msg import LawnmowerStatus

class LawnmowerSub(Node):
    def __init__(self):
        super().__init__('lawnmower_subscriber')
        self.subscription = self.create_subscription(
            LawnmowerStatus,
            'lawnmower_status',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(
            f"Speed: {msg.speed:.2f} m/s | Battery: {msg.battery:.1f}% | "
            f"Lat: {msg.latitude:.3f} | Lon: {msg.longitude:.3f}"
        )

def main(args = None):
    rclpy.init(args = args)
    node = LawnmowerSub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()