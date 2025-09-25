import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from arduinobot_msgs.action import Fibonacci  # Replace with your actual action type    
import time


class SimpleActionServer(Node):
    def __init__(self):
        super().__init__('simple_action_server')
        self.action_server = ActionServer(
            self,
            # Replace 'YourAction' with the actual action type you want to use
            Fibonacci,
            'fibonacci',
            self.goalcallback
            )
        self.get_logger().info('Action Server has been started.')



    def goalcallback(self, goal_handle):
        self.get_logger().info('Received goal request with order %d' % goal_handle.request.order)
        feedback_msg = Fibonacci.Feedback()
        feedback_msg.partial_sequence = [0, 1]
        
        for i in range(1, goal_handle.request.order):
            feedback_msg.partial_sequence.append(feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i - 1])
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)  # Simulate work being done
        goal_handle.succeed()
        result = Fibonacci.Result()
        result.sequence = feedback_msg.partial_sequence
        self.get_logger().info('Goal succeeded!')
        return result
    




def main(args=None):
    rclpy.init(args=args)
    simple_action_server = SimpleActionServer()
    simple_action_server.destroy_node()
    rclpy.spin(simple_action_server)
    rclpy.shutdown()


if __name__ == '__main__':
    main()