#!/usr/bin/env python3
import os
os.environ['GPIOZERO_PIN_FACTORY'] = 'rpigpio'
import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool
from gpiozero import OutputDevice  # Use gpiozero for GPIO access

class MagnetServer(Node):
    def __init__(self):
        super().__init__('magnet_server')
        self.service = self.create_service(SetBool, 'toggle_magnets_service', self.handle_toggle_request)
        self.relay_pin = 26  # Make sure this is the correct GPIO pin number
        self.relay = OutputDevice(self.relay_pin)  # Use gpiozero's OutputDevice for the relay

    def handle_toggle_request(self, request, response):
        try:
            self.get_logger().info('Received request to toggle magnets: %s' % request.data)
            if request.data:
                self.relay.on()
            else:
                self.relay.off()
            response.success = True
            return response
        except Exception as e:
            self.get_logger().error('Error in handling request: %s' % str(e))
            response.success = False
            return response

    def destroy_node(self):
        self.relay.close()  # Clean up GPIO when the node is destroyed
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    magnet_server = MagnetServer()
    rclpy.spin(magnet_server)
    magnet_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
