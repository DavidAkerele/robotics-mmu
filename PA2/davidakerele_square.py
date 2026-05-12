#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import time
import math

def move_square():
    rospy.init_node('davidakerele_square_node', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    # 1 Hz loop rate
    rate = rospy.Rate(1) 
    
    speed = 0.2
    distance = 1.0
    angular_speed = 0.5
    angle = math.pi / 2.0  # 90 degrees

    rospy.loginfo("Robot is starting the square movement...")
    
    for _ in range(4):
        # Move Forward
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        vel_msg.linear.x = speed
        vel_msg.angular.z = 0
        
        while(current_distance < distance and not rospy.is_shutdown()):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = speed * (t1 - t0)
        
        # Stop
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
        time.sleep(1)
        
        # Turn
        t0 = rospy.Time.now().to_sec()
        current_angle = 0
        vel_msg.linear.x = 0
        vel_msg.angular.z = angular_speed
        
        while(current_angle < angle and not rospy.is_shutdown()):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed * (t1 - t0)
            
        # Stop
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        time.sleep(1)
        
    rospy.loginfo("Square movement completed.")

if __name__ == '__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass
