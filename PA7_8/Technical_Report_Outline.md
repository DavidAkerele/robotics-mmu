# Technical Report: Mobile Robot SLAM in Highly Dynamic Environments

**Word Count Target:** 1,000 - 1,500 words

---

## 1. Title
*Suggested:* "Navigating the Unpredictable: Advances in Mobile Robot Simultaneous Localisation and Mapping (SLAM) within Highly Dynamic Environments"

## 2. Abstract (approx. 100 words)
* Summarize the entire report: Briefly explain what SLAM is, mention the critical issue of dynamic environments (e.g., humans walking, objects moving), highlight the state-of-the-art solutions analyzed (like Deep Learning-based visual SLAM), and state the main conclusion regarding future research directions.

## 3. Background (approx. 200 words)
* Define SLAM (Simultaneous Localisation and Mapping).
* Explain how traditional SLAM (like purely geometric approaches) works on the assumption that the environment is completely static.
* Explain the importance of SLAM in modern robotics (autonomous driving, warehouse logistics, service robots).

## 4. Challenges Across Academia and Industry (approx. 250 words)
* **The "Dynamic" Problem:** When moving objects (like humans or other vehicles) are treated as static features, it corrupts the map and leads to severe localization failure (the robot gets "lost").
* **Industry perspective:** Autonomous warehouses (like Amazon) have forklifts and people constantly moving. False mapping of these dynamic entities causes path-planning algorithms to fail.
* **Academia perspective:** The heavy computational cost of running object-detection algorithms in real-time alongside standard SLAM pipelines.

## 5. State-of-the-Art Solutions & Pros/Cons (approx. 400 words)
* **Solution 1: Geometry-based filtering (e.g., Epipolar geometry constraints)**
  * *Pros:* Lightweight, doesn't require massive datasets to train.
  * *Cons:* Fails if the dynamic object takes up too much of the camera's field of view, or moves very slowly.
* **Solution 2: Deep Learning Semantic Segmentation (e.g., DynaSLAM)**
  * *How it works:* Uses neural networks (like Mask R-CNN) to detect "movable" objects (cars, people) and mask them out of the SLAM pipeline.
  * *Pros:* Highly accurate, creates perfectly clean static maps.
  * *Cons:* Computationally expensive; struggles to run in real-time on lightweight mobile robots without an edge-AI GPU.
* **Solution 3: Sensor Fusion (LiDAR + Vision + IMU)**
  * *Pros:* Highly robust, works in various lighting conditions.
  * *Cons:* Expensive hardware, complex calibration.

## 6. Future Works to Improve Solutions (approx. 200 words)
* **Edge AI Acceleration:** Implementing low-power tensor processing units (TPUs) directly on mobile robots to speed up semantic SLAM without draining battery.
* **Lifelong / Persistent SLAM:** Algorithms that don't just "ignore" dynamic objects, but actively track them to predict crowd movement, which is essential for safe human-robot collaboration.

## 7. Conclusion (approx. 150 words)
* Restate the core problem: Dynamic environments remain a significant hurdle.
* Summarize that while Deep Learning offers the best accuracy (DynaSLAM), computational trade-offs necessitate further hardware and algorithmic optimization.

## 8. Self-Reflection of the RSS Unit (approx. 150 words)
* Reflect on how building the publisher/subscriber nodes (PAs 1-6) gave you a practical understanding of how SLAM nodes might communicate within a ROS ecosystem.
* Discuss how theoretical lectures informed your ability to critically analyze complex robotics literature for this report.

## 9. References
* *Note: Use academic formatting (Harvard/APA). Find 5-7 recent papers (2020-2026) via Google Scholar on "Dynamic SLAM", "DynaSLAM", or "Visual SLAM in dynamic environments".*
