# PA 6 Config Snippets

## package.xml
Ensure you have the following lines in your `package.xml`:

```xml
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
```

## CMakeLists.txt
Update your `CMakeLists.txt` with these modifications:

1. Add `message_generation` to `find_package`:
```cmake
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  message_generation
)
```

2. Add your custom service file:
```cmake
add_service_files(
  FILES
  turtlebot_move_square.srv
)
```

3. Generate added messages and services:
```cmake
generate_messages(
  DEPENDENCIES
  std_msgs
)
```

4. Uncomment or modify `catkin_package`:
```cmake
catkin_package(
  CATKIN_DEPENDS rospy std_msgs geometry_msgs message_runtime
)
```

After these changes, run `catkin_make` in your `~/catkin_ws_rss/` directory.
