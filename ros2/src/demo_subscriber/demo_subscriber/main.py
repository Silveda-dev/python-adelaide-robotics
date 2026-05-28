from demo_subscriber import DemoSubscriber
import rclpy

def main(args=None):
    rclpy.init(args=args)
    node = DemoSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()