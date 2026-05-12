#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from rss_linux_pkg.srv import turtlebot_move_square, turtlebot_move_squareResponse
import math
import time

def move_square(sideLength, repetitions):
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    speed = 0.2
    angular_speed = 0.5
    angle = math.pi / 2.0  # 90 degrees

    for r in range(repetitions):
        rospy.loginfo(f"Starting repetition {r+1} of {repetitions}")
        for _ in range(4):
            # Move Forward
            t0 = rospy.Time.now().to_sec()
            current_distance = 0
            vel_msg.linear.x = speed
            vel_msg.angular.z = 0
            
            while(current_distance < sideLength and not rospy.is_shutdown()):
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
            
    return True

def handle_move_square(req):
    rospy.loginfo(f"Received request: sideLength={req.sideLength}, repetitions={req.repetitions}")
    try:
        success = move_square(req.sideLength, req.repetitions)
        return turtlebot_move_squareResponse(success)
    except Exception as e:
        rospy.logerr(f"Error during movement: {e}")
        return turtlebot_move_squareResponse(False)

def move_square_server():
    rospy.init_node('davidakerele_server')
    s = rospy.Service('move_square_service', turtlebot_move_square, handle_move_square)
    rospy.loginfo("Ready to move the robot in a square.")
    rospy.spin()

if __name__ == "__main__":
    move_square_server()
