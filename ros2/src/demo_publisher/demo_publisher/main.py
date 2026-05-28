from demo_publisher import DemoPublisher
import rclpy

def main(args=None):
    rclpy.init(args=args)
    node = DemoPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()