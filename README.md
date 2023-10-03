nav_house

Description:
nav_house is a repository containing code and resources for an indoor robot navigation project. The project involves designing a robot capable of navigating within a house environment using Fusion 360 for robot design, Gazebo for simulation, and ROS for implementing navigation algorithms.

Project Overview:
The goal of this project is to create a robot that can autonomously navigate through indoor spaces. The robot is designed using Fusion 360, and simulation files for Gazebo (URDF and SDF) are provided. The project utilizes ROS (Robot Operating System) for implementing mapping, localization, and navigation algorithms, including the use of the slam and nav2 toolbox.

Features:

    Fusion 360 design files for the robot.
    Gazebo simulation files for URDF and SDF formats.
    ROS packages for implementing slam and navigation algorithms.
    Custom map creation in Gazebo for dynamic obstacle avoidance.

Project Structure:

    /fusion_360_files: Contains Fusion 360 design files for the robot.
    /gazebo_simulation: Includes Gazebo simulation files in URDF and SDF formats.
    /ros_packages: ROS packages for implementing slam and navigation.

Getting Started:

    Clone the repository:

    bash

    git clone https://github.com/Hemanth95/nav_house.git
    cd nav_house

    Explore the respective directories for Fusion 360 files, Gazebo simulation, and ROS packages.

Simulation Instructions:

    Launch Gazebo simulation:

    bash

roslaunch gazebo_simulation main.launch

Run the navigation stack:

bash

    roslaunch ros_packages navigation.launch

Contributing:
Contributions are welcome! If you find a bug or have an enhancement in mind, please open an issue or submit a pull request.

License:
This project is licensed under the MIT License.

Acknowledgments:

    Thanks to the open-source community for providing tools like Fusion 360, Gazebo, and ROS.
    Inspiration for this project comes from the desire to explore indoor robot navigation.

Feel free to explore, modify, and contribute to this project. Happy coding!
