#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry

def odom_callback(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    rospy.loginfo(f"Robot Position: x = {x:.2f}, y = {y:.2f}")

def listener():
    rospy.init_node('davidakerele_subscriber', anonymous=True)
    rospy.Subscriber('/odom', Odometry, odom_callback)
    rospy.loginfo("Subscribed to /odom. Listening to robot position...")
    rospy.spin()

if __name__ == '__main__':
    listener()
