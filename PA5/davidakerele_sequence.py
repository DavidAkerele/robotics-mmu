#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import time

def move_sequence():
    rospy.init_node('davidakerele_sequence', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    rate = rospy.Rate(10) # 10hz
    
    # 1. Move in a circle for 20 seconds
    rospy.loginfo("1. Moving in a circle for 20 seconds...")
    vel_msg.linear.x = 0.2
    vel_msg.angular.z = 0.5
    t_end = rospy.Time.now().to_sec() + 20.0
    while rospy.Time.now().to_sec() < t_end and not rospy.is_shutdown():
        velocity_publisher.publish(vel_msg)
        rate.sleep()
        
    # 2. Stop for 5 seconds
    rospy.loginfo("2. Stopping for 5 seconds...")
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    t_end = rospy.Time.now().to_sec() + 5.0
    while rospy.Time.now().to_sec() < t_end and not rospy.is_shutdown():
        rate.sleep()

    # 3. Move along the x-axis for 5 seconds
    rospy.loginfo("3. Moving along x-axis for 5 seconds...")
    vel_msg.linear.x = 0.3
    vel_msg.angular.z = 0
    t_end = rospy.Time.now().to_sec() + 5.0
    while rospy.Time.now().to_sec() < t_end and not rospy.is_shutdown():
        velocity_publisher.publish(vel_msg)
        rate.sleep()

    # 4. Stop completely
    rospy.loginfo("4. Stopping completely.")
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        move_sequence()
    except rospy.ROSInterruptException:
        pass
