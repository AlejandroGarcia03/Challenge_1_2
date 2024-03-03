import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from std_msgs.msg import String
import yaml
import math
from my_msg_interfaces.msg import MyParameter


class SignalGenerator(Node):
    def __init__(self):
        super().__init__('signal_generator')

        self.declare_parameters(
            namespace="",
            parameters=[
                ('default.type_', rclpy.Parameter.Type.STRING),
                ('default.amplitude_', rclpy.Parameter.Type.DOUBLE),
                ('default.frequency_', rclpy.Parameter.Type.DOUBLE),
                ('default.offset_', rclpy.Parameter.Type.DOUBLE),
                ('default.phase_', rclpy.Parameter.Type.DOUBLE),
                ('default.time_', rclpy.Parameter.Type.DOUBLE),
                ('square.type_', rclpy.Parameter.Type.STRING),
                ('square.amplitude_', rclpy.Parameter.Type.DOUBLE),
                ('square.frequency_', rclpy.Parameter.Type.DOUBLE),
                ('square.offset_',rclpy.Parameter.Type.DOUBLE),
                ('square.phase_', rclpy.Parameter.Type.DOUBLE),
                ('square.time_', rclpy.Parameter.Type.DOUBLE),
                ('sawtooth.type_', rclpy.Parameter.Type.STRING),
                ('sawtooth.amplitude_', rclpy.Parameter.Type.DOUBLE),
                ('sawtooth.frequency_', rclpy.Parameter.Type.DOUBLE),
                ('sawtooth.offset_', rclpy.Parameter.Type.DOUBLE),
                ('sawtooth.phase_', rclpy.Parameter.Type.DOUBLE),
                ('sawtooth.time_', rclpy.Parameter.Type.DOUBLE),
            ])
        
        self.pub_msg = self.create_publisher(MyParameter, 'signal_parameters', 10)
        self.timer_period = 0.02  # seconds (2 Hz)
        self.i = 0
        self.create_timer(self.timer_period, self.timer_callback)

    def timer_callback(self):
        msg_signal = MyParameter()
        type_ = self.get_parameter('default.type_').value
        msg_signal.type= type_
        self.pub_msg.publish(msg_signal)


def main(args=None):
    rclpy.init(args=args)
    signal_generator = SignalGenerator()
    
    rclpy.spin(signal_generator)
    signal_generator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()