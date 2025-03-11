import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
class turtlesimSubscriber(Node):
	def __init__(self):
		super().__init__('turtlesim_subscriber')
		self.subscription=self.create_subscription(Pose,/turtle1/pose,self.listener_callback,10)
	def listener_callback(self,msg):
		x,y=msg.x,msg,y
		dist=(x**2+y**2)**0.5
		self.get_logger().info(f'Distance of Turtle from Origin: {dist}')
def main(args=None):
	rclpy.init(args=args)
	node=turtlesimSubscriber()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()
if __name__=='__main__':
	main()