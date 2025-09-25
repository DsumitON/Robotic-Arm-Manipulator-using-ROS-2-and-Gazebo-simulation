import rclpy
from rclpy.node import Node
from arduinobot_msgs.srv import AddTwoInts


class SimpleServiceServer(Node):

    def __init__(self):
        super().__init__('simple_service_server')
        self.service_ = self.create_service(AddTwoInts, 'add_two_ints', self.servicecallback)
        self.get_logger().info('Service Server is Ready to Add Two Ints')   


    def servicecallback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
        self.get_logger().info('Sending back response: %d' % (response.sum))
        return response
    

def main(args=None):
    rclpy.init(args=args)
    simple_service_server = SimpleServiceServer()
    rclpy.spin(simple_service_server)
    simple_service_server.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()