#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math

class MoveDistance:
    def __init__(self):
        rospy.init_node('davidakerele_pubsub', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        
        self.start_x = None
        self.start_y = None
        self.current_x = None
        self.current_y = None
        self.distance_to_travel = 2.0  # Set desired distance to travel
        self.has_started = False
        
        self.rate = rospy.Rate(10)

    def odom_callback(self, msg):
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        
        if not self.has_started:
            self.start_x = self.current_x
            self.start_y = self.current_y
            self.has_started = True

    def move(self):
        # Wait until we get the first odom reading
        while not self.has_started and not rospy.is_shutdown():
            self.rate.sleep()
            
        vel_msg = Twist()
        vel_msg.linear.x = 0.3 # Move forward at 0.3 m/s
        
        rospy.loginfo(f"Moving {self.distance_to_travel} meters...")
        
        while not rospy.is_shutdown():
            distance_moved = math.sqrt((self.current_x - self.start_x)**2 + (self.current_y - self.start_y)**2)
            
            if distance_moved >= self.distance_to_travel:
                rospy.loginfo(f"Reached destination. Distance moved: {distance_moved:.2f} meters.")
                vel_msg.linear.x = 0
                self.velocity_publisher.publish(vel_msg)
                break
            else:
                self.velocity_publisher.publish(vel_msg)
            
            self.rate.sleep()

if __name__ == '__main__':
    try:
        mover = MoveDistance()
        mover.move()
    except rospy.ROSInterruptException:
        pass
