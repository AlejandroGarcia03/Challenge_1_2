import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from std_msgs.msg import String
import yaml
import numpy
from my_msg_interfaces.msg import MyParameter


class SignalGenerator(Node):
    def __init__(self):
        super().__init__('signal_generator')

        self.declare_parameters(
            namespace="",
            parameters=[
                ('requested_signal', 0),
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
        plotted_signal=0
        offset_signal=0
        self.create_timer(self.timer_period, self.timer_callback)

    def timer_callback(self):
        msg_signal = MyParameter()
        defaulttype_= self.get_parameter('default.type_').get_parameter_value().string_value
        defaultampl_= self.get_parameter('default.amplitude_').get_parameter_value().double_value
        defaultfreq_= self.get_parameter('default.frequency_').get_parameter_value().double_value
        defaultoffs_= self.get_parameter('default.offset_').get_parameter_value().double_value
        defaultphas_= self.get_parameter('default.phase_').get_parameter_value().double_value
        defaulttime_= self.get_parameter('default.time_').get_parameter_value().double_value

        squaretype_= self.get_parameter('square.type_').get_parameter_value().string_value
        squareampl_= self.get_parameter('square.amplitude_').get_parameter_value().double_value
        squarefreq_= self.get_parameter('square.frequency_').get_parameter_value().double_value
        squareoffs_= self.get_parameter('square.offset_').get_parameter_value().double_value
        squarephas_= self.get_parameter('square.phase_').get_parameter_value().double_value
        squaretime_= self.get_parameter('square.time_').get_parameter_value().double_value

        sawtoothtype_= self.get_parameter('sawtooth.type_').get_parameter_value().string_value
        sawtoothampl_= self.get_parameter('sawtooth.amplitude_').get_parameter_value().double_value
        sawtoothfreq_= self.get_parameter('sawtooth.frequency_').get_parameter_value().double_value
        sawtoothoffs_= self.get_parameter('sawtooth.offset_').get_parameter_value().double_value
        sawtoothphas_= self.get_parameter('sawtooth.phase_').get_parameter_value().double_value
        sawtoothtime_= self.get_parameter('sawtooth.time_').get_parameter_value().double_value
        
        signal= self.get_parameter('requested_signal').get_parameter_value().integer_value
        
        if  signal == 0 :
            msg_signal.type= defaulttype_
            msg_signal.ampl= defaultampl_
            msg_signal.freq= defaultfreq_
            msg_signal.offset= defaultoffs_
            msg_signal.phase= defaultphas_
            msg_signal.time= defaulttime_
            plotted_signal= defaultampl_*numpy.sin(self.i*defaultfreq_+defaultphas_)
            offset_signal= plotted_signal * numpy.cos(defaultoffs_) + numpy.sin(defaultoffs_)*(defaultampl_*numpy.cos(self.i*defaultfreq_+defaultphas_))
            msg_signal.signal=offset_signal
            
            
        elif  signal == 1 :
            msg_signal.type= squaretype_
            msg_signal.ampl= squareampl_
            msg_signal.freq= squarefreq_
            msg_signal.offset= squareoffs_
            msg_signal.phase= squarephas_
            msg_signal.time= squaretime_
        elif  signal == 2 :
            msg_signal.type= sawtoothtype_
            msg_signal.ampl= sawtoothampl_
            msg_signal.freq= sawtoothfreq_
            msg_signal.offset= sawtoothoffs_
            msg_signal.phase= sawtoothphas_
            msg_signal.time= sawtoothtime_

        
        self.pub_msg.publish(msg_signal)


def main(args=None):
    rclpy.init(args=args)
    signal_generator = SignalGenerator()
    
    rclpy.spin(signal_generator)
    signal_generator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()