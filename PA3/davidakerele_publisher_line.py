#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move_straight():
    rospy.init_node('davidakerele_publisher_line', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    # Move along x-axis
    vel_msg.linear.x = 0.3
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    rate = rospy.Rate(10) # 10hz
    rospy.loginfo("Moving the robot in a straight line...")
    
    while not rospy.is_shutdown():
        velocity_publisher.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_straight()
    except rospy.ROSInterruptException:
        pass
