import rclpy
from custom_messages.msg import HelloWorld
from custom_messages.srv import IndexVerify

class DemoSubscriber(rclpy.node.Node):
    def __init__(self):
        super().__init__('demo_subscriber')
        self.subscription_ = self.create_subscription(HelloWorld, 'demo_topic', self.subscriber_callback, 10)
    
        self.client_ = self.create_client(IndexVerify, 'index_verify')
        while not self.client_.wait_for_service(timeout_sec=2.0):
            self.get_logger().info('IndexVerify service not available, trying again...')
        self.request_ = IndexVerify.Request()
    
    def send_request(self, msg_index):
        self.request_.msg_index = msg_index
        self.future_ = self.client_.call_async(self.request_)
        rclpy.spin_until_future_complete(self, self.future_)
        return self.future_.result()

    def subscriber_callback(self, msg):
        self.get_logger().info(f'Received: {msg.msg}, index: {msg.msg_index}. Verifying index...')
        verified = self.send_request(msg.msg_index)
        self.get_logger().info(f'Message with index {msg.msg_index} verified? {verified.verified}')