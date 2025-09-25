import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter




class SimpleParameter(Node):
    def __init__(self):
        super().__init__('simple_parameter')
        self.declare_parameter('simple_int_param', 28)
        self.declare_parameter('simple_string_param', "Antonio")

        self.add_on_set_parameters_callback(self.paramChanageCallback)

    def paramChanageCallback(self, params):
        result = SetParametersResult()
        result.successful = False
        for param in params:
            if param.name == 'simple_int_param' and param.type_ == Parameter.Type.INTEGER:
                self.get_logger().info(f"Parameter 'simple_int_param' changed to {param.value}")
                result.successful = True
            if param.name == 'simple_string_param' and param.type_ == Parameter.Type.STRING:
                self.get_logger().info(f"Parameter 'simple_string_param' changed to {param.value}")
                result.successful = True

        return result
                

def main(args=None):
    rclpy.init(args=args)
    node = SimpleParameter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
# This code defines a simple ROS 2 node that manages parameters.