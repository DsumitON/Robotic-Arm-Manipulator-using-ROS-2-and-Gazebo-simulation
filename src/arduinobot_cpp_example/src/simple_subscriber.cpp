#include<rclcpp/rclcpp.hpp>
#include<std_msgs/msg/string.hpp>
#include<chrono>
using namespace std::chrono_literals;



class SimpleSubscriber : public rclcpp::Node
{
public:
    SimpleSubscriber() : Node("simple_subscriber")
    {
        sub_ = this->create_subscription<std_msgs::msg::String>(
            "chatter", 10,
            std::bind(&SimpleSubscriber::msgcallback, this, std::placeholders::_1)); 
        RCLCPP_INFO(this->get_logger(), "SimpleSubscriber node has been started.");
    }
    void msgcallback(const std_msgs::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "Received message: '%s'", msg->data.c_str());
    }
private:
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr sub_;
};  

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SimpleSubscriber>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}




