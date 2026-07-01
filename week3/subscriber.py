import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LawnmowerSub(Node):
    def __init__(self):
        super().__init__('lawnmower_subscriber')
        self.subscription = self.create_subscription(
            String,
            'lawnmower_status',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f"Heard: {msg.data}")

def main(args = None):
    rclpy.init(args = args)
    node = LawnmowerSub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()