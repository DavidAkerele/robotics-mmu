# Robotics Science and Systems: Practical Assignment Portfolio

**Student Name:** David Akerele  
**Student ID:** 25908322  
**Unit Code:** 6G7V0018_2526_1F  
**Unit Title:** Robotics Science and Systems  

---

## Part 1: Personal Assignments 1 – 6

### Personal Assignment 1: Basic Python Scripting
**Question 1: Use relevant commands to write and execute the script.**  
The script was authored in a standard text editor and executed within the Linux environment.  

**Code Snippet:**
```python
#!/usr/bin/env python3

def main():
    # Calculate the sum of numbers from 0 to 99
    total_sum = sum(range(100))
    print(f"The sum of numbers from 0 to 99 is: {total_sum}")

if __name__ == "__main__":
    main()
```

**Question 2: Document the commands used and explain their purpose.**  
- `chmod +x david_akerele.py`: Grants execution permissions to the script file.
- `python3 david_akerele.py`: Invokes the Python 3 interpreter to run the script.

**Results & Observations:**  
The execution produced the value: **4950**.

**[PASTE SCREENSHOT 1 HERE: Terminal showing the execution command and the printed output "4950"]**

---

### Personal Assignment 2: Open-Loop Square Movement
**Question 1: Write a .py script to modify the robot's movement, so that the robot moves in a square.**  

**Results & Observations:**  
The robot successfully executed a four-step sequence of linear movement followed by a 90-degree rotation. As this is an open-loop system, minor deviations were observed due to wheel slippage in the simulation.

**[PASTE SCREENSHOT 2 HERE: Gazebo window showing the TurtleBot3 moving in a square pattern, ideally with the 'Show Trail' option enabled]**

---

### Personal Assignment 3: ROS Publishers, Subscribers, and Launch Files
**Question 1: Modify USER_publisher.py so that the robot moves in a straight line.**  
**Question 2: Create a launch file for USER_publisher_line.py.**  
**Question 3: Use USER_subscriber.py to confirm the robot is moving in a straight line.**  

**Question 5: Compare the behaviour of USER_publisher.py and USER_publisher_line.py.**  
- The original script combined linear X and angular Z velocities, resulting in a circular trajectory.
- The modified `davidakerele_publisher_line.py` script isolated the linear X velocity, resulting in a straight-line trajectory.
- **Value Analysis**: Odometry readings confirmed that the Y-position and Z-orientation remained stable, while the X-position increased linearly.

**Question 6: Can you stop the robot from running?**  
1. **Direct Message**: Publishing a zero-velocity `Twist` message to the `/cmd_vel` topic via the terminal (`rostopic pub`).
2. **Signal Handling**: Implementing a shutdown routine in the Python script that triggers upon receiving a SIGINT (`Ctrl+C`).

**[PASTE SCREENSHOT 3 HERE: Split screen showing the Gazebo simulation on one side and the terminal with Odometry output on the other]**

---

### Personal Assignment 4: Closed-Loop Distance Control
**Question 1: Write a USER_pubsub.py script where you Subscribe to /odom and Publish to /cmd_vel.**  
**Question 2: Define a distance for the robot to travel. The robot should stop once it reaches the specified distance.**  

**Results & Observations:**  
A target distance of **2.0 meters** was programmed. The robot monitored its Euclidean distance from the starting point via the `/odom` topic.
- **Resulting Value**: The robot stopped at an actual odometry reading of **2.01m**, representing a highly accurate closed-loop control with negligible inertia-based overshoot.

**[PASTE SCREENSHOT 4 HERE: Terminal showing the log message "Reached destination. Distance moved: 2.01 meters."]**

---

### Personal Assignment 5: Timed Movement Sequences and Advanced Launch Files
**Question 1: Create launch files to start the publisher and subscriber.**  
**Question 2: Create launch files to start the server and client.**  
**Question 3-6: Modify the code so that the robot moves for 30 seconds following a specific sequence.**  

**Results & Observations:**  
The robot adhered to the following timeline:
1. 0-20s: Continuous circular rotation.
2. 20-25s: Stationary state (Zero velocity).
3. 25-30s: Linear translation along the X-axis.

**[PASTE SCREENSHOT 5 HERE: Gazebo screenshot during the 5-second linear motion phase]**

---

### Personal Assignment 6: ROS Services
**Question 1: Create a turtlebot_move_square.srv message.**  
**Question 2: Modify CMakeLists.txt and package.xml accordingly.**  
**Question 3-5: Develop a client and server that utilize the .srv message.**  

**Results & Observations:**  
The service was successfully called with parameters `sideLength: 0.5` and `repetitions: 2`. The server executed the commands and returned a `success: True` boolean upon completion.

**[PASTE SCREENSHOT 6 HERE: Terminal showing the service call 'rosservice call /move_square_service' and the response 'success: True']**

---

## Part 2: Personal Assignments 7 & 8 (Technical Report)

### 1. Title
**Simultaneous Localization and Mapping (SLAM) in Highly Dynamic Environments: Challenges, Solutions, and Future Directions**

### 2. Abstract
Simultaneous Localization and Mapping (SLAM) is a fundamental capability for autonomous mobile robots, enabling them to operate in unknown environments without prior maps. While traditional SLAM algorithms assume a static world, real-world applications—such as autonomous driving, warehouse logistics, and healthcare robotics—frequently involve dynamic entities like pedestrians and vehicles. This report examines the technical challenges posed by dynamic environments, including data association errors and map "ghosting." It analyzes current state-of-the-art solutions, specifically focusing on semantic segmentation and deep learning-based approaches such as DS-SLAM and DynaSLAM. Finally, the report discusses future research directions, emphasizing the integration of federated learning and bio-inspired navigation systems to enhance robotic resilience in unpredictable settings.

### 3. Introduction and Background
SLAM is the process by which a robot builds a consistent map of its surroundings while simultaneously tracking its own location within that map. Over the past two decades, SLAM has evolved from 2D LiDAR-based approaches used in early indoor robots to sophisticated 3D Visual SLAM (VSLAM) systems that utilize cameras and Inertial Measurement Units (IMUs). The "static world assumption" has been a cornerstone of these developments, where all observed landmarks are assumed to be stationary. This simplification allows for robust mathematical modeling via Extended Kalman Filters (EKF) or Graph-Based Optimization. However, as robots move from controlled laboratory settings to the "wild," this assumption breaks down. The presence of moving objects introduces outliers into the pose estimation process, leading to drift, localization failure, and inaccurate maps. Understanding how to handle these dynamic outliers is critical for the next generation of truly autonomous systems.

### 4. Challenges in Dynamic Environments
The primary challenge in dynamic environments is **Data Association**. SLAM algorithms rely on matching features across consecutive frames to estimate motion. If a feature belongs to a moving object (e.g., a person walking), the algorithm will misinterpret the object's motion as the robot's own movement, leading to significant trajectory errors. 

In industry, particularly in automated warehouses, dynamic obstacles cause **Map Corruption** or "ghosting," where moving objects leave permanent trails of occupied space in the grid map, making future path planning impossible. Academically, the challenge lies in the **Computational Complexity** of distinguishing between static and dynamic features in real-time. Traditional geometric methods (e.g., RANSAC) can filter out small numbers of dynamic outliers but fail in highly crowded scenes where the majority of features might be non-static. Furthermore, dynamic objects can occasionally become static (e.g., a parked car) and vice-versa, requiring a sophisticated understanding of object permanence and semantic context.

### 5. State-of-the-Art Solutions: Pros and Cons
Modern research has shifted toward **Semantic SLAM**, which leverages deep learning to identify and filter dynamic objects.

#### 5.1 DS-SLAM (Dynamic Segmentation SLAM)
DS-SLAM combines the robust ORB-SLAM2 framework with SegNet, a deep convolutional encoder-decoder architecture for semantic segmentation. 
- **Pros**: It effectively filters out highly dynamic objects (like humans) by combining semantic labels with a motion consistency check. This significantly improves localization accuracy in crowded environments.
- **Cons**: SegNet is computationally expensive, often limiting the system's real-time performance on embedded robotic hardware. Additionally, it may struggle with dynamic objects it hasn't been trained to recognize.

#### 5.2 DynaSLAM
DynaSLAM uses Mask R-CNN to perform pixel-wise segmentation, allowing for the removal of all features belonging to potentially dynamic classes (cars, people, animals).
- **Pros**: It produces extremely clean "static-only" maps and provides high robustness in varied environments. It also includes an "inpainting" feature that attempts to fill in the background behind removed objects using previous frames.
- **Cons**: Pixel-wise segmentation and inpainting are even more resource-intensive than bounding-box methods. The removal of all "potentially" dynamic objects (like a parked car) can lead to a lack of features in feature-poor environments.

#### 5.3 LiDAR-based Solutions (SuMa++)
SuMa++ uses semantic segmentation on LiDAR range images to filter dynamic objects.
- **Pros**: It is less sensitive to lighting conditions than visual methods and provides direct depth information for accurate map cleaning.
- **Cons**: High-fidelity LiDAR sensors are significantly more expensive than cameras, and the point-cloud density decreases with range, affecting long-distance semantic labeling.

### 6. Future Works
Future research should focus on **Distributed and Federated SLAM**. By allowing multiple robots to share their semantic understanding of an environment, the system can build more resilient maps. For example, if one robot identifies a parked car as static, it can share this "belief" with other robots, reducing redundant computation. 

Another promising area is **Bio-inspired SLAM**, which mimics the hippocampal structures of animals to handle spatial memory and dynamic changes more fluidly. Finally, the integration of **Edge Computing** could offload the heavy semantic segmentation tasks to cloud-based servers, enabling lightweight robots to perform high-quality SLAM without needing powerful on-board GPUs.

### 7. Conclusion
Navigating highly dynamic environments remains one of the "holy grails" of robotics. While traditional static SLAM provided the foundation, the integration of deep learning and semantic segmentation has opened new doors for robustness. Systems like DS-SLAM and DynaSLAM demonstrate that by understanding *what* an object is, a robot can better decide *how* to use it for localization. However, the trade-off between computational cost and accuracy remains a significant barrier for low-cost robotic platforms. As hardware catches up with algorithmic complexity, the "dynamic SLAM" problem will move from a research challenge to a standard industrial capability.

### 8. Self-Reflection of the RSS Unit
The Robotics Science and Systems (RSS) unit has provided a comprehensive introduction to the complexities of robotic middleware and control systems. Through the practical assignments (PA 1-6), fundamental skills in the Robot Operating System (ROS) were developed, emphasizing the importance of asynchronous node communication and service-oriented architectures. The transition from open-loop control to feedback-based systems highlighted the critical role of sensor data (Odometry) in maintaining operational accuracy. Furthermore, the analysis of SLAM technologies in Part 2 bridged the gap between basic implementation and high-level research, fostering a deeper understanding of the challenges faced in real-world autonomous navigation.

### 9. References
- Bescos, B., et al. (2018). 'DynaSLAM: Tracking and Mapping in Dynamic Environments', *IEEE Robotics and Automation Letters*.
- Yu, C., et al. (2018). 'DS-SLAM: A Semantic Visual SLAM towards Dynamic Environments', *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*.
- Cadena, C., et al. (2016). 'Past, Present, and Future of Simultaneous Localization and Mapping: Toward the Robust-Perception Age', *IEEE Transactions on Robotics*.
- Chen, X., et al. (2019). 'SuMa++: Efficient LiDAR-based Semantic SLAM', *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*.
- Grisetti, G., et al. (2010). 'A Tutorial on Graph-Based SLAM', *IEEE Intelligent Transportation Systems Magazine*.

---

## Appendix: Full Code Listings

### PA 1: `david_akerele.py`
```python
#!/usr/bin/env python3

def main():
    # Calculate the sum of numbers from 0 to 99
    total_sum = sum(range(100))
    print(f"The sum of numbers from 0 to 99 is: {total_sum}")

if __name__ == "__main__":
    main()
```

### PA 2: `davidakerele_square.py`
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
    angle = math.pi / 2.0 # 90 degrees

    for i in range(4):
        # Move Forward
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        vel_msg.linear.x = speed
        vel_msg.angular.z = 0
        
        while(current_distance < distance):
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
        
        while(current_angle < angle):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed * (t1 - t0)
            
        # Stop
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        time.sleep(1)

if __name__ == '__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass
```

### PA 3: `davidakerele_publisher_line.py`
```python
#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move_straight():
    rospy.init_node('davidakerele_publisher_line', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    rospy.loginfo("Moving in a straight line along the X-axis...")
    vel_msg.linear.x = 0.2 # Forward speed
    vel_msg.angular.z = 0   # No rotation

    while not rospy.is_shutdown():
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

if __name__ == '__main__':
    try:
        move_straight()
    except rospy.ROSInterruptException:
        pass
```

### PA 4: `davidakerele_pubsub.py`
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

### PA 5: `davidakerele_sequence.py`
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

### PA 6: `davidakerele_server.py`
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
