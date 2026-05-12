# Robotics Science and Systems (RSS) - Assessment 

This repository contains the codebase for the **Robotics Science and Systems** module assessment (Unit Code: 6G7V0018_2526_1F) at Manchester Metropolitan University. The project demonstrates practical implementations of the Robot Operating System (ROS) using Python, and includes the foundational outline for a technical research report on Mobile Robot SLAM.

## 📂 Repository Structure

The project is structured according to the Personal Assignments (PA) specified in the assessment brief:

*   **`PA1/`**: Basic Python scripting. Includes a script (`david_akerele.py`) to calculate the sum of numbers from 0 to 99, and the terminal commands required to execute it.
*   **`PA2/`**: Open-loop ROS control. Contains `davidakerele_square.py` which publishes `geometry_msgs/Twist` messages to move a TurtleBot3 in a square pattern.
*   **`PA3/`**: ROS Publishers and Subscribers. Contains a publisher (`davidakerele_publisher_line.py`) to move the robot in a straight line, a subscriber (`davidakerele_subscriber.py`) to monitor Odometry (`/odom`), and a combined launch file.
*   **`PA4/`**: Closed-loop control. Contains a unified Publisher/Subscriber script (`davidakerele_pubsub.py`) that utilizes Odometry feedback to move the robot precisely 2.0 meters and stop.
*   **`PA5/`**: Timed Sequential logic. Features a script (`davidakerele_sequence.py`) that dictates a 30-second multi-stage movement sequence (circle, stop, straight, stop) alongside required launch files.
*   **`PA6/`**: Custom ROS Services. Includes a custom service definition (`turtlebot_move_square.srv`), and a Service Server/Client architecture (`davidakerele_server.py` and `davidakerele_client.py`) allowing dynamic repetition of square movements.
*   **`PA7_8/`**: Contains the highly-structured academic outline (`Technical_Report_Outline.md`) for a 1,500-word report on **Mobile Robot SLAM in Highly Dynamic Environments**.

## 🚀 How to Run

These scripts are designed to be run within a ROS Noetic environment configured with the TurtleBot3 simulation packages.

1.  **Clone the repository** into your catkin workspace's `scripts` folder:
    ```bash
    cd ~/catkin_ws_rss/src/rss_linux_pkg/scripts/
    git clone <repository_url> .
    ```

2.  **Make the Python scripts executable:**
    ```bash
    chmod +x */*.py
    ```

3.  **Build the workspace** (Required for the PA6 custom service to compile):
    ```bash
    cd ~/catkin_ws_rss/
    catkin_make
    source devel/setup.bash
    ```

4.  **Launch the Simulation:**
    In a new terminal window, start the TurtleBot3 environment:
    ```bash
    roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
    ```

5.  **Run the Nodes:**
    In another terminal, use `rosrun` or `roslaunch` depending on the assignment. For example, to run PA 2:
    ```bash
    rosrun rss_linux_pkg davidakerele_square.py
    ```

## 👨‍💻 Author
**David Akerele**
