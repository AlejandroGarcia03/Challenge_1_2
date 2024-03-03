import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Time


class SignalProcessor(Node):
    def __init__(self):
        super().__init__('process')
        self.subscription_signal = self.create_subscription(Float32, '/signal', self.signal_callback, 10)
        self.publisher_proc_signal = self.create_publisher(Float32, '/proc_signal', 10)
        self.amplitude_reduction = 0.5  # Half amplitude reduction
        self.phase_shift = math.pi / 4  # Hardcoded phase shift of pi/4
        self.alpha = 0.5  # Offset parameter
        self.clock = self.get_clock()

    def signal_callback(self, msg):
        processed_signal = self.process_signal(msg.data)
        self.publisher_proc_signal.publish(processed_signal)
        self.get_logger().info('Processed signal: %f' % processed_signal.data)

    def process_signal(self, signal):
        # Offset the signal to ensure it remains positive
        offset_signal = signal + self.alpha if signal < 0 else signal
        # Reduce the amplitude
        reduced_amplitude_signal = offset_signal * self.amplitude_reduction
        # Add phase shift
        processed_signal = reduced_amplitude_signal + math.sin(signal + self.phase_shift)

        # Get current time in seconds
        current_time_sec = self.clock.now().nanoseconds / 1e9

        # Append current time to the processed signal
        processed_signal_with_time = processed_signal + current_time_sec

        return Float32(data=processed_signal_with_time)


def main(args=None):
    rclpy.init(args=args)
    signal_processor = SignalProcessor()
    rclpy.spin(signal_processor)
    signal_processor.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
