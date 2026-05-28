import rclpy
from custom_interfaces.msg import HelloWorld
from custom_interfaces.srv import IndexVerify

class DemoPublisher(rclpy.node.Node):
    def __init__(self):
        super().__init__('demo_publisher')
        self.publisher_ = self.create_publisher(HelloWorld, 'demo_topic', 10)
        self.service_ = self.create_service(IndexVerify, 'index_verify', self.service_callback)
        self.timer_ = self.create_timer(2, self.publish_callback)  # Time in seconds
        self.iter_ = 0
    
    def publish_callback(self):
        msg = HelloWorld()
        msg.msg = 'Hello world'
        self.iter_ += 1
        msg.msg_index = self.iter_

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}, index: {msg.msg_index}')
    
    def service_callback(self, request, response):
        response.bool = (request.msg_index == self.iter_)
        self.get_logger(f'Attempting to verify index: {request.msg_index}')
        return response