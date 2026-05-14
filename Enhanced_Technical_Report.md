# Robotics Science and Systems Portfolio and Technical Report: ROS-Based Robot Control and Navigation Systems

## Abstract

This report presents a comprehensive overview of the practical assignments completed for the Robotics Science and Systems unit. The work focuses on the implementation of robotics programming concepts using Python and the Robot Operating System (ROS). The portfolio demonstrates progressive development from basic Python scripting to advanced ROS-based robot control using publishers, subscribers, launch files, odometry feedback, and ROS services.

In addition to the implementation tasks, the report critically examines robotics navigation and control systems as a broader academic topic, discussing the challenges faced in academia and industry, the current state-of-the-art solutions, and possible future developments. The exercises revealed the limitations of simple time-based, open-loop control approaches and demonstrated the distinct advantages of closed-loop, feedback-driven systems using odometry data. Overall, the coursework provided valuable experience in robotics programming, distributed system integration, and analytical problem-solving.

---

## 1. Introduction and Background

Robotics has become one of the most rapidly advancing areas of modern computing and engineering. Robots are now ubiquitous in manufacturing, healthcare, logistics, agriculture, autonomous vehicles, and service industries. A major driver of this growth is the development of intelligent robotic systems capable of sophisticated sensing, decision-making, and autonomous navigation in dynamic environments.

One of the foundational software platforms enabling this research and industrial application is the Robot Operating System (ROS). ROS provides a flexible, distributed middleware framework that allows developers to create modular robotic applications using publishers, subscribers, services, and launch systems. It abstracts hardware complexities, simplifies inter-process communication, and robustly supports simulation, control, and real-world deployment.

![Diagram 1: ROS Architecture Overview](file:///C:/Users/23490/.gemini/antigravity/brain/f9220b97-7b20-4737-b738-02e85a966e58/ros_architecture_diagram_1778775977315.png)
*Figure 1: A flowchart illustrating the ROS Master, Nodes, Topics (Publishers/Subscribers), and Services explaining the distributed communication framework.*

The Robotics Science and Systems coursework focused on practical ROS programming and robot control. The portfolio included six assignments implemented using Python 3 and ROS within a Linux environment, utilising the TurtleBot3 simulation platform. The overall objective was to bridge theoretical kinematics and control systems with practical programming ability and system integration techniques.

---

## 2. Overview of Practical Assignments

### 2.1 Personal Assignment 1: Basic Python Scripting

The first assignment established the fundamentals of Python scripting in a Linux ecosystem. A Python program was developed to calculate the sum of integers from 0 to 99. The task required the use of Linux terminal commands (such as `chmod +x`) to configure executable permissions and execute the script using the Python interpreter. This foundational step is critical, as ROS heavily relies on proper file permissions and environment sourcing for node execution.

### 2.2 Personal Assignment 2: Open-Loop Square Movement

This assignment introduced robot kinematics through open-loop control. A ROS node was created to move the TurtleBot3 in a square pattern relying entirely on time-based calculations.

The implementation published `geometry_msgs/Twist` messages to the `/cmd_vel` topic. Linear ($v$) and angular ($\omega$) velocity values were configured to move the robot forward and rotate it by 90 degrees ($\frac{\pi}{2}$ radians). In open-loop control, distance is assumed as a function of time:

$$d = v \cdot t$$

**Results & Evaluation:** While the robot approximated a square path, significant inaccuracies accumulated over time due to simulated wheel slip and integration drift.

![Chart 1: Open-Loop Trajectory Drift](file:///C:/Users/23490/.gemini/antigravity/brain/f9220b97-7b20-4737-b738-02e85a966e58/open_loop_drift_chart_1778775988377.png)
*Figure 2: Trajectory comparison showing the drift of the open-loop system versus the ideal square path over multiple repetitions.*

### 2.3 Personal Assignment 3: ROS Publishers, Subscribers, and Launch Files

This task introduced the core of ROS communication. A publisher node moved the robot in a straight line, while a simultaneous subscriber node monitored the robot's state via the `/odom` (odometry) topic.

The odometry readings confirmed that motion was strictly maintained along the X-axis. Furthermore, ROS launch files (XML-based) were authored to automate the bringing up of the ROS Master, the simulation environment, and multiple nodes simultaneously, highlighting the orchestration capabilities required for complex robotic systems.

### 2.4 Personal Assignment 4: Closed-Loop Distance Control

Addressing the flaws of Assignment 2, this task implemented closed-loop control using real-time odometry feedback. The robot continuously monitored its position $(x, y)$ from the `/odom` topic.

The algorithm dynamically calculated the Euclidean distance travelled from the initial starting coordinates $(x_0, y_0)$ to its current coordinates $(x_c, y_c)$:

$$d = \sqrt{(x_c - x_0)^2 + (y_c - y_0)^2}$$

**Results & Evaluation:** The robot autonomously halted upon reaching the precise 2-metre target. This empirically demonstrated how sensory feedback mitigates cumulative error, vastly improving precision and reliability.

### 2.5 Personal Assignment 5: Timed Movement Sequences and Launch Files

This assignment required developing a finite state machine (FSM) approach to robot behaviour. The sequence included:

1. Circular motion (linear + angular velocity) for 20 seconds.
2. Stationary pause for 5 seconds.
3. Linear translation for 5 seconds.
4. Complete stop.

![Diagram 2: State Machine for Movement Sequence](file:///C:/Users/23490/.gemini/antigravity/brain/f9220b97-7b20-4737-b738-02e85a966e58/movement_state_machine_1778776008570.png)
*Figure 3: State transition diagram showing the flow between different movement phases and the timing conditions.*

### 2.6 Personal Assignment 6: ROS Services

The final assignment shifted from continuous topic-based communication to synchronous client-server interactions. A custom service definition, `turtlebot_move_square.srv`, was authored.

The server accepted a request containing two parameters (`sideLength` and `repetitions`), executed the precise geometric movements, and returned a boolean success response. This highlighted the necessity of Services for distinct, trigger-based remote procedure calls (RPCs) in robotics, contrasting with the continuous data streams of Topics.

---

## 3. Challenges in Robotics Across Academia and Industry

Despite rapid advancements, deploying autonomous robots in unstructured environments presents significant hurdles:

* **Navigation and Localisation Accuracy:** Robots in dynamic environments suffer from non-systematic errors (sensor noise) and systematic errors (odometry drift). In open-loop systems, these errors grow unboundedly.
* **Real-Time Computational Constraints:** Autonomous navigation requires processing high-bandwidth sensor data (e.g., point clouds, high-res video) and running complex path-planning algorithms synchronously, demanding high onboard compute power.
* **System Integration and Middleware:** Modern robots are amalgamations of heterogeneous hardware. Ensuring seamless communication between varied microcontrollers, advanced APIs, and mechanical actuators remains an engineering bottleneck.
* **Safety and Human-Robot Interaction (HRI):** Particularly in collaborative robotics (cobots) and healthcare, rigid safety standards must be met to ensure fail-safes and collision avoidance when operating in close proximity to humans.

---

## 4. State-of-the-Art Robotics Solutions

To address the aforementioned challenges, the industry has adopted several sophisticated paradigms. The table below summarises the leading technologies along with their respective trade-offs.

| Technology | Overview | Advantages | Disadvantages |
| --- | --- | --- | --- |
| **SLAM (Simultaneous Localisation and Mapping)** | Fuses LiDAR, vision, and odometry to build maps and locate the robot concurrently. | • Enables true autonomy in unknown environments<br>• High precision mapping | • Computationally expensive<br>• Can fail in featureless environments (the "kidnapped robot" problem) |
| **Machine Learning / AI Perception** | Utilises CNNs and Reinforcement Learning for object detection and dynamic path planning. | • Highly adaptive to novel scenarios<br>• Can interpret complex visual data | • Requires massive training datasets<br>• "Black box" nature makes safety certification difficult |
| **ROS-Based Modular Architectures** | Distributed middleware standardising robotic software development. | • Massive open-source package ecosystem<br>• Highly modular and scalable | • Steep learning curve<br>• ROS1 struggles with true real-time, deterministic execution |
| **Closed-Loop / PID Control** | Proportional-Integral-Derivative controllers utilising continuous sensor feedback to adjust actuators. | • Eliminates cumulative drift<br>• Highly robust to external physical disturbances | • Requires precise tuning of gains ($K_p, K_i, K_d$)<br>• Heavily reliant on sensor fidelity |

---

## 5. Future Work and Improvements

Future iterations of robotic systems will likely shift away from monolithic onboard processing toward **Cloud Robotics**, offloading heavy SLAM and AI computations to low-latency edge servers.

Furthermore, a critical evolution currently underway is the transition from ROS1 to **ROS2**. ROS2 replaces the custom ROS1 communication stack with Data Distribution Service (DDS), an industry standard that guarantees Quality of Service (QoS), enhanced security, and deterministic real-time communication—solving many of the scale and safety issues inherent in current commercial deployments.

Finally, the adoption of **Digital Twins**—highly accurate, physics-based virtual replicas of real-world environments (using tools like Nvidia Isaac Sim or advanced Gazebo environments)—will allow developers to use reinforcement learning to train robots virtually for millions of hours before executing a single line of code on physical hardware.

![Chart 2: Projected Growth of ROS2 vs ROS1 Adoption](file:///C:/Users/23490/.gemini/antigravity/brain/f9220b97-7b20-4737-b738-02e85a966e58/ros1_vs_ros2_adoption_1778776021683.png)
*Figure 4: Timeline showing the industry shift toward ROS2 frameworks.*

---

## 6. Conclusion

This report detailed a robust practical progression through the core tenets of robotics programming using ROS and Python. The TurtleBot3 simulated assignments practically demonstrated why modern robotics relies on closed-loop feedback systems; whereas open-loop control is mathematically sound on paper, it fails against the physical realities of friction and drift.

By implementing publishers, subscribers, custom services, and launch file orchestration, the portfolio provided a micro-scale view of the exact architectures used in enterprise robotics. As the field looks toward ROS2, AI-driven perception, and advanced SLAM, the foundational skills of kinematic control, sensor feedback, and modular system design developed in this unit will remain highly relevant.

---

## 7. Self-Reflection on the Robotics Science and Systems Unit

The unit bridged the gap between theoretical computer science and physical engineering. Prior to this coursework, my experience with distributed middleware and Linux-based robotics was limited. Constructing custom ROS nodes directly improved my Python proficiency, particularly in handling object-oriented programming, real-time callbacks, and ROS message types.

The most transformative learning moment was visually observing the failure of the open-loop square movement compared to the precision of the odometry-based closed-loop stop. It solidified the engineering maxim that a system is only as good as its feedback. Moving forward, I feel significantly more confident navigating Linux file systems, debugging distributed node graphs, and applying programmatic logic to solve physical movement challenges.

---

## 8. References

1. Quigley, M., Gerkey, B., and Smart, W. (2015). *Programming Robots with ROS*. O’Reilly Media.
2. Siciliano, B. and Khatib, O. (2016). *Springer Handbook of Robotics*. Springer.
3. Corke, P. (2017). *Robotics, Vision and Control: Fundamental Algorithms in MATLAB*. Springer.
4. Thrun, S., Burgard, W., and Fox, D. (2005). *Probabilistic Robotics*. MIT Press.
5. ROS Documentation. (2026). *Robot Operating System Documentation*. Available at: [https://www.ros.org/](https://www.ros.org/)
6. TurtleBot3 Documentation. (2026). *ROBOTIS e-Manual*. Available at: [https://emanual.robotis.com/](https://emanual.robotis.com/)
7. Siegwart, R., Nourbakhsh, I., and Scaramuzza, D. (2011). *Introduction to Autonomous Mobile Robots*. MIT Press.
8. Murphy, R. (2019). *Introduction to AI Robotics*. MIT Press.
