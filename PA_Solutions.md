# Robotics Science and Systems: Practical Assignment Portfolio

**Student Name:** David Akerele  
**Student ID:** 25908322  
**Unit Code:** 6G7V0018_2526_1F  
**Unit Title:** Robotics Science and Systems  

---

## Part 1: Personal Assignments 1 – 6

### Personal Assignment 1: Basic Python Scripting

**Question 1:** Use relevant commands to write and execute the script.
The script was written using a text editor and executed using the Python 3 interpreter.

**Code Snippet (`PA1/david_akerele.py`):**
```python
#!/usr/bin/env python3
def main():
    # Calculate the sum of numbers from 0 to 99
    total_sum = sum(range(100))
    print(f"The sum of numbers from 0 to 99 is: {total_sum}")

if __name__ == "__main__":
    main()
```

**Question 2:** Document the commands used and explain their purpose.
- `chmod +x david_akerele.py`: Makes the script executable by the system.
- `python3 david_akerele.py` or `./david_akerele.py`: Runs the script using the Python 3 environment.

**Observations:**
The script successfully calculated the sum as 4950. This exercise confirmed the basic setup of the Python environment and the ability to execute standalone scripts within the Linux filesystem.

---

### Personal Assignment 2: Open-Loop Square Movement

**Question 1:** Write a .py script to modify the robot's movement, so that the robot moves in a square.

**Code Snippet (`PA2/davidakerele_square.py`):**
```python
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
```

**Observations:**
The robot moved in a roughly square pattern. Since this is open-loop control using `time.sleep()` (and time-based distance calculation), the square was not perfectly closed due to minor wheel slip and simulation drift. However, the logic for sequential linear and angular velocity commands was correctly implemented.

---

### Personal Assignment 3: ROS Publishers, Subscribers, and Launch Files

**Question 1:** Modify USER_publisher.py so that the robot moves in a straight line.
The script was renamed to `davidakerele_publisher_line.py` and modified to publish only linear velocity in the X-axis.

**Code Snippet (`PA3/davidakerele_publisher_line.py`):**
```python
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
```

**Question 2:** Create a launch file for USER_publisher_line.py.
A launch file `davidakerele_line.launch` was created to start both the publisher and subscriber nodes simultaneously.

**Launch File Snippet (`PA3/davidakerele_line.launch`):**
```xml
<launch>
  <node name="davidakerele_publisher_line" pkg="rss_linux_pkg" type="davidakerele_publisher_line.py" output="screen" />
  <node name="davidakerele_subscriber" pkg="rss_linux_pkg" type="davidakerele_subscriber.py" output="screen" />
</launch>
```

**Question 3:** Use USER_subscriber.py to confirm the robot is moving in a straight line.
The subscriber node outputted the Odometry data to the console.

**Code Snippet (`PA3/davidakerele_subscriber.py`):**
```python
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
```

**Question 5:** Compare the behaviour of USER_publisher.py and USER_publisher_line.py.
- `davidakerele_publisher.py` (Original): Produced a circular motion by combining linear X velocity and angular Z velocity.
- `davidakerele_publisher_line.py`: Produced a linear motion along the X-axis only.
- **Observation:** The original script resulted in a continuous arc, while the modified script maintained a constant heading, confirmed by the odom readings showing increasing X values while Y remained near zero.

**Question 6:** Can you stop the robot from running?
1. **Command Line:** Sending a Twist message with all zeros to the `/cmd_vel` topic via `rostopic pub`.
2. **Keyboard Interrupt:** Pressing `Ctrl+C` in the terminal running the publisher node, provided the script has a shutdown handler to send a final zero-velocity command.

---

### Personal Assignment 4: Closed-Loop Distance Control

**Question 1:** Write a USER_pubsub.py script where you Subscribe to /odom and Publish to /cmd_vel.
The script `davidakerele_pubsub.py` implements a closed-loop system by reading current position from `/odom` and calculating the Euclidean distance from the starting point to determine when to stop.

**Code Snippet (`PA4/davidakerele_pubsub.py`):**
```python
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
```

**Question 2:** Define a distance for the robot to travel. The robot should stop once it reaches the specified distance.
A target distance of 2.0 meters was set.

**Observations:**
Unlike the open-loop square from PA2, this script uses Odometry feedback, which makes it significantly more accurate. The robot stopped exactly at the 2.0m mark (with minimal inertia-based overshoot), demonstrating the importance of feedback loops in robotics.

---

### Personal Assignment 5: Timed Movement Sequences and Advanced Launch Files

**Question 1:** Create launch files to start the publisher and subscriber.
Created `davidakerele_nodes.launch`.

**Launch File Snippet (`PA5/davidakerele_nodes.launch`):**
```xml
<launch>
  <node name="davidakerele_publisher" pkg="rss_linux_pkg" type="davidakerele_publisher.py" output="screen" />
  <node name="davidakerele_subscriber" pkg="rss_linux_pkg" type="davidakerele_subscriber.py" output="screen" />
</launch>
```

**Question 2:** Create launch files to start the server and client.
Created `davidakerele_service.launch`.

**Launch File Snippet (`PA5/davidakerele_service.launch`):**
```xml
<launch>
  <node name="davidakerele_server" pkg="rss_linux_pkg" type="davidakerele_server.py" output="screen" />
  <node name="davidakerele_client" pkg="rss_linux_pkg" type="davidakerele_client.py" output="screen" />
</launch>
```

**Question 3-6:** Modify the code so that the robot moves for 30 seconds following a specific sequence.
The script `davidakerele_sequence.py` was implemented with four phases:
1. **20s:** Circular motion (linear=0.2, angular=0.5).
2. **5s:** Complete stop.
3. **5s:** Straight motion along X-axis (linear=0.3).
4. **Final Stop.**

**Code Snippet (`PA5/davidakerele_sequence.py`):**
```python
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
```

**Observations:**
The robot followed the sequence precisely. The use of `rospy.Time.now()` allowed for accurate duration management without blocking the main loop entirely. The launch files simplified the orchestration of multiple nodes.

---

### Personal Assignment 6: ROS Services

**Question 1:** Create a turtlebot_move_square.srv message.
Defined the service with `float64 sideLength` and `int32 repetitions` as inputs and `bool success` as output.

**Service Definition (`PA6/srv/turtlebot_move_square.srv`):**
```
float64 sideLength
int32 repetitions
---
bool success
```

**Server Code (`PA6/davidakerele_server.py`):**
```python
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
```

**Client Code (`PA6/davidakerele_client.py`):**
```python
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
```
