#!/usr/bin/env python3
import sys
import rospy
from rss_linux_pkg.srv import turtlebot_move_square

def move_square_client(sideLength, repetitions):
    rospy.wait_for_service('move_square_service')
    try:
        move_square = rospy.ServiceProxy('move_square_service', turtlebot_move_square)
        resp = move_square(sideLength, repetitions)
        return resp.success
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) == 3:
        sideLength = float(sys.argv[1])
        repetitions = int(sys.argv[2])
    else:
        print(f"Usage: {sys.argv[0]} [sideLength] [repetitions]")
        sys.exit(1)
        
    print(f"Requesting to move square with side length {sideLength} for {repetitions} repetitions.")
    success = move_square_client(sideLength, repetitions)
    print(f"Service returned success: {success}")
